"""
Pipeline 2: RAG mit Metadaten
==============================
Moderner LCEL-Chain, Metadaten-Filter via ChromaDB where-Klausel.
"""

import time
from typing import Any

from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel
from langsmith import traceable

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import CHROMA_BASE_PATH, COLLECTION_METADATA, TOP_K
from ingest.loader import load_documents, to_langchain_docs
from ingest.llm_factory import get_llm, get_embeddings
from ingest.sanitizer import sanitize_answer

PIPELINE_TAG = "pipeline:metadata_rag"

PROMPT = PromptTemplate.from_template(
    """Du bist ein hilfreicher Assistent für akademische Inhalte. Beantworte die Frage
direkt in natürlicher Sprache. Schreibe NUR Fließtext als Antwort. Rufe keine Funktionen
auf, gib keinen Code zurück, verwende keine JSON- oder Python-Syntax. Antworte auf Deutsch.

Der Kontext enthält Textinhalte sowie strukturierte Metadaten (dcterms:, schema:, rdf:type)
aus einem Linked-Data-Wissenssystem. Nutze Metadaten (Autor, Typ, Zugehörigkeit) wenn relevant.

Kontext:
{context}

Frage: {question}

Antwort (nur Fließtext):"""
)


def _format_docs(docs) -> str:
    parts = []
    for d in docs:
        meta_lines = [
            f"  {k}: {v}" for k, v in d.metadata.items()
            if k not in ("source",) and v
        ]
        meta_str = "\n".join(meta_lines)
        parts.append(
            f"[Quelle: {d.metadata.get('source', '?')}]\n"
            f"Metadaten:\n{meta_str}\n\n{d.page_content}"
        )
    return "\n\n---\n\n".join(parts)


class MetadataRAGPipeline:

    def __init__(self):
        self.llm        = get_llm(run_name=PIPELINE_TAG)
        self.embeddings = get_embeddings()
        self.vectorstore: Chroma | None = None

    def ingest(self, docs_path: str | None = None) -> None:
        parsed  = load_documents(docs_path) if docs_path else load_documents()
        lc_docs = to_langchain_docs(parsed, include_metadata=True)
        print(f"[Pipeline 2] Ingesting {len(lc_docs)} Chunks mit Metadaten ...")
        self.vectorstore = Chroma.from_documents(
            documents=lc_docs,
            embedding=self.embeddings,
            collection_name=COLLECTION_METADATA,
            persist_directory=f"{CHROMA_BASE_PATH}/{COLLECTION_METADATA}",
        )
        print("[Pipeline 2] Ingestion abgeschlossen.")

    def load(self) -> None:
        self.vectorstore = Chroma(
            collection_name=COLLECTION_METADATA,
            embedding_function=self.embeddings,
            persist_directory=f"{CHROMA_BASE_PATH}/{COLLECTION_METADATA}",
        )

    def _make_retriever(self, metadata_filter: dict | None = None):
        search_kwargs: dict[str, Any] = {"k": TOP_K}
        if metadata_filter:
            search_kwargs["filter"] = metadata_filter
        return self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs=search_kwargs,
        )

    @traceable(name="metadata_rag_query", tags=[PIPELINE_TAG])
    def query(self, question: str, metadata_filter: dict | None = None) -> dict:
        """
        metadata_filter Beispiele:
            {"type__uri": "https://schema.org/Course"}
            {"schema__educationalLevel": "Master"}
        """
        if self.vectorstore is None:
            raise RuntimeError("Pipeline nicht initialisiert.")

        t0        = time.perf_counter()
        retriever = self._make_retriever(metadata_filter)

        setup = RunnableParallel(
            context=retriever | _format_docs,
            question=RunnablePassthrough(),
        )
        chain  = setup | PROMPT | self.llm | StrOutputParser()
        answer = sanitize_answer(chain.invoke(question))
        latency = (time.perf_counter() - t0) * 1000

        source_docs = retriever.invoke(question)

        return {
            "answer":           answer,
            "source_documents": source_docs,
            "latency_ms":       round(latency, 2),
            "pipeline":         "metadata_rag",
            "filter_used":      metadata_filter,
        }

    def get_unique_metadata_values(self, field: str) -> list[str]:
        if self.vectorstore is None:
            raise RuntimeError("Pipeline nicht initialisiert.")
        results = self.vectorstore._collection.get(include=["metadatas"])
        return sorted({m[field] for m in results["metadatas"] if field in m})
