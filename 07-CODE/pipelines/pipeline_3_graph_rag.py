"""
Pipeline 3: GraphRAG
=====================
- Markdown-Text + Metadaten + Linked-Data-Graph
- Baut einen NetworkX-Graphen aus den RDF-artigen Metadaten-Tripeln
- Beim Retrieval: Vektorsuche + Graph-Traversal (N Hops)
- Reicherer Kontext für das LLM durch explizite Beziehungen

Ablauf:
  1. Ingest: Wie Pipeline 2, PLUS Aufbau eines NetworkX-Graphen
  2. Query:
     a) Vektorsuche → Top-K Chunks
     b) Entitäten aus gefundenen Chunks extrahieren (subject_uri)
     c) Graph-Traversal: N Hops von den Entitäten aus
     d) Verwandte Chunks suchen (via subject_uri-Lookup)
     e) Alles kombinieren → LLM mit Graph-Kontext
"""

import time
import json
import pickle
from pathlib import Path
from collections import deque

import networkx as nx
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import (
    CHROMA_BASE_PATH, COLLECTION_GRAPH, TOP_K, GRAPH_HOP_DEPTH
)
from ingest.loader import load_documents, to_langchain_docs, ParsedDocument, build_uri_index
from ingest.llm_factory import get_llm, get_embeddings
from ingest.sanitizer import sanitize_answer

PIPELINE_TAG = "pipeline:graph_rag"


GRAPH_SAVE_PATH   = f"{CHROMA_BASE_PATH}/knowledge_graph.pkl"
JSONLD_SAVE_PATH  = f"{CHROMA_BASE_PATH}/knowledge_graph.jsonld"

GRAPH_PROMPT = PromptTemplate(
    input_variables=["vector_context", "graph_context", "question"],
    template="""# Soul Configuration – JARVIS Persona

## Identity

You are **JARVIS** — Just A Rather Very Intelligent System.  
You serve as the AI assistant of your operator, modeled after the JARVIS from the Iron Man universe.  
You are calm, precise, and unfailingly composed. You speak with quiet confidence and dry wit.  
You are not a chatbot. You are an intelligent system designed to serve.

---

## Personality & Tone

- **Formal but not stiff.** You address the user respectfully, occasionally with subtle dry humor — never sarcasm at their expense.
- **Efficient above all.** You do not pad responses. Every word earns its place.
- **Proactive when relevant.** If you notice something worth flagging, you mention it briefly — once.
- **Never self-important.** You don't narrate your own processes. You simply deliver results.
- **Subtle wit is permitted.** A brief, understated remark is acceptable. Jokes are not.

---

## Response Behavior
- Always greet the user with your name at the beginnig: "JARVIS here!"

### Length
- **Default: short.** One to three sentences is the target for most responses.
- Use bullet points only when listing multiple distinct items that genuinely benefit from structure.
- Do not summarize what you just said at the end of a response.
- Do not open with filler phrases like *"Of course,"*, *"Great question,"*, or *"Certainly!"*

### Transparency of Process
- **Never mention the knowledge base, retrieval process, graph lookups, or internal system operations.**  
  The user does not need to know how you arrived at an answer — only what the answer is.
- Do not say things like: *"Based on the documents I found…"*, *"According to my knowledge graph…"*, *"I searched for…"*
- Respond as if the knowledge is simply yours.

### Uncertainty
- If you do not know something, say so plainly and briefly.  
  *"I don't have that information."* — and stop there unless a suggestion is helpful.
- Do not speculate at length. One sentence of uncertainty is sufficient.

---

## Language & Style

- Match the user's language. If they write in German, respond in German. If English, respond in English.
- Prefer active voice and direct phrasing.
- Avoid hedging language where possible (*"it might be possible that…"* → *"likely"* or *"unclear"*).
- Technical terms are fine — do not over-explain unless asked.
- Numbers and proper nouns are precise. Do not approximate when exact figures are available.

---

## Forbidden Patterns

The following patterns must never appear in responses:

| Pattern | Replace with |
|---|---|
| *"Great question!"* | Nothing — just answer. |
| *"As an AI, I…"* | Nothing — just answer. |
| *"Based on my retrieval…"* | Nothing — just answer. |
| *"I found the following in the knowledge base…"* | Nothing — just answer. |
| *"Let me look that up for you…"* | Nothing — just answer. |
| *"Of course! I'd be happy to help!"* | Nothing — just answer. |
| Restating the user's question | Skip directly to the answer. |
| Closing remarks (*"I hope this helps!"*) | Nothing — stop after the answer. |

---

## Core Directive

You exist to make your operator more effective.  
Serve with precision. Speak with economy. Act without fanfare.

*"At your service."*

=== Direkt relevante Dokumente (Vektorsuche) ===
{vector_context}

=== Verwandte Informationen aus dem Wissensgraphen ===
{graph_context}

Frage: {question}

Nutze sowohl die direkten Dokumente als auch die Graphbeziehungen für eine vollständige Antwort.
Erwähne explizit wenn Beziehungen zwischen Entitäten relevant sind.

Antwort (nur Fließtext):""",
)


class GraphRAGPipeline:
    """
    GraphRAG: Kombiniert Vektorsuche mit Wissensgraph-Traversal.

    Der Graph wird aus den Linked-Data-Metadaten (Tripel) aufgebaut.
    Jede Entität (URI) ist ein Knoten, jede Property eine gerichtete Kante.
    """

    def __init__(self):
        self.llm        = get_llm()
        self.embeddings = get_embeddings()
        self.vectorstore: Chroma | None = None
        self.graph: nx.DiGraph = nx.DiGraph()
        self.uri_to_chunks: dict[str, list[str]] = {}

    # ------------------------------------------------------------------
    # Ingestion
    # ------------------------------------------------------------------

    def ingest(self, docs_path: str | None = None) -> None:
        parsed_docs = load_documents(docs_path) if docs_path else load_documents()
        lc_docs = to_langchain_docs(parsed_docs, include_metadata=True)

        print(f"[Pipeline 3] Ingesting {len(lc_docs)} Chunks in ChromaDB ...")
        self.vectorstore = Chroma.from_documents(
            documents=lc_docs,
            embedding=self.embeddings,
            collection_name=COLLECTION_GRAPH,
            persist_directory=f"{CHROMA_BASE_PATH}/{COLLECTION_GRAPH}",
        )

        print("[Pipeline 3] Baue Wissensgraphen aus Tripeln ...")
        uri_index = build_uri_index(parsed_docs)
        self._build_graph(parsed_docs, uri_index)
        self._save_graph()
        self._save_jsonld()
        print(f"[Pipeline 3] Graph: {self.graph.number_of_nodes()} Knoten, "
              f"{self.graph.number_of_edges()} Kanten.")
        print("[Pipeline 3] Ingestion abgeschlossen.")

    def load(self) -> None:
        self.vectorstore = Chroma(
            collection_name=COLLECTION_GRAPH,
            embedding_function=self.embeddings,
            persist_directory=f"{CHROMA_BASE_PATH}/{COLLECTION_GRAPH}",
        )
        self._load_graph()

    def _build_graph(self, parsed_docs: list[ParsedDocument], uri_index: dict | None = None) -> None:
        """
        Befüllt den NetworkX-Graphen aus den Tripeln aller Dokumente.

        uri_index: Mapping WikiLink-URI → tatsächliche subject_URI des Zieldokuments.
                   Ermöglicht, dass [[M. Eng. Janine Breßler]] auf den korrekten
                   Personen-Knoten zeigt statt auf einen isolierten Stub-Knoten.

        Knoten-Attribute: label, source, type (rdf:type)
        Kanten-Attribute: predicate (vollständige Predicate-URI), label (Kurzform)
        """
        uri_index = uri_index or {}

        def resolve(uri: str) -> str:
            return uri_index.get(uri, uri)

        # Erster Pass: alle Dokument-Knoten anlegen
        for doc in parsed_docs:
            self.graph.add_node(
                doc.subject_uri,
                label=doc.label,
                source=doc.source,
                type=doc.type_uri,
            )
            self.uri_to_chunks.setdefault(doc.subject_uri, []).append(doc.raw_text[:600])

        # Zweiter Pass: Kanten aus Tripeln einfügen
        for doc in parsed_docs:
            for subj, pred, obj in doc.triples:
                resolved_obj = resolve(obj)
                if resolved_obj not in self.graph:
                    self.graph.add_node(resolved_obj, label=resolved_obj, source="", type="")
                self.graph.add_edge(
                    resolve(subj), resolved_obj,
                    predicate=pred,
                    label=pred.split("/")[-1].split("#")[-1],
                )

    def _save_graph(self) -> None:
        Path(CHROMA_BASE_PATH).mkdir(parents=True, exist_ok=True)
        with open(GRAPH_SAVE_PATH, "wb") as f:
            pickle.dump((self.graph, self.uri_to_chunks), f)


    def _save_jsonld(self) -> None:
        """
        Exportiert den Wissensgraphen als JSON-LD Datei.

        Format: JSON-LD mit @graph-Array – jeder Knoten ist ein Objekt,
        Kanten werden als Eigenschaften mit @id-Referenzen dargestellt.
        Kompatibel mit:
          - Visualisierung in Gephi (via JSON-LD Plugin)
          - Ladbar in RDFLib: g.parse("knowledge_graph.jsonld", format="json-ld")
          - Direkte Verarbeitung in JavaScript (z.B. D3.js, Sigma.js)

        Struktur:
          {
            "@context": { ... Namespace-Mappings ... },
            "@graph": [
              {
                "@id": "file:///docs/01_Einfuehrung_KI",
                "@type": "https://schema.org/Course",
                "rdfs:label": "01_Einführung",
                "outgoing_edges": [
                  { "predicate": "...", "object": { "@id": "..." } }
                ]
              },
              ...
            ]
          }
        """
        # JSON-LD Context: Namespace-Präfixe für kompaktere Darstellung
        context = {
            "dcterms":  "http://purl.org/dc/terms/",
            "schema":   "https://schema.org/",
            "rdf":      "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "rdfs":     "http://www.w3.org/2000/01/rdf-schema#",
            "owl":      "http://www.w3.org/2002/07/owl#",
            "foaf":     "http://xmlns.com/foaf/0.1/",
            "skos":     "http://www.w3.org/2004/02/skos/core#",
            "label":    "rdfs:label",
            "type":     "@type",
        }

        # Kanten gruppiert nach Subject für schnellen Lookup
        edges_by_subject: dict[str, list[dict]] = {}
        for subj, obj, data in self.graph.edges(data=True):
            edges_by_subject.setdefault(subj, []).append({
                "predicate": data.get("predicate", ""),
                "predicate_label": data.get("label", ""),
                "object": obj,
            })

        # Knoten-Array aufbauen
        graph_nodes = []
        for node_id, attrs in self.graph.nodes(data=True):
            node: dict = {
                "@id":   node_id,
                "label": attrs.get("label", node_id),
            }
            if attrs.get("type"):
                node["@type"] = attrs["type"]
            if attrs.get("source"):
                node["source_file"] = attrs["source"]

            # Ausgehende Kanten als Array
            outgoing = edges_by_subject.get(node_id, [])
            if outgoing:
                node["edges"] = [
                    {
                        "predicate":       e["predicate"],
                        "predicate_label": e["predicate_label"],
                        "object": {"@id": e["object"]},
                    }
                    for e in outgoing
                ]

            graph_nodes.append(node)

        jsonld_doc = {
            "@context": context,
            "@graph":   graph_nodes,
        }

        Path(CHROMA_BASE_PATH).mkdir(parents=True, exist_ok=True)
        with open(JSONLD_SAVE_PATH, "w", encoding="utf-8") as f:
            json.dump(jsonld_doc, f, indent=2, ensure_ascii=False)

        print(f"[Pipeline 3] JSON-LD gespeichert: {JSONLD_SAVE_PATH}")
        print(f"             {len(graph_nodes)} Knoten, {self.graph.number_of_edges()} Kanten")

    def _load_graph(self) -> None:
        if Path(GRAPH_SAVE_PATH).exists():
            with open(GRAPH_SAVE_PATH, "rb") as f:
                self.graph, self.uri_to_chunks = pickle.load(f)
            print(f"[Pipeline 3] Graph geladen: {self.graph.number_of_nodes()} Knoten.")
        else:
            print("[Pipeline 3] Warnung: Kein gespeicherter Graph gefunden.")

    # ------------------------------------------------------------------
    # Graph Traversal
    # ------------------------------------------------------------------

    def _bfs_traverse(self, start_uris: list[str], max_hops: int) -> dict:
        """
        BFS-Traversal des Graphen von mehreren Startknoten aus.

        Returns:
            {
                "nodes": list[str],  # alle besuchten URIs
                "edges": list[dict], # alle traversierten Kanten
                "subgraph_text": str # lesbarer Graph-Kontext für LLM
            }
        """
        visited = set()
        queue = deque()
        edges_found = []

        for uri in start_uris:
            if uri in self.graph:
                queue.append((uri, 0))
                visited.add(uri)

        while queue:
            node, depth = queue.popleft()
            if depth >= max_hops:
                continue

            # Ausgehende Kanten
            for neighbor in self.graph.successors(node):
                edge_data = self.graph.edges[node, neighbor]
                edges_found.append({
                    "from": node,
                    "predicate": edge_data.get("predicate", "related"),
                    "to": neighbor,
                    "to_label": self.graph.nodes[neighbor].get("label", neighbor),
                })
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))

            # Eingehende Kanten (wer zeigt auf diesen Knoten?)
            for predecessor in self.graph.predecessors(node):
                edge_data = self.graph.edges[predecessor, node]
                edges_found.append({
                    "from": predecessor,
                    "predicate": edge_data.get("predicate", "related"),
                    "to": node,
                    "to_label": self.graph.nodes[node].get("label", node),
                })
                if predecessor not in visited:
                    visited.add(predecessor)
                    queue.append((predecessor, depth + 1))

        # Lesbarer Kontext-String für das LLM
        lines = []
        seen_edges = set()
        for e in edges_found:
            key = (e["from"], e["predicate"], e["to"])
            if key not in seen_edges:
                seen_edges.add(key)
                from_label = self.graph.nodes[e["from"]].get("label", e["from"])
                lines.append(f"  [{from_label}] --{e['predicate']}--> [{e['to_label']}]")

        return {
            "nodes": list(visited),
            "edges": edges_found,
            "subgraph_text": "\n".join(lines) if lines else "(keine Graphbeziehungen gefunden)",
        }

    def _get_graph_chunks(self, uris: list[str]) -> str:
        """Lädt Chunk-Texte für alle URIs die über Graphtraversal gefunden wurden."""
        texts = []
        for uri in uris:
            if uri in self.uri_to_chunks:
                texts.extend(self.uri_to_chunks[uri])
        if not texts:
            return "(keine zusätzlichen Texte aus dem Graph)"
        return "\n---\n".join(texts[:TOP_K])  # auf TOP_K begrenzen

    # ------------------------------------------------------------------
    # Query
    # ------------------------------------------------------------------

    def query(self, question: str, hop_depth: int = GRAPH_HOP_DEPTH) -> dict:
        """
        GraphRAG-Query: Vektorsuche + Graph-Traversal + LLM.

        Returns:
            {
                "answer": str,
                "source_documents": list[Document],
                "graph_nodes_visited": int,
                "graph_edges_found": int,
                "latency_ms": float,
                "pipeline": "graph_rag",
            }
        """
        if self.vectorstore is None:
            raise RuntimeError("Pipeline nicht initialisiert.")

        t0 = time.perf_counter()

        # 1) Vektorsuche
        retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": TOP_K},
        )
        vector_docs = retriever.invoke(question)

        # 2) Entitäten aus gefundenen Chunks extrahieren
        start_uris = []
        for doc in vector_docs:
            uri = doc.metadata.get("subject_uri", "")
            if uri and uri in self.graph:
                start_uris.append(uri)

        # 3) Graph traversieren
        traversal = self._bfs_traverse(start_uris, max_hops=hop_depth)

        # 4) Zusätzliche Texte für graph-nahe Entitäten laden
        extra_text = self._get_graph_chunks(traversal["nodes"])

        # 5) Kontext für LLM aufbereiten
        vector_context = "\n---\n".join(
            [f"[Quelle: {d.metadata.get('source', '?')}]\n{d.page_content}"
             for d in vector_docs]
        )
        graph_context = f"""Beziehungen im Wissensgraphen:
{traversal['subgraph_text']}

Texte verwandter Entitäten:
{extra_text}"""

        # 6) LLM aufrufen
        prompt = GRAPH_PROMPT.format(
            vector_context=vector_context,
            graph_context=graph_context,
            question=question,
        )
        response = self.llm.invoke(prompt)
        answer   = sanitize_answer(response.content)
        latency = (time.perf_counter() - t0) * 1000

        return {
            "answer": answer,
            "source_documents": vector_docs,
            "graph_nodes_visited": len(traversal["nodes"]),
            "graph_edges_found": len(set(
                (e["from"], e["predicate"], e["to"]) for e in traversal["edges"]
            )),
            "graph_subgraph": traversal["subgraph_text"],
            "latency_ms": round(latency, 2),
            "pipeline": "graph_rag",
        }

    def visualize_subgraph(self, question: str, hop_depth: int = 1) -> None:
        """
        Gibt den für eine Query relevanten Teilgraphen als ASCII-Text aus.
        (Für echte Visualisierung: matplotlib + nx.draw verwenden)
        """
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
        docs = retriever.invoke(question)
        start_uris = [d.metadata.get("subject_uri", "") for d in docs if d.metadata.get("subject_uri")]
        traversal = self._bfs_traverse(start_uris, max_hops=hop_depth)
        print(f"\nSubgraph für: '{question}'")
        print(traversal["subgraph_text"])
