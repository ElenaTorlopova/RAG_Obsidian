---
rdf:type: schema:Course
dcterms:title: 07_Adressierung_im_Internet
dcterms:contributor:
  - "[[Prof. Birgit Wilkes]]"
dcterms:created: 2026-02-01
dcterms:modified: 2026-02-01
dcterms:isPartOf:
  - "[[Spectrum_Informatics-Lecture-BIM25]]"
dcterms:references:
schem:language: german
schema:educationalProgramName: "[[M.Sc. Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
## Adressierung im Internet (IPv4)
- Die IP-Adresse ist eine 32 Bit-Adresse in Dezimaldarstellung als 4 Byte
	- A.B.C.D
	  z.B. 137.226.76.1
- Internetprovider teilt Adressblöcke zu je nach Zahl der Knoten
- Kennzeichnung und Verwaltung durch NICs (Network Information Center)

Wir unterscheiden 3 Klassen von Netzen:
- Class-A Adresse: A.x.x.x wobei 0<=A<127 A<>10
- Class-B Adresse: B1.B2.x.x wobei 127<B1<192, 0<=B2<256
- Class-C Adresse: C1.C2.C3.x wobei 191<C1<224, 0<=C2, C3<256
## Sonderadressen
- 127.x.x.x ist reserviert für Loopback-Funktionen aller Rechner
- 127.0.0.1 = localhost (eigener Rechner)
- Der Wert 255 in einem Oktett adressiert aller Rechner dieses Oktetts (255.255.255.255 adressiert alle Rechner im Internet)
- Eine Netzwerkadresse zeichnet sich dadurch aus, dass alle Bit der Host-ID auf 0 gesetzt sind
## Subnetze
- Besonders bei den Klassen A und B ist ein sehr großer Bereich für die Vergabe von Host IDs reserviert
- Daher macht es Sinn, ein Netzwerk wird in Subnetze als logische Teile zu gliedern, um eine strukturelle Ordnung abzubilden und die Netzlast zu verteilen
	- Nach örtlichen Gegebenheiten (Häuser, Stockwerke, etc.)
	- Nach organisatorischen Einheiten (Abteilungen, Profit Center, etc.)
- Die Anzahl der Rechner und das Datenaufkommen in den Subnetzen muss berücksichtigt werden, um die Last pro Segment nicht zu hoch werden zu lassen
- Netze der Klassen A, B und C können jeweils in weitere Subnetze aufgeteilt werden
- Dazu wird eine bestimme Anzahl von Bits der Host-ID für die Adressierung von Subnetzen verwendet
	- Beispiel: In einem Class-B Netz stehen 16 Bit für die Host-Adressierung zur Verfügung. Diese können z.B. in 8 Bit für die Subnetz-Adresse und 8 Bit in die Host-IDs in einem Subnetz aufgeteilt werden
	- Daraus ergeben sich 256 Subnetze mit jeweils 254 Hosts
- Netze können auch innerhalb der Adressoktette aufgeteilt werden
## Netzmaskierung
- Eine 32-Bit Subnetz-Maske bestimmt die Anzahl der für die Subnetz-Adressierung reservierten Bits
- Alle mit 1 belegten Bitpositionen der Subnetz-Maske werden im Vergleich mit der Netz-ID zur Subnetz-Adresse gerechnet
- Die restlichen in der Subnetz-Maske mit 0 belegten Bits bleiben in dem Subnetz für die Adressierung der Hosts
- Beispiel einer Aufteilung eines Class-B Netzes in 256 Subnetze mit je 254 Hosts:
	- Netzmaske:
		- Binär: 11111111.11111111.11111111.00000000
		- Dezimal: 255.255.255.0
## Multicasting
- Multicasting bezeichnet das gleichzeitige Versenden von IP-Paketen an eine Gruppe von Zielrechnern
- Die Verwaltung der zur Multicasting-Gruppe gehörenden Netzwerkknoten obliegt in TCP/IP dem Internet Group Management Protocol (IGMP)
- Für Multicasting-Gruppen steht ein eigener Adressraum, die sogenannte Class-D Adresse zur Verfügung
	- Reserviert sind dafür alle Adressen, die mit den Bots 1110 beginnen
	- Anders ausgedrückt: Alle Adressen der Form A.B.C.D, wobei 224<=A<240 und B, C, D sind beliebig
## Adressierung über Namen
- Anstelle der IP-Adressen können die Domain-Namen verwendet werden
- Die Namenräume werden von den nationalen NICs (Network Information Center) verwaltet und zugeteilt
- Die Domain-Namen richten sich nach folgenden Konventionen:
	- computer.bereich.institution.land (.edu, .com, .net, .org)
- Beispiel: tm09.tm.th-wildau.de
- Die Auflösung der Domain-Namen erfolgt über einen DNS-Server (Domain Name Service), der die zu einem Namen zugehörige IP-Adresse zurückliefert
## IP-Datagramm
- Die Dateneinheiten des Internet-Protokolls bezeichnet man als IP-Datagramme
- Sie werden in die Dateneinheiten der unterliegenden Netzwerkschichten (z.B. Ethernet-Frames) verpackt und übertragen
- Ein IP-Datagramm Header der IPv4 hat ohne Optionen die Länge von 20 Byte und umfasst 12 Steuerfelder
- Version: Gibt die Versionsnummer des verwendeten IP-Standards an
- IHL (Internet Header Length): Enthält die Anzahl der Doppelwerte, aus denen sich der IP-Header inklusive Optionen zusammensetzt (normal 5)
- Type of Service: Spezifiziert Qualitätsanforderungen (z.B. maximaler Durchsatz, minimale Verzögerung), Umsetzung erfolgte nicht im gesamten Internet
- Total Length: Absolute Länge des IP-Datagramms
- Identification, Flags, Fragment Offset: Die drei Felder steuern die Fragmentierung von IP-Datagramms
	- Identification dient der Zuordnung der Fragmente zum ursprünglichen Datagramms
	- Die Flags kontrollieren die Fragmentierung
	- Fragment Offsets enthält den Offset-Wert des betreffenden Fragments vom Beginn des Datagramms gerechnet
- Time to Live: Anzahl der Router, die das Datagramm passieren darf
- Protocol: Das Steuerfeld gibt an, welches Protokoll das jeweilige IP-Datagramm benutzt
- Header Checksum: Prüfsumme über den Header des IP-Datagramms
- Source Address, Destination Address: Die Felder enthalten die 32 Bit Internet-Adressen des senden und des Zielrechners
- Options: Ein optionales Feld, dessen variable Länge immer ein Vielfaches von 32 sein muss. Passt die Länge der Option nicht, wird dies durch Padding ausgeglichen, das Stopfen der restlichen Stellen durch 0-Bits
