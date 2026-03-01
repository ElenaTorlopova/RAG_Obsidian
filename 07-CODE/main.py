"""
main.py – Einstiegspunkt für den Pipeline-Vergleich
=====================================================

Ausführung:
  python main.py --ingest          # Einmalig: Dokumente einlesen & indexieren
  python main.py --ingest --docs ./meine_docs

  python main.py --query "Was ist maschinelles Lernen?"
  python main.py --query "Wer unterrichtet den KI-Kurs?" --pipeline 3
"""

import argparse
import json
from dotenv import load_dotenv

load_dotenv()

from pipelines.pipeline_1_basic_rag import BasicRAGPipeline
from pipelines.pipeline_2_metadata_rag import MetadataRAGPipeline
from pipelines.pipeline_3_graph_rag import GraphRAGPipeline


def build_pipelines() -> dict:
    return {
        "1": BasicRAGPipeline(),
        "2": MetadataRAGPipeline(),
        "3": GraphRAGPipeline(),
    }


def ingest_all(pipelines: dict, docs_path: str | None = None) -> None:
    for name, pipeline in pipelines.items():
        print(f"\n>>> Ingestiere Pipeline {name} ...")
        pipeline.ingest(docs_path)


def load_all(pipelines: dict) -> None:
    for name, pipeline in pipelines.items():
        pipeline.load()


def run_query(pipelines: dict, question: str, pipeline_id: str | None = None) -> None:
    """
    Stellt eine Frage an eine oder alle Pipelines und gibt die Antworten aus.
    pipeline_id: "1", "2", "3" oder None für alle drei.
    """
    targets = {pipeline_id: pipelines[pipeline_id]} if pipeline_id else pipelines

    for name, pipeline in targets.items():
        label = {
            "1": "Basic RAG",
            "2": "Metadata RAG",
            "3": "Graph RAG",
        }.get(name, name)

        print(f"\n{'='*60}")
        print(f"Pipeline {name}: {label}")
        print(f"{'='*60}")

        result = pipeline.query(question)

        print(f"Antwort:\n{result['answer']}")
        print(f"\nLatenz: {result['latency_ms']} ms")

        if result.get("graph_nodes_visited"):
            print(f"Graph: {result['graph_nodes_visited']} Knoten besucht, "
                  f"{result['graph_edges_found']} Kanten gefunden")

        print(f"\nQuellen ({len(result['source_documents'])}):")
        seen = set()
        for doc in result["source_documents"]:
            src = doc.metadata.get("doc_label") or doc.metadata.get("source", "?")
            if src not in seen:
                print(f"  · {src}")
                seen.add(src)


def main():
    parser = argparse.ArgumentParser(description="RAG Pipeline Vergleich")
    parser.add_argument(
        "--ingest", action="store_true",
        help="Dokumente einlesen und indexieren (einmalig nötig)"
    )
    parser.add_argument(
        "--docs", type=str, default=None,
        help="Pfad zu den Markdown-Dokumenten (überschreibt DOCS_PATH in config.py)"
    )
    parser.add_argument(
        "--query", type=str, default=None,
        help="Frage die an die Pipelines gestellt wird"
    )
    parser.add_argument(
        "--pipeline", type=str, choices=["1", "2", "3"], default=None,
        help="Nur eine bestimmte Pipeline nutzen (Standard: alle drei)"
    )
    args = parser.parse_args()

    pipelines = build_pipelines()

    if args.ingest:
        ingest_all(pipelines, docs_path=args.docs)
        print("\n✓ Ingestion abgeschlossen. Starte Queries mit: python main.py --query '...'")
        return

    load_all(pipelines)

    if args.query:
        run_query(pipelines, args.query, args.pipeline)
    else:
        # Interaktiver Modus
        print("\nRAG Pipeline Vergleich – Interaktiver Modus")
        print("Pipelines: 1=Basic RAG  2=Metadata RAG  3=Graph RAG")
        print("Beenden mit: exit\n")
        while True:
            try:
                question = input("Frage: ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if not question or question.lower() == "exit":
                break
            pid = input("Pipeline [1/2/3/alle]: ").strip()
            pid = pid if pid in ("1", "2", "3") else None
            run_query(pipelines, question, pid)


if __name__ == "__main__":
    main()
