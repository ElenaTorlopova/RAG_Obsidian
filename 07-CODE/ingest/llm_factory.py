"""
LLM & Embedding Factory
========================
Kapselt die KISSKI-spezifische Client-Konfiguration.

KISSKI nutzt einen OpenAI-kompatiblen Endpunkt, daher verwenden wir
ChatOpenAI mit überschriebenem base_url – LangChain trackt automatisch
über LangSmith sobald LANGCHAIN_TRACING_V2=true gesetzt ist.

Embeddings: Da KISSKI kein Embedding-Modell anbietet, nutzen wir
HuggingFaceEmbeddings (sentence-transformers) lokal.
Das ist kostenlos, offline-fähig und gut für Deutsch + Englisch.
"""

from __future__ import annotations
from functools import lru_cache

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# Modell-Empfehlungen für stabile Ausgaben (kein Function-Call-Ghosting):
#   Gut:   meta-llama-3.1-70b-instruct  (empfohlen für Produktion)
#   Ok:    mistral-7b-instruct-v0.3      (weniger Function-Call-Anfälligkeit als Llama 8B)
#   Debug: meta-llama-3.1-8b-instruct   (schnell, aber anfällig für Fehlmuster)

from config import (
    KISSKI_API_KEY,
    KISSKI_BASE_URL,
    LLM_MODEL,
    LLM_TEMPERATURE,
    EMBEDDING_MODEL,
)


@lru_cache(maxsize=1)
def get_llm(
    model: str = LLM_MODEL,
    temperature: float = LLM_TEMPERATURE,
    run_name: str | None = None,
) -> ChatOpenAI:
    """
    Gibt ein gecachtes ChatOpenAI-Objekt zurück das gegen KISSKI spricht.

    LangSmith-Tracing ist automatisch aktiv wenn LANGCHAIN_TRACING_V2=true.
    run_name erscheint als Label im LangSmith-Trace.
    """
    kwargs: dict = dict(
        model=model,
        temperature=temperature,
        api_key=KISSKI_API_KEY,
        base_url=KISSKI_BASE_URL,
        # LangSmith-Metadaten
        metadata={"provider": "KISSKI", "base_url": KISSKI_BASE_URL},
    )
    if run_name:
        kwargs["tags"] = [run_name]

    return ChatOpenAI(**kwargs)


@lru_cache(maxsize=1)
def get_embeddings(model: str = EMBEDDING_MODEL) -> HuggingFaceEmbeddings:
    """
    Gibt gecachte HuggingFace-Embeddings zurück (lokal, kein API-Key).

    Beim ersten Aufruf wird das Modell heruntergeladen (~420 MB).
    Danach gecacht unter ~/.cache/huggingface/
    """
    print(f"[Factory] Lade Embedding-Modell: {model}")
    return HuggingFaceEmbeddings(
        model_name=model,
        model_kwargs={"device": "cpu"},   # "cuda" falls GPU verfügbar
        encode_kwargs={"normalize_embeddings": True},
    )
