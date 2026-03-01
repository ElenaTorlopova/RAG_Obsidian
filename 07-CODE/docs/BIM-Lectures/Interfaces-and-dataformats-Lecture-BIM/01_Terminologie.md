---
dcterms:title: 01_Terminologie
dcterms:contributor:
  - "[[Tracy Arndt]]"
dcterms:created: 2026-01-31
dcterms:modified: 2026-01-31
dcterms:subjects:
  - "[[Metadata]]"
  - "[[Data Formats]]"
dcterms:isPartOf:
  - Interfaces_and_Dataformats_Lecture-BIM25
dcterms:references:
schem:language: german
rdf:type: schema:Course
schema:educationalProgramName: "[[Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
# 1. Terminologie
## Daten
Was sind Daten?
Daten sind eine Sammlung roher und ungeordneter Fakten, die für Berechnungen, Schlussfolgerungen oder Planungen verwendet werden können. Ohne angemessene Verarbeitung und Organisation sind sie nutzlos.

Genau hier kommen Metadaten ins Spiel.
## Metadaten
- Daten über Daten -- Informationen über Dinge (Items)
- Beschreibung und Kontext
- Helfen Daten zu organisieren, zu finden und zu verstehen, bspw. durch Format, Herkunft, Erstellungszeitpunkt, Änderungszeitpunkt, etc.
- "Kerngeschäft" der Bibliothek
- Bibliothekarische Metadaten
	- Detaillierte Beschreibung von Dingen, die Nutzenden beim Auffinden dieser Dinge helfen

= strukturierte Daten zur einheitlichen Beschreibungen von Ressourcen jeglicher Art (z.B. Daten, Dokumente, Personen, Gemälde, Orte, Gebäude, Konzepte)
## Unterschiede zwischen Daten und Metadaten

|              | Daten                                     | Metadaten                    |
| ------------ | ----------------------------------------- | ---------------------------- |
| Definition   | Sammlung roher und unorganisierter Fakten | Daten über Daten             |
| Information  | Kann informativ sein oder auch nicht      | immer informativ             |
| Verarbeitung | Kann verarbeitet werden oder auch nicht   | immer verarbeitet            |
| Storage      | Datenbank                                 | Data Dictionary (Wörterbuch) |
## Wichtige Begriffe
### Datenmodelle
- Vorstufe oder Abstraktion eines Datenformats
- Datenmodellierung -> Datenformate
- Von Skizzen auf Papier bis zu komplexen Datenmodellierungssprachen
- Konkrete, abstrakte und universelle Datenmodelle (Übergänge fließend!)

- Konkrete Datenmodelle
	- Grundlage für konkrete Anwendungsformate (z.B. MARC, PICA, MADS)
- Abstrakte Datenmodelle
	- Beziehen sich nicht auf ein konkretes Datenformat (z.B. FRBR, BIBFRAME, Dublin Core)
- Universelle Datenmodelle
	- Für sehr allgemeine Vorstellungen wie "Objekte", "Hierarchien" und "Beziehungen" (z.B. RDF)
### Datenformate
- Strukturierungssprache
- Kodierung
- Anwendungsformate
- Schemasprache
### Strukturierungssprachen
- Daten in kleinere Einheiten unterteilen und miteinander in Beziehung setzen
- Basieren auf Ordnungsprinzipien
- z.B. JSON, XML, CSV

| Ordnungsprinzip     | Strukturierungssprachen      | Beispiele für Anwendungsformate           |
| ------------------- | ---------------------------- | ----------------------------------------- |
| Felder              | INI, MARC, PICA              | MARC 21 für bibliografische Daten, BibTex |
| Hierarchie/Dokument | JSON, XML, SGML, YAML        | TEI                                       |
| Tabelle             | CSV, SQL                     | Excel                                     |
| Graph/Netzwerk      | RDF, GraphML, YAML, SQL      | Ontologien                                |
| Zeichenkette        | Zeichenkette, Unicode, Bytes | ISBD                                      |
### Kodierung
- Drücken Datenformate und -Modelle in Strukturierungssprachen aus
- Bspw.: JSON-LD (JSON-Format = JSON-Syntax)
- Datenformat in ein anderen Datenformat umwandeln nennt man Serialisierung 
### Anwendungsformate
- Erfassung von Daten für konkrete Arten von Inhalten
- Beziehen sich auf konkrete Objekte
	- Bibliografische Datenformate für Metadaten (PICA, MARC, MODS)
	- Formate für Normdaten (MARC, MAB, MADS)
	- Dokumentformate (HTML, Markdown)
### Schemasprachen
- Schemas beschreiben formale Datenformate
	- Avram --> PICA, MARC, MAB
	- Document Type Definition (DTD) --> XML
	- XML Schema (XSD) --> XML
	- JSON Schema --> JSON
	- Shape Expression Language (ShEx) --> RDF
- Automatische Prüfung möglich, ob Daten dem Schema entsprechen
### Typen von Metadaten

| Beschreibende Metadaten      | Zum Finden oder Verstehen der Ressource                                                      |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| **Administrative Metadaten** | Technische Metadaten, Metadata für die Erhaltung, Rechtliche Metadaten                       |
| **Strukturelle**             | Beziehungen zwischen Teilen der Resource und anderen Resourcen                               |
| **Markup Sprachen**          | Integriert Metadaten für andere strukturelle oder semantische Merkmale innerhalb des Inhalts |
### Prinzipien für die Verwendung von Metadaten
- One-to-One: Ein Metadatensatz beschreibt eine Manifestation einer Resource
- Dumb-Down: Granulare Metadatenelemente werden generischen Elementen zugeordnet (alternativeTitle --> title)
- Appropriate Values: Informationen müssen menschen- und maschinenlesbar sein
### Bausteine von Metadaten
#### Metadatenelemente
- Terms and Values
- Metadatenelemente sind:
	- Classes: Definieren die Art der Ressourcen, die beschrieben werden.
	- Properties: Definieren, was für Eigenschaften eine bestimmte Art von Ressourcen hat.
	- Encoding Scheme: Definieren, wie der Eintrag bzw. Wert aussieht der zu einer bestimmten Property gehört.
#### Metadatenschema
- "menschenlesbare" Dokumentation die den Gebrauch eines Metadatenstandards und weitere Metadatenterme innerhalb einer konkreten Anwendung übersichtlich beschreibt.
- Nachvollziehbare und übersichtliche Dokumentation
- Auch "Anwendungsprofil" oder "Metadatenprofil" genannt
- Datenaustausch --> Interoperabilität
#### Metadatenprofil/Dokumentation
- Wozu werden die Metadaten benötigt?
- Was wird beschrieben?
- Welche Eigenschaften sind für die Anwendung relevant?
- Welche Metadatenterme werden verwendet?
- Was für Regeln gelten für die ausgewählte Metadatenterme?
- Was für Encoding Scheme gelten für die einzelnen Terme?
- Wie wird ein Description Set Profile maschinenlesbar?
### Kompetenzzentren für Standards
- Zuständig für die Pflege, die Weiterentwicklung und der Dokumentation von Standards
- Internationale Kompetenzzentren:
	- ISO (International Organisation für Normung)
	- ANSI (American National Standards Institute)
	- NISO (National Information Standards Organization)
	- W3C (World Wide Web Consortium)
- Nationale Kompetenzzentren
	- DIN
	- Standardisierungsausschuss DNB
		- Expertengruppen (Datenformate, Formalerschließung, Normdaten)
		- Normdatenredaktion
	- Überregionale Arbeitsgruppen
	- Regionale Arbeitsgruppen
	- KIM (Kompetenzzentrum Interoperable Metadaten)
