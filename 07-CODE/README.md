# RAG Pipeline Vergleich

Drei Pipelines, ein Benchmark – um objektiv zu messen, was Metadaten und Linked Data bringen.

## Pipelines

| Pipeline | Beschreibung |
|---|---|
| **1 – Basic RAG** | Nur Markdown-Text, kein Kontext |
| **2 – Metadata RAG** | Text + YAML-Metadaten (dcterms, schema, rdf) als ChromaDB-Filter |
| **3 – GraphRAG** | Text + Metadaten + Wissensgraph (NetworkX) mit WikiLink-Traversal |

## Setup

```bash
pip install -r requirements.txt

cp .env.example .env
# .env öffnen und Keys eintragen:
#   KISSKI_API_KEY=...
#   LANGSMITH_API_KEY=...
```

## Ausführung

```bash
# Einmalig: Dokumente einlesen und indexieren
python main.py --ingest --docs ./docs

# Benchmark mit bestehenden Daten
python main.py --output results.json
```

## Konfiguration (`.env`)

| Variable | Pflicht | Beschreibung |
|---|---|---|
| `KISSKI_API_KEY` | ✅ | API-Key vom KISSKI/GWDG-Portal |
| `KISSKI_BASE_URL` | – | Default: `https://chat-ai.academiccloud.de/v1` |
| `LLM_MODEL` | – | Default: `meta-llama-3.1-8b-instruct` |
| `LANGSMITH_API_KEY` | ✅ | API-Key aus smith.langchain.com |
| `LANGSMITH_PROJECT` | – | Default: `rag-comparison` |
| `EMBEDDING_MODEL` | – | Default: multilinguales Sentence-Transformer-Modell |

## Markdown-Format (Obsidian-Style)

```yaml
---
dcterms:title: 01_Einführung
dcterms:contributor:
  - "[[M. Eng. Janine Breßler]]"
rdf:type: schema:Course
schema:provider: "[[Technische Hochschule Wildau]]"
schema:educationalLevel: Master
---
```

**Unterstützte Namespaces:** `dcterms:`, `schema:`, `schem:` (Alias), `rdf:`, `rdfs:`, `owl:`, `foaf:`, `skos:`

**WikiLinks** (`[[Seitenname]]`) werden automatisch in interne URIs (`file:///docs/Seitenname`) aufgelöst und als Graph-Kanten gespeichert.

## LangSmith

Alle Runs landen automatisch in deinem Projekt. Was du dort siehst:

- **Pro Query-Run:** Retrieval-Schritte, LLM-Prompt, Antwort, Latenz, Token
- **Pro Benchmark:** Judge-Scores als Feedback auf jeden Run
- **Tags:** `pipeline:basic_rag`, `pipeline:metadata_rag`, `pipeline:graph_rag`

→ https://smith.langchain.com

## Embeddings

Da KISSKI kein Embedding-Modell anbietet, werden Embeddings **lokal** über
`sentence-transformers/paraphrase-multilingual-mpnet-base-v2` erzeugt.
Das Modell (~420 MB) wird beim ersten Start automatisch heruntergeladen.
Es funktioniert gut für Deutsch und Englisch gemischt.

## Projektstruktur

```
rag_comparison/
├── .env.example
├── config.py                      # Alle Keys & Einstellungen
├── main.py                        # Einstiegspunkt & Benchmark
├── requirements.txt
├── docs/                          # Deine Markdown-Dateien
├── pipelines/
│   ├── pipeline_1_basic_rag.py
│   ├── pipeline_2_metadata_rag.py
│   └── pipeline_3_graph_rag.py
├── evaluation/
│   └── evaluator.py               # LLM-Judge + LangSmith-Feedback
└── ingest/
    ├── loader.py                  # Obsidian-Markdown + WikiLink-Parser
    └── llm_factory.py             # KISSKI-Client (gecacht)
```
