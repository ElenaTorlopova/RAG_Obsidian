---
dcterms:title: Resource Description Framework (RDF)
dcterms:creator: "[[Patryk Gadziomski]]"
dcterms:created: 2025-11-28
dcterms:modified: 2025-11-28
schema:about: Resource Description Framework Standards
dcterms:subjects:
  - Schema
  - Dublin Core
  - Linked Data
  - Friend of a Friend
  - Simple Knowledge Organization System
  - Web Ontology Language
  - Resource Description Framework
  - Provenance Ontology
  - Time Ontology
  - Geografische Daten
  - Vocabulary of Interlinked Datasets
tags:
  - rdf
  - schema
  - dublin_core
  - linked_data
  - friend_of_a_friend
  - simple_knowledge_organization_system
  - web_ontology_language
  - resource_description_framework
  - provenance_ontology
  - time_ontology
  - geografische_daten
  - vocabulary_of_Interlinked_datasets
dcterms:isPartOf: vault:RAG_Obsidian
dcterms:references:
  - https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
  - https://schema.org/
  - https://de.wikipedia.org/wiki/FOAF
  - https://www.w3.org/TR/skos-reference/
  - https://www.w3.org/OWL/
  - https://www.w3.org/TR/1999/REC-rdf-syntax-19990222/
  - https://www.w3.org/TR/rdf-schema/
  - https://www.w3.org/ns/prov
  - https://www.w3.org/TR/owl-time/
  - https://www.w3.org/2003/01/geo/
  - https://www.w3.org/TR/void/
content: beruflich
foaf:primaryTopic: Resource Description Framework
geo:lat: "52.5200"
geo:long: "13.4050"
geo:location: Berlin, Germany
---
## 1. **`schema:` → Schema.org**
**URI**: `http://schema.org/`  
**Zweck**: Beschreibt Webinhalte (Artikel, Personen, Organisationen, Ereignisse, Produkte…)  
**Ideal für**: Titel, Autor, Datum, Typ, Thema
### Beispiele:
```yaml
schema:author: "Patryk Gadziomski"
schema:datePublished: "2025-11-20"
schema:about: "Retrieval Augmented Generation"
schema:articleBody: "Der Text der Notiz..."
schema:isPartOf: "vault:Beruflich"
```
## 2. **`dcterms:` → Dublin Core Terms**
**URI**: `http://purl.org/dc/terms/`  
**Zweck**: Metadaten für Ressourcen (Titel, Autor, Thema, Beziehungen, Datum…)  
**Ideal für**: Allgemeine Metadaten, Verknüpfungen, Kategorien
### Beispiele:
```yaml
dcterms:title: "RAG in der Praxis"
dcterms:creator: "Patryk Gadziomski"
dcterms:subject: ["AI", "LLM"]
dcterms:isPartOf: "vault:Beruflich"
dcterms:references: "vault:LLM_Grundlagen"
dcterms:created: "2025-11-20"
```
## 3. **`foaf:` → Friend of a Friend**
**URI**: `http://xmlns.com/foaf/0.1/`  
**Zweck**: Beschreibt Personen, Organisationen und ihre Beziehungen  
**Ideal für**: Autoren, Hauptthemen, Kontakte
### Beispiele:
```yaml
foaf:Person: "Patryk Gadziomski"
foaf:name: "Patryk Gadziomski"
foaf:primaryTopic: "RAG"
foaf:knows: "vault:Martin_Schmidt"
```
## 4. **`skos:` → Simple Knowledge Organization System**
**URI**: `http://www.w3.org/2004/02/skos/core#`  
**Zweck**: Beschreibt Begriffe, Kategorien, Hierarchien, Thesauri  
**Ideal für**: Tags, Kategorien, Verwandte Begriffe, Hierarchien
### Beispiele:
```yaml
skos:Concept: "RAG"
skos:broader: "vault:LLM"
skos:narrower: "vault:VectorDB"
skos:related: "vault:PromptEngineering"
skos:prefLabel: "Retrieval Augmented Generation"
```
## 5. **`owl:` → Web Ontology Language**
**URI**: `http://www.w3.org/2002/07/owl#`  
**Zweck**: Beschreibt logische Beziehungen und Klassen (für fortgeschrittene Ontologien)  
**Ideal für**: Wenn du später logische Schlüsse ziehen willst (z. B. „Alle RAG-Notizen sind auch LLM-Notizen“)
### Beispiele:
```yaml
owl:equivalentClass: "vault:RAG"
owl:subClassOf: "vault:KI_Methode"
owl:sameAs: "https://www.wikidata.org/entity/Q123456"
```
## 6. **`rdf:` → RDF Schema**
 **URI**: `http://www.w3.org/1999/02/22-rdf-syntax-ns#`  
 **Zweck**: Grundlegendes RDF-Vokabular (Typ, Eigenschaft, etc.)  
 **Ideal für**: Wenn du explizit den Typ einer Ressource angeben willst
### Beispiele:
```yaml
rdf:type: "schema:Article"
rdf:type: "skos:Concept"
```
## 7. **`rdfs:` → RDF Schema**
**URI**: `http://www.w3.org/2000/01/rdf-schema#`  
**Zweck**: Erweiterung von `rdf:` mit Klassen und Eigenschaften  
**Ideal für**: Wenn du Klassen und Eigenschaften definieren willst
### Beispiele:
```yaml
rdfs:label: "RAG in der Praxis"
rdfs:comment: "Eine Einführung in RAG mit Obsidian"
rdfs:subClassOf: "schema:Article"
```
## 8. **`prov:` → Provenance Ontology**
**URI**: `http://www.w3.org/ns/prov#`  
**Zweck**: Beschreibt Herkunft, Veränderung und Verantwortlichkeit  
**Ideal für**: Wer hat was wann geändert? — für Audit-Logs oder Versionskontrolle
### Beispiele:
```yaml
prov:wasGeneratedBy: "Patryk Gadziomski"
prov:generatedAtTime: "2025-11-20T10:00:00Z"
prov:wasDerivedFrom: "vault:LLM_Grundlagen"
```
## 9. **`time:` → Time Ontology**
**URI**: `http://www.w3.org/2006/time#`  
**Zweck**: Beschreibt Zeitpunkte, Zeiträume, Dauern  
**Ideal für**: Wenn du Zeitverläufe oder Zeiträume in deinen Notizen modellieren willst
### Beispiele:
```yaml
time:hasBeginning: "2025-11-20T09:00:00Z"
time:hasEnd: "2025-11-20T17:00:00Z"
time:duration: "PT8H"  # 8 Stunden
```
## 10. **`geo:` → GeoSPARQL / Geografische Daten**
**URI**: `http://www.w3.org/2003/01/geo/wgs84_pos#`  
**Zweck**: Beschreibt geografische Positionen  
**Ideal für**: Wenn du Orte in deinen Notizen verknüpfen willst (z. B. „Meeting in Berlin“)
### Beispiele:
```yaml
geo:lat: "52.5200"
geo:long: "13.4050"
geo:location: "Berlin, Germany"
```
## 11. **`void:` → Vocabulary of Interlinked Datasets**
**URI**: `http://rdfs.org/ns/void#`  
**Zweck**: Beschreibt, wie Datensätze miteinander verknüpft sind  
**Ideal für**: Wenn du später mehrere Vaults oder externe Datenquellen verknüpfen willst
### Beispiele:
```yaml
void:dataset: "vault:Beruflich"
void:linkPredicate: "dcterms:references"
void:triples: "1200"
```
