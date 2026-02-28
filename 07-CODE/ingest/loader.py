"""
Loader für Obsidian-artige Markdown-Dateien mit Linked-Data-Frontmatter
========================================================================

Unterstützt das spezifische Format mit:
  - Namespace-qualifizierten Feldnamen: dcterms:title, schema:provider, rdf:type ...
  - WikiLink-Syntax [[Seitenname]] für Beziehungen zu anderen Entitäten
  - Gemischten Namespaces (dcterms, schema, rdf, schem als Alias für schema)
  - Verschiedenen Notiz-Templates (Vorlesung, Person, Organisation, ...)

Verarbeitungsschritte:
  1. YAML-Frontmatter parsen
  2. [[WikiLinks]] → interne URIs auflösen  (file:///docs/Seitenname)
  3. Namespace-Präfixe → vollständige URIs expandieren
  4. Tripel (subject, predicate, object) aufbauen
  5. Dokument-URI aus Dateinamen ableiten

Namespace-Mapping:
  dcterms: → http://purl.org/dc/terms/
  schema:  → https://schema.org/
  schem:   → https://schema.org/   (Tippfehler-Alias)
  rdf:     → http://www.w3.org/1999/02/22-rdf-syntax-ns#
"""

from __future__ import annotations

import os
import re
import yaml
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import quote

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import DOCS_PATH, CHUNK_SIZE, CHUNK_OVERLAP


# ------------------------------------------------------------------
# Namespace-Registry
# ------------------------------------------------------------------

NAMESPACES: dict[str, str] = {
    "dcterms": "http://purl.org/dc/terms/",
    "schema":  "https://schema.org/",
    "schem":   "https://schema.org/",
    "rdf":     "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs":    "http://www.w3.org/2000/01/rdf-schema#",
    "owl":     "http://www.w3.org/2002/07/owl#",
    "xsd":     "http://www.w3.org/2001/XMLSchema#",
    "foaf":    "http://xmlns.com/foaf/0.1/",
    "skos":    "http://www.w3.org/2004/02/skos/core#",
}

RDF_TYPE_KEYS = {"rdf:type", "rdf:Type"}

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]")
NS_KEY_RE   = re.compile(r"^([a-zA-Z][a-zA-Z0-9]*):(.+)$")
# Namespace-Präfix in Werten: nur wenn lokaler Teil mit Großbuchstabe beginnt
# (unterscheidet schema:Course von schema:language)
NS_VAL_RE   = re.compile(r"^([a-zA-Z][a-zA-Z0-9]*):([A-Z].*)$")


# ------------------------------------------------------------------
# URI-Hilfsfunktionen
# ------------------------------------------------------------------

def _slug(name: str) -> str:
    return quote(name.replace(" ", "_"), safe="_-.")


def _wikilink_to_uri(page_name: str) -> str:
    return f"file:///docs/{_slug(page_name)}"


def _expand_namespace(value: str) -> str:
    m = NS_VAL_RE.match(str(value))
    if m:
        prefix, local = m.group(1), m.group(2)
        if prefix in NAMESPACES:
            return NAMESPACES[prefix] + local
    return value


def _expand_key_to_predicate(key: str) -> str:
    m = NS_KEY_RE.match(key)
    if m:
        prefix, local = m.group(1), m.group(2)
        if prefix in NAMESPACES:
            return NAMESPACES[prefix] + local
    return f"prop:{key}"


def _resolve_value(raw_value: str) -> str:
    s = str(raw_value).strip()
    wl = WIKILINK_RE.match(s)
    if wl:
        return _wikilink_to_uri(wl.group(1))
    if s.startswith("http://") or s.startswith("https://"):
        return s
    expanded = _expand_namespace(s)
    if expanded != s:
        return expanded
    return s


def _file_to_subject_uri(filepath: str, docs_path: str) -> str:
    rel = os.path.relpath(filepath, docs_path)
    slug = _slug(Path(rel).with_suffix("").as_posix())
    return f"file:///docs/{slug}"


# ------------------------------------------------------------------
# Datenmodell
# ------------------------------------------------------------------

@dataclass
class ParsedDocument:
    source: str
    raw_text: str
    metadata: dict[str, Any]            # Original-YAML
    resolved_metadata: dict[str, Any]   # ChromaDB-kompatibel
    subject_uri: str
    type_uri: str
    label: str
    triples: list[tuple[str, str, str]]
    wikilinks: list[str]                # WikiLinks im Body (als URIs)


# ------------------------------------------------------------------
# Parser
# ------------------------------------------------------------------

def _extract_frontmatter(content: str) -> tuple[dict, str]:
    match = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n", content, re.DOTALL)
    if match:
        try:
            meta = yaml.safe_load(match.group(1)) or {}
            if not isinstance(meta, dict):
                meta = {}
        except yaml.YAMLError as e:
            print(f"[Loader] YAML-Fehler: {e}")
            meta = {}
        body = content[match.end():]
    else:
        meta = {}
        body = content
    return meta, body


def _extract_body_wikilinks(text: str) -> list[str]:
    return [_wikilink_to_uri(m) for m in WIKILINK_RE.findall(text)]


def _build_triples(
    subject_uri: str,
    meta: dict,
) -> tuple[dict[str, Any], str, list[tuple[str, str, str]]]:
    """
    Kernfunktion: Baut RDF-Tripel aus dem YAML-Dict.

    Returns:
        resolved_metadata  – ChromaDB-kompatibles Flat-Dict
        type_uri           – rdf:type des Dokuments
        triples            – Liste von (subject, predicate, object)
    """
    triples: list[tuple[str, str, str]] = []
    resolved: dict[str, Any] = {}
    type_uri = ""

    for raw_key, raw_value in meta.items():
        predicate_uri = _expand_key_to_predicate(str(raw_key))

        if raw_value is None:
            continue

        values_raw = raw_value if isinstance(raw_value, list) else [raw_value]
        resolved_values = []

        for v in values_raw:
            if v is None:
                continue
            resolved_v = _resolve_value(str(v))
            resolved_values.append(resolved_v)
            triples.append((subject_uri, predicate_uri, resolved_v))

            if raw_key in RDF_TYPE_KEYS and not type_uri:
                type_uri = resolved_v

        if resolved_values:
            flat = ", ".join(resolved_values)
            # ChromaDB verträgt keine Doppelpunkte in Keys → __ als Trennzeichen
            safe_key = str(raw_key).replace(":", "__")
            resolved[safe_key] = flat

    return resolved, type_uri, triples


def parse_document(filepath: str, docs_path: str) -> ParsedDocument:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    meta, body = _extract_frontmatter(content)
    subject_uri = _file_to_subject_uri(filepath, docs_path)
    resolved_meta, type_uri, triples = _build_triples(subject_uri, meta)

    label = (
        str(meta.get("dcterms:title", "") or meta.get("title", ""))
        or Path(filepath).stem
    )

    body_wikilinks = _extract_body_wikilinks(body)

    # Body-WikiLinks als schwache "mentions"-Kanten
    for link_uri in body_wikilinks:
        triples.append((subject_uri, "prop:mentions", link_uri))

    return ParsedDocument(
        source=filepath,
        raw_text=body,
        metadata=meta,
        resolved_metadata=resolved_meta,
        subject_uri=subject_uri,
        type_uri=type_uri,
        label=label,
        triples=triples,
        wikilinks=body_wikilinks,
    )


# ------------------------------------------------------------------
# Public API
# ------------------------------------------------------------------

def load_documents(docs_path: str = DOCS_PATH) -> list[ParsedDocument]:
    """Lädt alle .md-Dateien rekursiv und gibt ParsedDocuments zurück."""
    parsed = []
    docs_path = os.path.abspath(docs_path)

    for root, _, files in os.walk(docs_path):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            try:
                doc = parse_document(fpath, docs_path)
                parsed.append(doc)
            except Exception as e:
                print(f"[Loader] Fehler bei '{fpath}': {e}")

    # Statistik
    type_counts: dict[str, int] = {}
    for d in parsed:
        t = d.type_uri or "unbekannt"
        type_counts[t] = type_counts.get(t, 0) + 1

    total_triples = sum(len(d.triples) for d in parsed)
    total_links   = sum(len(d.wikilinks) for d in parsed)

    print(f"\n[Loader] {len(parsed)} Dokumente aus '{docs_path}'")
    print(f"[Loader] Tripel: {total_triples}  |  Body-WikiLinks: {total_links}")
    print("[Loader] Dokument-Typen (rdf:type):")
    for t, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        short = t.split("/")[-1].split("#")[-1] or t
        print(f"          {count:4d}x  {short}")

    return parsed


def to_langchain_docs(
    parsed_docs: list[ParsedDocument],
    include_metadata: bool = False,
) -> list[Document]:
    """
    Wandelt ParsedDocuments in LangChain-Documents um.

    include_metadata=False → Pipeline 1 (reines RAG)
    include_metadata=True  → Pipeline 2 & 3
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        # Sinnvolle Trennstellen für Vorlesungsnotizen
        separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", " "],
    )

    lc_docs: list[Document] = []

    for doc in parsed_docs:
        base_meta: dict[str, Any] = {
            "source":    doc.source,
            "doc_label": doc.label,
        }

        if include_metadata:
            base_meta.update(doc.resolved_metadata)
            base_meta["subject_uri"] = doc.subject_uri
            base_meta["type_uri"]    = doc.type_uri

        chunks = splitter.create_documents(
            texts=[doc.raw_text],
            metadatas=[base_meta],
        )
        lc_docs.extend(chunks)

    return lc_docs


def build_uri_index(parsed_docs: list[ParsedDocument]) -> dict[str, str]:
    """
    Mapping: WikiLink-URI → tatsächliche subject_uri des Dokuments.
    Ermöglicht in Pipeline 3 die Auflösung von [[Links]] auf Graph-Knoten,
    auch wenn das Zieldokument in einem Unterordner liegt.

    Problem ohne diesen Index:
      [[Janine_Bressler]] erzeugt URI  file:///docs/Janine_Bressler
      Das Dokument liegt aber unter    file:///docs/Personen/Janine_Bressler
      → Ohne Alias: zwei isolierte Knoten im Graph

    Lösung – drei Alias-Einträge pro Dokument:
      1. Exakte subject_uri          (file:///docs/Personen/Janine_Bressler)
      2. Label-basierte URI          (file:///docs/M._Eng._Janine_Bre%C3%9Fler)
      3. Dateiname ohne Pfad/Suffix  (file:///docs/Janine_Bressler)
         → matcht [[Janine_Bressler]] unabhängig vom Unterordner

    Bei Namenskollisionen (gleichnamige Dateien in verschiedenen Ordnern)
    gewinnt das zuletzt geladene Dokument – wird im Log gewarnt.
    """
    index: dict[str, str] = {}

    for doc in parsed_docs:
        real_uri = doc.subject_uri

        candidates = [
            real_uri,                                          # 1. exakte URI
            f"file:///docs/{_slug(doc.label)}",               # 2. Label
            f"file:///docs/{_slug(Path(doc.source).stem)}",   # 3. Dateiname ohne Pfad
        ]

        for alias in candidates:
            if alias in index and index[alias] != real_uri:
                print(
                    f"[Loader] Warnung: WikiLink-Kollision für '{alias}'"
                    f"\n         '{index[alias]}' wird überschrieben durch '{real_uri}'"
                )
            index[alias] = real_uri

    return index
