---
dcterms:title: 04_ISO_OSI_Referenzmodell
dcterms:contributor:
  - "[[Prof. Birgit Wilkes]]"
dcterms:created: 2026-02-01
dcterms:modified: 2026-02-01
dcterms:subjects:
  - "[[Informatics]]"
  - "[[Internet]]"
dcterms:isPartOf:
  - "[[Spectrum_Informatics-Lecture-BIM25]]"
dcterms:references:
schem:language: german
rdf:type: schema:Organization
schema:educationalProgramName: "[[Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
## Referenzmodelle
- ISO/OSI
	- ISO = International Organisation for Standardization
	- OSI = Open System Interconnection
- TCP/IP
	- TCP = Transmission Control Protocol
	- IP = Internet Protocol
	- TCP/IP is Protokollgrundlage des Internets
## ISO/OSI Referenzmodell
Das ISO/OSI Schichtenmodell besteht aus 7 Schichten und gilt als Referenz für die Kommunikationstechnik:
### Bitübertragung/Physical Layer
- Die unterste Schicht des ISO Referenzmodells
- Sie definiert die mechanischen, elektronischen und funktionalen Charakteristiken einer realen Leitung
- die Übertragung erfolgt transparent, d.h. jedes in die Leitung hineineingegebene Bit kommt auch wieder heraus. Bitsequenzen werden nicht verschluckt, z.B. weil die als Befehl interpretiert werden.
### Sicherung/Data Link Layer
- Die Ebene verantwortet das Verbindungsmanagement
- Die hat die Aufgabe, Übertragungsfehler, die auf der Bitübertragungsschicht möglicherwiese entstanden sind, zu entdecken und zu korrigieren
- Fehler können durch Neuübertragung behoben werden
- Hier kommen bestätigungs- und Flusskontrollmechanismen zum Einsatz
### Vermittlung/Network Layer
- Ihre Aufgabe ist die Weiterleitung einer Nachricht durch ein Netzwerk
- Zentrale Aufgabe ist die Wegwahl (Routing)
- Absicherung von Verbindungsqualität (QoS: Quality of Service)
- Adressierung von Endsystemen
- Abrechnung von Verbindungskosten
### Transport/Transport Layer
- Ab dieser Ebene wird eine End-zu-End Kommunikation zwischen Rechnern betrachtet, d.h. es ist die erste transparente Schicht (Daten werden von den Transitsystemen nicht ausgewertet)
- Letzte transportorientierte Schicht
- Überwachung der Verbindung zwischen den Endrechnern
- Wahl einer möglichst kostengünstigen und effizienten Verbindung
- Gleicht QoS-Anforderungen zwischen den Anwendungen und den QoS-Parametern der unteren Schichten (Transitsysteme) aus
### Sitzung/Session Layer
- Sie ist die erste Anwendungsorientierte Schicht
- Strukturierung durch Setzen von Synchronisationspunkten für einen Neustart im Fehlerfall
### Darstellung/Presentation Layer
- Verantwortet die Passfähigkeit von Syntax und Semantik der Anwendungsinformationen und unterschiedlichen Systemen
- Transformiert die anwendungsorientierten Daten in Standardformate. Anwendungen müssen sich verstehen.
- Verschlüsselung und Datenkompression sind ebenfalls Dienste des Presentation Layer
### Anwendung/Application Layer
- Sie besitzt als oberste Schicht keine Dienstzugangspunkte
- Sie liefert Kommunikationsdienste für Anwendungsinstanzen innerhalb der gleichen Schicht (Anwendungsassoziationen)
- Enthält von Anwendungen genutzte Protokolle. Sie ist die einzige Möglichkeit für Anwendungen, auf das Netzwerk zuzugreifen
