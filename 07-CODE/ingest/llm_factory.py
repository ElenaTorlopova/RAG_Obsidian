"""
LLM & Embedding Factory
========================
Kapselt die KISSKI-spezifische Client-Konfiguration.
Gecacht via lru_cache – alle Pipelines teilen dieselbe Instanz.
"""

from functools import lru_cache
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import KISSKI_API_KEY, KISSKI_BASE_URL, LLM_MODEL, LLM_TEMPERATURE, EMBEDDING_MODEL


@lru_cache(maxsize=1)
def get_llm(model: str = LLM_MODEL, temperature: float = LLM_TEMPERATURE) -> ChatOpenAI:
    """ChatOpenAI gegen den KISSKI-Endpunkt."""
    print(f"[Factory] Lade LLM-Modell: {LLM_MODEL}")
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        api_key=KISSKI_API_KEY,
        base_url=KISSKI_BASE_URL,
    )


@lru_cache(maxsize=1)
def get_embeddings(model: str = EMBEDDING_MODEL) -> HuggingFaceEmbeddings:
    """Lokale Sentence-Transformer-Embeddings (kein API-Key nötig).
    Beim ersten Aufruf wird das Modell heruntergeladen (~420 MB)."""
    print(f"[Factory] Lade Embedding-Modell: {model}")
    return HuggingFaceEmbeddings(
        model_name=model,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
