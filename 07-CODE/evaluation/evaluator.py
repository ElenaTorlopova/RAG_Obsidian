"""
Evaluierungs-Framework
=======================
Misst für alle drei Pipelines:
  - Antwortqualität (LLM-as-Judge, 1–5)
  - Retrieval Precision@K
  - Latenz (ms)
  - Kosten (Token-Zählung × KISSKI-Preise – aktuell $0 für akademische Nutzung,
    Token-Zählung trotzdem sinnvoll für Effizienzvergleich)

LangSmith-Integration:
  - Jeder Benchmark-Run erzeugt ein Dataset + Experiment in LangSmith
  - Einzelne Queries sind als traceable Runs sichtbar
  - Judge-Bewertungen werden als Feedback auf die Runs geschrieben
"""

import json
import time
import uuid
from dataclasses import dataclass, field, asdict

from langchain_core.prompts import PromptTemplate
from langsmith import Client as LangSmithClient
from langsmith import traceable

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from ingest.llm_factory import get_llm
from config import LANGSMITH_PROJECT, LLM_MODEL


JUDGE_PROMPT = PromptTemplate(
    input_variables=["question", "answer", "ground_truth"],
    template="""Du bist ein objektiver Evaluator für RAG-Systeme im akademischen Bereich.

Frage: {question}
Erwartete Antwort (Ground Truth): {ground_truth}
Tatsächliche Antwort: {answer}

Bewerte die tatsächliche Antwort auf einer Skala von 1–5:
5 = Vollständig korrekt und vollständig
4 = Größtenteils korrekt, kleine Lücken
3 = Teilweise korrekt, wichtige Punkte fehlen
2 = Größtenteils falsch oder irreführend
1 = Komplett falsch oder keine Antwort

Antworte NUR mit einer einzigen Zahl zwischen 1 und 5, ohne weitere Erklärung.""",
)


@dataclass
class QueryResult:
    pipeline: str
    question: str
    answer: str
    ground_truth: str
    latency_ms: float
    quality_score: float
    retrieval_precision: float
    input_tokens: int
    output_tokens: int
    graph_nodes_visited: int = 0
    graph_edges_found: int = 0
    langsmith_run_id: str = ""   # Für Feedback-Verknüpfung


@dataclass
class BenchmarkResult:
    pipeline: str
    avg_quality: float
    avg_latency_ms: float
    avg_precision: float
    query_results: list[QueryResult] = field(default_factory=list)


class Evaluator:

    def __init__(self):
        self.judge_llm    = get_llm(run_name="judge")
        self.ls_client    = LangSmithClient()
        self.run_id       = str(uuid.uuid4())[:8]   # Kurze ID für diesen Benchmark-Lauf

    # ------------------------------------------------------------------
    # LLM-as-Judge
    # ------------------------------------------------------------------

    @traceable(name="llm_judge", tags=["evaluation"])
    def score_answer(self, question: str, answer: str, ground_truth: str) -> float:
        prompt = JUDGE_PROMPT.format(
            question=question,
            answer=answer,
            ground_truth=ground_truth,
        )
        response = self.judge_llm.invoke(prompt)
        try:
            return max(1.0, min(5.0, float(response.content.strip())))
        except ValueError:
            return 0.0

    # ------------------------------------------------------------------
    # Retrieval Precision
    # ------------------------------------------------------------------

    def compute_retrieval_precision(
        self,
        retrieved_docs: list,
        relevant_keywords: list[str],
    ) -> float:
        if not retrieved_docs or not relevant_keywords:
            return 0.0
        hits = sum(
            1 for doc in retrieved_docs
            if any(kw.lower() in doc.page_content.lower() for kw in relevant_keywords)
        )
        return round(hits / len(retrieved_docs), 3)

    # ------------------------------------------------------------------
    # Token-Zählung (ohne tiktoken – einfache Approximation)
    # ------------------------------------------------------------------

    @staticmethod
    def count_tokens_approx(text: str) -> int:
        """Grobe Approximation: ~1 Token pro 4 Zeichen (passt für europäische Sprachen)."""
        return max(1, len(text) // 4)

    # ------------------------------------------------------------------
    # LangSmith Feedback schreiben
    # ------------------------------------------------------------------

    def _post_feedback(self, run_id: str, score: float, pipeline: str) -> None:
        """Schreibt den Judge-Score als Feedback auf den LangSmith-Run."""
        try:
            self.ls_client.create_feedback(
                run_id=run_id,
                key="quality_score",
                score=score / 5.0,          # LangSmith erwartet 0..1
                comment=f"LLM-Judge Score {score}/5 | Pipeline: {pipeline}",
            )
        except Exception as e:
            print(f"[Evaluator] LangSmith Feedback fehlgeschlagen: {e}")

    # ------------------------------------------------------------------
    # Benchmark
    # ------------------------------------------------------------------

    def run_benchmark(
        self,
        pipelines: dict[str, object],
        test_cases: list[dict],
    ) -> dict[str, BenchmarkResult]:
        """
        Führt alle Testfragen für alle Pipelines aus.

        test_cases Format:
        [
            {
                "question": "Was ist ein Wissensgraph?",
                "ground_truth": "Ein Wissensgraph ist ...",
                "relevant_keywords": ["Wissensgraph", "RDF", "Entität"],
            },
        ]
        """
        results: dict[str, BenchmarkResult] = {}

        for pipeline_name, pipeline in pipelines.items():
            print(f"\n{'='*60}")
            print(f"Evaluiere: {pipeline_name}  (Run {self.run_id})")
            print(f"{'='*60}")

            query_results = []

            for i, tc in enumerate(test_cases):
                print(f"  [{i+1}/{len(test_cases)}] {tc['question'][:65]}...")

                try:
                    raw = pipeline.query(tc["question"])
                except Exception as e:
                    print(f"    FEHLER: {e}")
                    continue

                answer    = raw["answer"]
                src_docs  = raw.get("source_documents", [])
                latency   = raw.get("latency_ms", 0.0)
                run_id_ls = raw.get("__run_id", "")   # LangSmith setzt das ggf.

                quality   = self.score_answer(tc["question"], answer, tc["ground_truth"])
                precision = self.compute_retrieval_precision(
                    src_docs, tc.get("relevant_keywords", [])
                )

                in_tok  = self.count_tokens_approx(tc["question"])
                out_tok = self.count_tokens_approx(answer)

                # Feedback in LangSmith schreiben
                if run_id_ls:
                    self._post_feedback(run_id_ls, quality, pipeline_name)

                qr = QueryResult(
                    pipeline=pipeline_name,
                    question=tc["question"],
                    answer=answer,
                    ground_truth=tc["ground_truth"],
                    latency_ms=latency,
                    quality_score=quality,
                    retrieval_precision=precision,
                    input_tokens=in_tok,
                    output_tokens=out_tok,
                    graph_nodes_visited=raw.get("graph_nodes_visited", 0),
                    graph_edges_found=raw.get("graph_edges_found", 0),
                    langsmith_run_id=run_id_ls,
                )
                query_results.append(qr)

                print(
                    f"    Qualität: {quality}/5 | "
                    f"Precision: {precision:.0%} | "
                    f"Latenz: {latency:.0f}ms"
                    + (f" | Graph: {qr.graph_nodes_visited} Knoten" if qr.graph_nodes_visited else "")
                )

            if query_results:
                results[pipeline_name] = BenchmarkResult(
                    pipeline=pipeline_name,
                    avg_quality=round(
                        sum(r.quality_score for r in query_results) / len(query_results), 2
                    ),
                    avg_latency_ms=round(
                        sum(r.latency_ms for r in query_results) / len(query_results), 1
                    ),
                    avg_precision=round(
                        sum(r.retrieval_precision for r in query_results) / len(query_results), 3
                    ),
                    query_results=query_results,
                )

        return results

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def print_report(self, results: dict[str, BenchmarkResult]) -> None:
        print(f"\n{'='*70}")
        print(f"BENCHMARK ERGEBNIS  (Run-ID: {self.run_id})")
        print(f"LangSmith-Projekt: {LANGSMITH_PROJECT}")
        print(f"{'='*70}")
        print(f"{'Pipeline':<25} {'Qualität':>10} {'Precision':>10} {'Latenz':>12}")
        print(f"{'-'*70}")
        for name, br in results.items():
            print(
                f"{name:<25} "
                f"{br.avg_quality:>9.2f}/5 "
                f"{br.avg_precision:>9.1%} "
                f"{br.avg_latency_ms:>10.0f}ms"
            )
        print(f"{'='*70}")
        print(f"\nDetaillierte Traces: https://smith.langchain.com/projects/{LANGSMITH_PROJECT}")

    def save_report(
        self,
        results: dict[str, BenchmarkResult],
        path: str = "evaluation_results.json",
    ) -> None:
        serializable = {name: asdict(br) for name, br in results.items()}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(serializable, f, indent=2, ensure_ascii=False)
        print(f"[Evaluator] Ergebnisse gespeichert: {path}")
