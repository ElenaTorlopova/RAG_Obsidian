---
dcterms:title: 05_Metadatenorganisation
dcterms:contributor:
  - "[[Tracy Arndt]]"
dcterms:created: 2026-01-31
dcterms:modified: 2026-01-31
dcterms:subjects:
  - "[[Data Formats]]"
  - "[[Metadata]]"
  - "[[BibFrame]]"
dcterms:isPartOf:
  - Interfaces_and_Dataformats_Lecture-BIM25
dcterms:references:
schem:language: german
rdf:type: schema:Course
schema:educationalProgramName: "[[Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
# 5. Metadatenorganisation
## Anforderungen an die Organisation von Metadaten
Ausgleich zwischen den Anforderungen für das Information Retrieval und der Realisierung bibliothekarischer Workflows.
## Anforderungen an die Metadatenumgebung (Datenflow)
- Wie kommen Metadaten in das System?
- Welches Datenhandling fordern die Geschäftsgänge?
- Was wollen Bibliotheken von Metadaten im Allgemeinen?
- Nachnutzung von Metadaten
- Erzeugung von Metadaten
- Anreichern von Metadaten
- Verknüpfung von Metadaten
- Transfer von Metadaten
## Exkurs: ETL-Prozess
Extract - Transform - Load
- Daten aus mehreren ggf. unterschiedlich strukturierten Datenquellen in eine Zieldatenbank vereinigen
- Begriff aus dem Data Warehouse-Bereich
- "Datenintegration"
## Standards für die Organisation von Metadaten
- Metadatenterme (Auswahl, Anordnung, Inhalt)
	- ISBD, FRBR --> LRM
- Values (Literale, Nicht-literale)
	- Regelwerke, RDA

--> Bibliografisches Metadatenschema
### Standardisierung der Organisation von Metadaten
International Standard Bibliographic Description (ISBD)
## Austauschformate für ISBD-organisierte Metadaten
#### Machine-Readable Cataloging (MARC)
```MARC
0XX – Kontrollfelder/codierte Angaben
1XX – Haupteintrag
2XX – Titel und verbundene Angaben
3XX – Physische Beschreibung
4XX – Gesamttitelangabe
5XX – Fussnoten
6XX – Sacherschliessung
7XX – Nebeneintrag
8XX – Nebeneintrag Gesamttitel
9XX – reserviert fü r lokale Einträge
```
#### MAB2 (abgeschlossen 2006)
```MAB2
0XX - codierte Angaben 
1XX - Verfasserangabe 
2XX - Körperschaft 
3XX - Titelangaben 
4XX - Ausgabevermerk 
5XX - Fußnoten 
6XX - Ausgabevermerk 
7XX - Sacherschließung 
8XX - Nebeneintragungen 
9XX - RSWK-Schlagwörter
```
## Organisationsmodelle
### FRBR (Functional Requirements for Bibliographic Records)
Group 1 Entities
#### FRBR-LRM (Library Reference Model)
#### Austauschformat für FRBR-organisierte Metadaten
##### Bibfame (Bibliographic Framework Initiative)
- MARC21 genügt nicht mehr den Anforderungen einer immer stärker werdenden digitalen Vernetzung der Informationswelt
- Möglichkeit von Linked Data und Semantic Web nutzen
- DNB gehört zur "Early Implementers Group"
- Bibframe Vocabulary Navigator http://bibfra.me/
- https://bibframe.org/
##### Systemunabhängige Abbildung (Bsp. Bibframe)
```BIBFRAME
<rdfs:label>&#x98;Die&#x9c; 13 1/2 Leben des Kä pt'n Blaubä r</rdfs:label>
	<bf:title>
		<bf:Title>
			<bflc:title40MatchKey>&#x98;Die&#x9c; 13 1/2 Leben des Kä pt'n Blaubä r</bflc:title40MatchKey>
			<bflc:title40MarcKey>24010$0(DE-588)7733327-5$0https://d-nb.info/gnd/7733327-5 $0(DE-101)1009860739$a&#x98;Die&#x9c; 
			13 1/2 Leben des Kä pt'n Blaubä r$2gnd</bflc:title40MarcKey
			<rdfs:label>&#x98;Die&#x9c; 13 1/2 Leben des Kä pt'n Blaubä r</rdfs:label>
			<bflc:titleSortKey>&#x98;Die&#x9c; 13 1/2 Leben des Kä pt'n Blaubä r</bflc:titleSortKey>
			<bf:mainTitle>&#x98;Die&#x9c; 13 1/2 Leben des Kä pt'n Blaubä r</bf:mainTitle>
		</bf:Title>
	</bf:title>
	<bf:identifiedBy>
		<bf:Identifier>
			<rdf:value>7733327-5</rdf:value>
			<bf:source>
				<bf:Source>
					<rdfs:label>DE-588</rdfs:label>
				</bf:Source>
			</bf:source>
		</bf:Identifier>
	</bf:identifiedBy>
```
## Anforderungen an den Metadatenumgang
Anforderungen an Metadaten (Nachnutzung, erzeugen, Anreichern, Verknüpfen, Transfer)
+
Diversität der Metadatenmodellierung (ISBD, FRBR, LRM, RDA, RAK-WB, BIBFRAME, MARC, MAB, DC, PICA, ...)

--> Ziel: Möglichst geringer Informationsverlust und Aufwand
