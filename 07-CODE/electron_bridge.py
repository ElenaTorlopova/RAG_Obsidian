"""
electron_bridge.py
==================
Wird von Electron als Subprocess aufgerufen.
Gibt Ergebnisse als JSON auf stdout aus.

Aufruf:
  python electron_bridge.py <pipeline_id> <question>
  python electron_bridge.py --ingest [docs_path]

pipeline_id: "1", "2" oder "3"
"""

import sys
import json
import os
import io
import builtins

# Windows: stdout/stderr auf UTF-8 erzwingen
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# Alle print()-Ausgaben auf stderr umleiten –
# stdout ist ausschließlich für den JSON-Output reserviert.
# Verhindert dass LangChain/Loader-Logs den JSON korrumpieren.
_real_print = builtins.print
def _stderr_print(*args, **kwargs):
    kwargs.setdefault("file", sys.stderr)
    kwargs.setdefault("flush", True)
    _real_print(*args, **kwargs)
builtins.print = _stderr_print

# Sicherstellen dass das Projektverzeichnis im Pfad ist
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from pipelines.pipeline_1_basic_rag    import BasicRAGPipeline
from pipelines.pipeline_2_metadata_rag import MetadataRAGPipeline
from pipelines.pipeline_3_graph_rag    import GraphRAGPipeline
from config import DOCS_PATH

PIPELINES = {
    "1": BasicRAGPipeline,
    "2": MetadataRAGPipeline,
    "3": GraphRAGPipeline,
}


def run_query(pipeline_id: str, question: str) -> None:
    cls = PIPELINES.get(pipeline_id)
    if not cls:
        print(json.dumps({"error": f"Unbekannte Pipeline: {pipeline_id}"}))
        sys.exit(1)

    pipeline = cls()
    pipeline.load()
    result = pipeline.query(question)

    # Nur serialisierbare Felder ausgeben
    output = {
        "answer":               result.get("answer", ""),
        "latency_ms":           result.get("latency_ms", 0),
        "pipeline":             result.get("pipeline", ""),
        "graph_nodes_visited":  result.get("graph_nodes_visited", 0),
        "graph_edges_found":    result.get("graph_edges_found", 0),
        "source_documents": [
            {
                "page_content": doc.page_content[:200],
                "metadata": {
                    k: v for k, v in doc.metadata.items()
                    if isinstance(v, (str, int, float, bool))
                }
            }
            for doc in result.get("source_documents", [])
        ],
    }
    _real_print(json.dumps(output, ensure_ascii=True), file=sys.stdout, flush=True)


def run_ingest(docs_path: str | None) -> None:
    path = docs_path or DOCS_PATH
    print(f"Ingestiere aus: {path}\n", flush=True)
    for name, cls in PIPELINES.items():
        print(f"── Pipeline {name} ──", flush=True)
        p = cls()
        p.ingest(path)
        print(f"   ✓ Pipeline {name} fertig\n", flush=True)
    print("Alle Pipelines ingestiert.", flush=True)


if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print(json.dumps({"error": "Keine Argumente"}))
        sys.exit(1)

    if args[0] == "--ingest":
        docs_path = args[1] if len(args) > 1 and args[1] else None
        run_ingest(docs_path)
    else:
        if len(args) < 2:
            print(json.dumps({"error": "Aufruf: bridge.py <pipeline_id> <question>"}))
            sys.exit(1)
        pipeline_id = args[0]
        question    = args[1]
        run_query(pipeline_id, question)
