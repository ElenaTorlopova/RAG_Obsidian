"""
Zentrale Konfiguration für alle drei RAG-Pipelines.

Credentials werden ausschließlich über .env geladen – nie hardcoded.
Kopiere .env.example zu .env und trage deine Keys ein.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------------
# KISSKI / AcademicCloud API (OpenAI-kompatibler Endpunkt)
# ------------------------------------------------------------------
KISSKI_API_KEY  = os.environ["KISSKI_API_KEY"]      # Pflicht – bricht sonst früh
KISSKI_BASE_URL = os.getenv("KISSKI_BASE_URL", "https://chat-ai.academiccloud.de/v1")

# Verfügbare Modelle auf KISSKI z.B.:
#   meta-llama-3.1-8b-instruct
#   meta-llama-3.1-70b-instruct
#   mistral-7b-instruct-v0.3
LLM_MODEL       = os.getenv("LLM_MODEL", "meta-llama-3.1-8b-instruct")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.0"))

# Embedding-Modell – KISSKI stellt keins bereit, daher lokales Sentence-Transformer-Modell.
# Alternativ: jedes OpenAI-kompatible Embedding-Modell falls verfügbar.
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",  # gut für Deutsch + Englisch
)

# ------------------------------------------------------------------
# LangSmith Tracing
# ------------------------------------------------------------------
LANGSMITH_API_KEY   = os.environ["LANGSMITH_API_KEY"]      # Pflicht
LANGSMITH_PROJECT   = os.getenv("LANGSMITH_PROJECT", "rag-comparison")
LANGSMITH_ENDPOINT  = os.getenv("LANGSMITH_ENDPOINT", "https://api.smith.langchain.com")

# LangSmith liest diese Umgebungsvariablen automatisch –
# wir setzen sie hier explizit damit sie sicher gesetzt sind,
# auch wenn load_dotenv() bereits oben aufgerufen wurde.
os.environ["LANGCHAIN_TRACING_V2"]  = "true"
os.environ["LANGCHAIN_API_KEY"]     = LANGSMITH_API_KEY
os.environ["LANGCHAIN_PROJECT"]     = LANGSMITH_PROJECT
os.environ["LANGCHAIN_ENDPOINT"]    = LANGSMITH_ENDPOINT

# ------------------------------------------------------------------
# ChromaDB
# ------------------------------------------------------------------
CHROMA_BASE_PATH      = "./chroma_db"
COLLECTION_BASIC      = "rag_basic"
COLLECTION_METADATA   = "rag_metadata"
COLLECTION_GRAPH      = "rag_graph_entities"

# ------------------------------------------------------------------
# Chunking
# ------------------------------------------------------------------
CHUNK_SIZE    = int(os.getenv("CHUNK_SIZE", "512"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "64"))

# ------------------------------------------------------------------
# Retrieval
# ------------------------------------------------------------------
TOP_K           = int(os.getenv("TOP_K", "5"))
GRAPH_HOP_DEPTH = int(os.getenv("GRAPH_HOP_DEPTH", "2"))

# ------------------------------------------------------------------
# Dokumente
# ------------------------------------------------------------------
DOCS_PATH = os.getenv("DOCS_PATH", "./docs")
