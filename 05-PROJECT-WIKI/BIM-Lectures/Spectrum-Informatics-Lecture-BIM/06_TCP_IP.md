---
dcterms:title: 06_TCP_IP
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
rdf:type: schema:Course
schema:educationalProgramName: "[[Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
## TCP/IP Schichtenarchitektur
TCP/IP bildet die 7 OSI Schichten auf 4 Schichten ab:
- Nicht an Hersteller gebunden
- Sowohl auf PCs als auch auf Hochleistungsrechnern implementiert
- Kann für LAN und WLANs verwendet werden
- Wird branchenunabhängig eingesetzt
- Durch den Boom des Internets am weitesten verbreiteter Protokoll-Stack
## TCP/IP Protokolle
- ARP (Address Resolution Protocol)
	- Abbildung der logischen Adressen der Netzwerkschicht auf die physikalischen Adressen der Übertragungsschicht
- RARP (Reverse Address Resolution Protocol)
- ICMP (Internet Control Message Protocol)
	- Austausch von Fehlermeldungen und anderen Steuerinformationen
- IGMP (Internet Group Management Protocol)
	- Unterstützt von Multicast (Senden von Dateien an mehrere Netzwerkknoten)
- IP (Internet Protocol)
	- Hauptprotokoll der Netzwerkschicht
	- Paketorientierte Übertragung und Routing
- TCP (Transmission Control Protocol)
	- Stellt Anwendungen byteorientiert, vollduplexfähige Datenverbindung zur Verfügung (bestätigt)
- UDP (User Datagram Protocol)
	- Ordnet Dateneinheiten den jeweiligen Anwendungen zu, ohne Garantie für konkrete Übertragung (unbestätigt)
- FTP (File Transfer Protocol)
	- Übertragung von Dateien zwischen Rechnersystemen
- TFTP (Trivial File Transfer Protocol)
	- Einfachere variante des FTP
- HTTP (Hypertext Transfer Protocol)
	- Anwendungsprotokoll für den Datenaustausch im World Wide Web
- etc.
## TCP/IP Schichten und Protokolle

## Einkapselung
- Sendet einer Anwendung Daten über TCP/IP, so durchlaufen die Datenpunkte alle Schichten der Internet-Schichtenarchitektur auf Sender- und Empfängerseite
- Beim Sender fügen die Protokollinstanzen jeder Schicht eine Art Umschlag genannt PDU (Protocol Data Unit) mit einem Header hinzu. Jede neue PDU-Kapsel legt sich um die vorherige.
- Auf der Empfängerseite werden die Umschläge von der zugehörigen Schicht wieder entfernt und die protokollspezifischen Headerinformationen ausgewertet
- Die Informationen aus den PDUs teilen den Protokollen der einzelnen Schichten mit, was Sie mit den Daten machen sollten
## Paket mit TCP/IP Protokoll
## MAC-Adresse
- Die MAC-Adresse ist eine feste Hardwareadresse, die jeder Netzwerkkarte in einer Netzwerkkomponente zugewiesen ist
- Jede Komponente erhält eine einmalige 48-Bit Kennung, die MAC-Adresse
- Die erste 24 Bit der Adresse sind die OUI (Organizationally Unique Identifier)
- Die IEEE weist jedem Hersteller von Netzwerkkomponenten eine Anzahl von einmaligen OUIs zu
- Die zweiten 24 Bit werden von der jeweiligen Firma vergeben