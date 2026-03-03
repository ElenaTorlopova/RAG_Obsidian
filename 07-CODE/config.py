"""
Zentrale Konfiguration für alle drei RAG-Pipelines.
Credentials werden ausschließlich über .env geladen – nie hardcoded.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------------
# KISSKI / AcademicCloud API (OpenAI-kompatibler Endpunkt)
# ------------------------------------------------------------------
KISSKI_API_KEY  = os.environ["KISSKI_API_KEY"]
KISSKI_BASE_URL = os.getenv("KISSKI_BASE_URL", "https://chat-ai.academiccloud.de/v1")

# Modell-Empfehlungen:
#   meta-llama-3.1-70b-instruct  → stabil, empfohlen
#   mistral-7b-instruct-v0.3     → schnell, weniger Function-Call-Anfälligkeit
#   meta-llama-3.1-8b-instruct   → schnell, aber manchmal fehlerhafte Ausgaben
LLM_MODEL       = os.getenv("LLM_MODEL", "meta-llama-3.1-8b-instruct")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.0"))

# Embeddings lokal via sentence-transformers (kein API-Key nötig)
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
)

# ------------------------------------------------------------------
# LangSmith Tracing (optional – weglassen wenn nicht gewünscht)
# ------------------------------------------------------------------
_langsmith_key = os.getenv("LANGSMITH_API_KEY", "")
if _langsmith_key:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"]    = _langsmith_key
    os.environ["LANGCHAIN_PROJECT"]    = os.getenv("LANGSMITH_PROJECT", "rag-comparison")
    os.environ["LANGCHAIN_ENDPOINT"]   = os.getenv("LANGSMITH_ENDPOINT", "https://api.smith.langchain.com")

# ------------------------------------------------------------------
# ChromaDB
# ------------------------------------------------------------------
CHROMA_BASE_PATH    = "./chroma_db"
COLLECTION_BASIC    = "rag_basic"
COLLECTION_METADATA = "rag_metadata"
COLLECTION_GRAPH    = "rag_graph_entities"

# ------------------------------------------------------------------
# Chunking & Retrieval
# ------------------------------------------------------------------
CHUNK_SIZE      = int(os.getenv("CHUNK_SIZE", "512"))
CHUNK_OVERLAP   = int(os.getenv("CHUNK_OVERLAP", "64"))
TOP_K           = int(os.getenv("TOP_K", "5"))
GRAPH_HOP_DEPTH = int(os.getenv("GRAPH_HOP_DEPTH", "2"))

# ------------------------------------------------------------------
# Dokumente
# ------------------------------------------------------------------
DOCS_PATH = os.getenv("DOCS_PATH", "./docs")

# Propmts
SOUL_PROMPT = os.getenv("./prompts")