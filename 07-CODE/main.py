"""
main.py – Einstiegspunkt für den Pipeline-Vergleich
=====================================================

Ablauf:
  1. Alle drei Pipelines initialisieren & ingestieren
  2. Testfragen definieren
  3. Benchmark ausführen
  4. Report ausgeben & speichern

Ausführung:
  python main.py --ingest   # Einmalig: Dokumente einlesen
  python main.py            # Benchmark mit bestehenden Daten
"""

import argparse
import os
from dotenv import load_dotenv

load_dotenv()  # OPENAI_API_KEY aus .env laden

from pipelines.pipeline_1_basic_rag    import BasicRAGPipeline
from pipelines.pipeline_2_metadata_rag import MetadataRAGPipeline
from pipelines.pipeline_3_graph_rag    import GraphRAGPipeline
from evaluation.evaluator              import Evaluator


# ------------------------------------------------------------------
# Testfragen – anpassen an deinen Datensatz!
# ------------------------------------------------------------------
TEST_CASES = [
    {
        "question": "Was ist ein Wissensgraph und wie unterscheidet er sich von einer Datenbank?",
        "ground_truth": (
            "Ein Wissensgraph speichert Informationen als Netzwerk von Entitäten und deren "
            "Beziehungen in Form von Tripeln (Subjekt, Prädikat, Objekt). Im Gegensatz zu "
            "relationalen Datenbanken ist er schemaflexibel und erlaubt semantische Abfragen."
        ),
        "relevant_keywords": ["Wissensgraph", "Entität", "Tripel", "RDF", "Beziehung"],
    },
    {
        "question": "Welche Dokumente sind mit dem Thema Linked Data verwandt?",
        "ground_truth": (
            "Dokumente zu RDF, SPARQL, Ontologien und dem Semantic Web sind typischerweise "
            "mit Linked Data verwandt."
        ),
        "relevant_keywords": ["Linked Data", "RDF", "SPARQL", "Semantic Web"],
    },
    {
        "question": "Wer sind die Autoren der Dokumente über maschinelles Lernen?",
        "ground_truth": "Die Autoren sind in den Metadaten der Dokumente hinterlegt.",
        "relevant_keywords": ["Autor", "maschinelles Lernen", "ML"],
    },
    {
        "question": "Wer unterrichtet den KI-Kurs im Studiengang Bibliotheksinformatik?",
        "ground_truth": "M. Eng. Janine Breßler unterrichtet den Kurs an der TH Wildau.",
        "relevant_keywords": ["Breßler", "Bibliotheksinformatik", "Wildau"],
    }
    # Füge hier weitere domänenspezifische Fragen hinzu
]


# ------------------------------------------------------------------
# Pipelines
# ------------------------------------------------------------------

def build_pipelines():
    return {
        "1_basic_rag":    BasicRAGPipeline(),
        "2_metadata_rag": MetadataRAGPipeline(),
        "3_graph_rag":    GraphRAGPipeline(),
    }


def ingest_all(pipelines: dict, docs_path: str | None = None) -> None:
    for name, pipeline in pipelines.items():
        print(f"\n>>> Ingestiere {name} ...")
        pipeline.ingest(docs_path)


def load_all(pipelines: dict) -> None:
    for name, pipeline in pipelines.items():
        print(f">>> Lade {name} ...")
        pipeline.load()


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="RAG Pipeline Vergleich")
    parser.add_argument(
        "--ingest", action="store_true",
        help="Dokumente neu einlesen (sonst wird bestehende DB genutzt)"
    )
    parser.add_argument(
        "--docs", type=str, default=None,
        help="Pfad zu den Markdown-Dokumenten (überschreibt config.DOCS_PATH)"
    )
    parser.add_argument(
        "--output", type=str, default="evaluation_results.json",
        help="Ausgabepfad für JSON-Report"
    )
    args = parser.parse_args()

    pipelines = build_pipelines()

    if args.ingest:
        ingest_all(pipelines, docs_path=args.docs)
    else:
        load_all(pipelines)

    # Benchmark
    evaluator = Evaluator()
    results = evaluator.run_benchmark(pipelines, TEST_CASES)

    # Report
    evaluator.print_report(results)
    evaluator.save_report(results, args.output)

    # Pipeline 3: Beispiel-Subgraph ausgeben
    print("\n>>> Beispiel-Subgraph für erste Testfrage:")
    pipelines["3_graph_rag"].visualize_subgraph(TEST_CASES[0]["question"])


if __name__ == "__main__":
    main()
