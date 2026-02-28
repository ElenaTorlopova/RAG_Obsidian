"""
Pipeline 1: Reines RAG
======================
Moderner LCEL-Chain statt depreciertem RetrievalQA.
"""

import time
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langsmith import traceable

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import CHROMA_BASE_PATH, COLLECTION_BASIC, TOP_K
from ingest.loader import load_documents, to_langchain_docs
from ingest.llm_factory import get_llm, get_embeddings
from ingest.sanitizer import sanitize_answer

PIPELINE_TAG = "pipeline:basic_rag"

PROMPT = PromptTemplate.from_template(
    """Du bist ein hilfreicher Assistent. Beantworte die Frage direkt in natürlicher Sprache.
Schreibe NUR Fließtext als Antwort. Rufe keine Funktionen auf, gib keinen Code zurück,
verwende keine JSON- oder Python-Syntax. Antworte auf Deutsch.

Kontext:
{context}

Frage: {question}

Antwort (nur Fließtext):"""
)


def _format_docs(docs) -> str:
    return "\n\n---\n\n".join(
        f"[Quelle: {d.metadata.get('source', '?')}]\n{d.page_content}" for d in docs
    )


class BasicRAGPipeline:

    def __init__(self):
        self.llm        = get_llm(run_name=PIPELINE_TAG)
        self.embeddings = get_embeddings()
        self.vectorstore: Chroma | None = None
        self.retriever  = None
        self.chain      = None

    def ingest(self, docs_path: str | None = None) -> None:
        parsed  = load_documents(docs_path) if docs_path else load_documents()
        lc_docs = to_langchain_docs(parsed, include_metadata=False)
        print(f"[Pipeline 1] Ingesting {len(lc_docs)} Chunks ...")
        self.vectorstore = Chroma.from_documents(
            documents=lc_docs,
            embedding=self.embeddings,
            collection_name=COLLECTION_BASIC,
            persist_directory=f"{CHROMA_BASE_PATH}/{COLLECTION_BASIC}",
        )
        self._build_chain()
        print("[Pipeline 1] Ingestion abgeschlossen.")

    def load(self) -> None:
        self.vectorstore = Chroma(
            collection_name=COLLECTION_BASIC,
            embedding_function=self.embeddings,
            persist_directory=f"{CHROMA_BASE_PATH}/{COLLECTION_BASIC}",
        )
        self._build_chain()

    def _build_chain(self) -> None:
        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": TOP_K},
        )
        # LCEL: retriever → prompt → llm → parser
        setup = RunnableParallel(
            context=self.retriever | _format_docs,
            question=RunnablePassthrough(),
        )
        self.chain = setup | PROMPT | self.llm | StrOutputParser()

    @traceable(name="basic_rag_query", tags=[PIPELINE_TAG])
    def query(self, question: str) -> dict:
        if self.chain is None:
            raise RuntimeError("Pipeline nicht initialisiert.")

        t0      = time.perf_counter()
        answer  = sanitize_answer(self.chain.invoke(question))
        latency = (time.perf_counter() - t0) * 1000

        # Dokumente separat holen für Precision-Berechnung
        source_docs = self.retriever.invoke(question)

        return {
            "answer":           answer,
            "source_documents": source_docs,
            "latency_ms":       round(latency, 2),
            "pipeline":         "basic_rag",
        }
