---
dcterms:title: 03_Interoperabilität
dcterms:contributor:
  - "[[Tracy Arndt]]"
dcterms:created: 2026-01-31
dcterms:modified: 2026-01-31
dcterms:subjects:
  - "[[Data Formats]]"
  - "[[Metadata]]"
dcterms:isPartOf:
  - Interfaces_and_Dataformats_Lecture-BIM25
dcterms:references:
schem:language: german
rdf:type: schema:Course
schema:educationalProgramName: "[[Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
# 3. Interoperabilität
##### Interoperabilität
"Interoperabilität ist die Fähigkeit, Daten zwischen verschiedenen Systemen ohne all zu großen Informationsverlust auszutauschen."
 
(Kleines Handbuch Metadaten, KIM)
- strukturell
- syntaktisch
- semantisch
## Einfach oder?!
Vollständige Interoperabilität kaum erreichbar, daher:
### A: Zentralisierung statt Interoperabilität
**Beispiel**: Gemeinsamer Verbundkatalog
**Vorteil**: Klare Verantwortlichkeit
**Probleme**: Abgeschlossene Datensilos, interne Inkonsistenten
### B: Gemeinsame Standards
**Beispiel**: Aggregator-Formate (Schema.org, DataCite XML, ...)
**Vorteil**: Offen für beliebig viele Akteure
**Probleme**: Verschiedene Standards für verschiedene Anwendungen
### C: Integration durch Mapping/Konvertierung
**Beispiel**: Konvertierung beim Import/Export von Formaten, Vokabular-Mapping im Projekt coli-conc
**Vorteil**: Sehr flexibel
**Problem**: Aufwändig und fehleranfällig
## Beispiel: Klemmbausteine
**A)** Zentralisierung: Wir kaufen einfach alles nur von LEGO!
**B)** Standards: LEGO, Q-Bricks, BlueBrixx, ... passt doch zusammen!
**C)** Mapping: Adapter wie das Free Universal Construction Kit

Meist wackelt es trotzdem ein bisschen...
### Welche Strategie wird in der Praxis angewandt?
**A)** Zentralisierung: Keine Gesamtlösung, aber hilfreich zur Abgrenzung von Systemen
**B)** Standards: Grundlage der gesamten Infrastruktur
**C)** Mapping: Findet als Konvertierung an vielen Stellen statt
### Metadaten-Interoperabilität in der Theorie
1. Interoperabilität ist die Fähigkeit unterschiedlicher Systeme, reibungslos Daten auszutauschen
2. Informationssysteme sind qausi-geschlossene Einheiten, die standardisierte Daten austauscht
3. Datenkonvertierung zwischen unterschiedlichen Standards
### Metadaten-Interoperabilität in der Praxis
Probleme:
- Es gibt sehr viele Standards und Informationssysteme
- Standards sind meist unvollständig
- Mapping/Konvertierungen sind meist unvollständig
Lösung:
- Kenntnis von Metadaten-Standards und Mapping-Verfahren
- Interoperabilität muss immer wieder neu hergestellt werden
## Metadatenstandards
- Vereinbarungen wie Daten aussehen sollen
- Explizite Vereinbarungen wie Daten aussehen sollen
	- Publiziert und verständlich, mit Beispielen
	- Versioniert (Was ist seit wann wie geregelt?)
	- Maschinenlesbar
- Aufbauend auf bereits etablierten Standards
	- Anwendungsbezogen
	- Möglichst in verschiedene Systeme umgesetzt
- Überprüfbar
	- Validierung von Daten (Fehler erkennen)
	- Konsequente (mit Fehlern umgehen)
	- Fehler nicht gleich Fehler
### Ebenen der Datenmodellierung
- Hinter Daten steht immer (implizit oder explizit) mindestens ein Modell
- Interoperabilität erfordert vor allem gleiche Modelle
- Datenformate bewegen sich zwischen Modell und Implementierung
- Auf jeder Ebene weitere Unterteilung möglich
### Beispiel: Ebenen von Metadaten-Standards in der Praxis
- Lokale Anwendungspraxis einer Bibliothek
- PICA-K10plus-Format
- PICA-Format
- PICA/XML
- XML
- Unicode
- Bytes
### Wie sind Standards festgelegt?
- Spezifikation (so soll es sein)
- Implementierung (so ist es umgesetzt)
- Datenpraxis (so wird es interpretiert)

Offizielle Standards, De-Facto Standards, Implizite Standards, Scheinbare Standards, Anwendungsprofile, ...
### Wie sind Standards zugänglich?
- Implementierung und Datenpraxis: konkret ansehen
- Spezifikationen:
	- Semi-formale Beschreibung: verstehbar
	- Formate Schema: maschinenlesbar und überprüfbar
### Beispiel: Spezifikation einer Jahreszahl
Implementierung: `year = int(input.readline())`
Datenpraxis: `2019, 1998, 722, 23...`
Semi-Formal: `Jahreszahlen werden durch eine bis vier Ziffern ohne führende Nullen ausgedrückt`
Formal: `YEAR := [1-9][0-9]*`

Überraschung: Keines dieser Beispiele ist 100% deckungsgleich!
### Arten von Daten-Standards und -formaten
- Strukturierungssprachen: CSV, JSON, RDF, ...
- Schemasprachen: Reguläre Ausdrücke, XSD, JSON-Schema, ...
- Abfragesprachen: SQL, XPath, XQuery, CSS Selector, ...
- Datenmodelle: BIBFRAME, CIDOC-CRM, Dublin Core, ...
### Interoperabilität hängt von dieser Datenebene ab
Was muss interoperabel sein?
- Datenmodell: Semantik (theoretisch interoperabel)
- Strukturierungssprache: Werkzeuge (praktisch umsetzbar)

Wie wird Interoperabilität umgesetzt?
- Schemas helfen passende Elemente zu finden (z.B. Feld für Jahreszahl)
- Abfragesprache helfen auf passende Elemente zu verweisen
## Beispiel: Ein Datensatz
### Ein Datensatz ohne Datenformat:

| Name               | Lebensdaten |
| ------------------ | ----------- |
| Douglas Noel Adams | 1952-2001   |
### Ein Datensatz (CSV):
```csv
name,dates 
Douglas Noel Adams,1952-2001
```
### Ein Datensatz (YAML):
```yaml
name: Douglas Noel Adams 
dates: 1952-2001
```
### Ein Datensatz (JSON):
```json
{ 
	"name": "Douglas Noel Adams", 
	"dates": "1952-2001"
}
```
### Ein Datensatz (XML):
```xml
<name>Douglas Noel Adams</name>
<dates>1952-2001</dates>
```
## Mapping/Konvertierung
### Arten von Mapping/Konvertierungen
Konvertierung zwischen Formaten
- DD.MM.YYY <--> YYY-MM-DD
- "Nachname, Vorname" --> "Vorname Nachname"
- ...

Mapping zwischen Vokabularen
- GND-ID <--> ORCID
- RVK <--> BK
- ...
### Konvertierung zwischen Formaten
- Muss meist programmiert werden
- Je nach Überschneidung des Datenmodells mehr oder weniger vollständig
- Mit jeder Konvertierung können Inhalte verloren gehen
### Konvertierung zwischen Vokabular
- Mapping von Identifiern statt Benennung
- Einfach wenn 1-zu-1 Zuordnung möglich (z.B. Personen)
- Bei Sachgebiet schwieriger (Mapping von Datenmodellen)
### Mapping
##### mapping
Bestandteile eines Metadatenstandards (Metadatenterme, Metadatenelemente, Regelungen) mit den Bestandteilen eines anderen Metadatenstandards in Beziehung setzen.

Beispiele:
```
Systemumgebung (MARC21)    -- Informationsumgebung (MARCXML) 
Austauschformat (MAB2)     -- Austauschformat (MARC21) 
Austauschformat (MARC21)   -- Internformat (PICA) 
Indexformat (PICA+)        -- Katalogisierungsformat (PICA3) 
Austauschformat (MARC21)   -- Organisationsmodell (BIBFRAME) 
Organisationsmodell (ISBD) -- Organisationsmodell (FRBR)
```
### Herausforderungen
- Unterschiedliche Komplexität
- Unterschiedliche Eigenschaften der Felder
- Verwendung unterschiedlicher encoding scheme

= Faktoren, die den Grad der semantischen und strukturellen Übereinstimmungen der Elemente des Quell- zu dem Zielformat beeinflussen.