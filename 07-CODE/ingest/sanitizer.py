"""
Output-Sanitizer
================
Fängt fehlerhafte LLM-Ausgaben ab, die entstehen wenn kleinere Modelle
(z.B. Llama 3.1 8B) trotz Prompt-Anweisung Function-Call-Syntax ausgeben.

Typische Fehlmuster:
  get_author_of_document("02_ML")
  {"function": "search", "args": {...}}
  <tool_call>...</tool_call>
  [TOOL_CALLS] [{"name": ...}]
"""

import re

# Muster die auf einen fehlerhaften Function-Call hindeuten
_FUNCTION_CALL_PATTERNS = [
    # Python-artige Funktionsaufrufe: foo("bar") oder foo_bar(...)
    re.compile(r'^\s*\w+\s*\(.*\)\s*$', re.DOTALL),
    # JSON-Objekt mit "function" oder "tool" Key
    re.compile(r'^\s*\{.*"(?:function|tool|name|action)".*\}.*$', re.DOTALL),
    # XML-artige Tool-Tags
    re.compile(r'<tool_call>.*</tool_call>', re.DOTALL | re.IGNORECASE),
    re.compile(r'<function_calls>.*</function_calls>', re.DOTALL | re.IGNORECASE),
    # Llama-spezifische Marker
    re.compile(r'^\s*\[TOOL_CALLS\]', re.MULTILINE),
    re.compile(r'^\s*\[/?INST\]', re.MULTILINE),
]

_FALLBACK_MESSAGE = (
    "Das Modell konnte keine direkte Antwort generieren. "
    "Bitte versuche die Frage umzuformulieren oder wechsle zu einem größeren Modell "
    "(z.B. meta-llama-3.1-70b-instruct)."
)


def is_function_call(text: str) -> bool:
    """Gibt True zurück wenn der Text wie ein Function-Call aussieht."""
    stripped = text.strip()
    return any(p.search(stripped) for p in _FUNCTION_CALL_PATTERNS)


def sanitize_answer(text: str) -> str:
    """
    Bereinigt die LLM-Ausgabe.
    - Entfernt Tool-Tags falls vorhanden aber Resttext noch sinnvoll
    - Ersetzt reine Function-Call-Ausgaben durch eine Fehlermeldung
    - Loggt den Originaltext zur Fehleranalyse in LangSmith
    """
    if not text or not text.strip():
        return _FALLBACK_MESSAGE

    cleaned = text.strip()

    # Tool-Tags entfernen, Rest behalten
    cleaned = re.sub(r'<tool_call>.*?</tool_call>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
    cleaned = re.sub(r'<function_calls>.*?</function_calls>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
    cleaned = re.sub(r'\[TOOL_CALLS\].*', '', cleaned, flags=re.DOTALL)
    cleaned = cleaned.strip()

    # Wenn nach dem Bereinigen nichts sinnvolles übrig bleibt
    if not cleaned or is_function_call(cleaned):
        print(f"[Sanitizer] ⚠️  Function-Call-Output erkannt, ersetze durch Fallback.\n"
              f"            Original: {text[:120]!r}")
        return _FALLBACK_MESSAGE

    return cleaned
