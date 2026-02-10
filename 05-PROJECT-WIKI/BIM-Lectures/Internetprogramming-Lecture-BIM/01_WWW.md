---
dcterms:title: 01_WWW
dcterms:contributor:
  - "[[Marcel-Dominique Block]]"
dcterms:created: 2026-02-01
dcterms:modified: 2026-02-01
dcterms:subjects:
  - "[[Web Development]]"
  - "[[WWW]]"
dcterms:isPartOf:
  - "[[Internetprogramming-Lecture-BIM25]]"
dcterms:references:
schem:language: german
rdf:type: schema:Course
schema:educationalProgramName: "[[Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
# 1. WWW
## 1.1. Das Internet
- Ein weltweiter Verbund von Rechnern und Rechnernetzen
- Bezeichnet die physikalische Betrachtung des globalen Netzwerkes
- Technische Weiterentwicklung wird durch die IETF (Internet Engineering Task Force) vorangetrieben
## 1.2. Kommunikation
- Ein Netzwerk liegt dann vor wenn mindestens zwei elektronische Geräte miteinander kommuniziere können
- Kommunikation erfolgt über standardisierte Protokolle --> Internetprotokollfamilie

| OSI-Schicht        | TCP/IP-Schicht | Beispiel                                     |
| ------------------ | -------------- | -------------------------------------------- |
| Anwendungen (7)    | Anwendung      | HTTP, FTP, SMTP, POP, Teinet                 |
| Darstellung (6)    |                |                                              |
| Sitzung (5)        |                |                                              |
| Transport (4)      | Transport      | TCP, UDP, SCTP                               |
| Vermittlung (3)    | Internet       | IP (IPv4, IPv6), ICMP (über IP)              |
| Sicherung (2)      | Netzzugang     | Ethernet, Token Bus, Token Ring, FDDI, IPoAC |
| Bitübertragung (1) |                |                                              |
## 1.3. Dienste
Beispiele für Dienste im Internet und ihre Protokolle WWW (HTTP, HTTPS)
- E-Mail (POP, SMTP, IMAP)
- Telnet (Telnet)
- FTP (FTP, FTPS, SFTP)
## 1.4. World Wide Web
- Ein Dienst im Internet
- Dienst der Verteilung von Hypertext-Dokumenten (Webseiten)
- 1989 von Tim Berners-Lee am CERN entwickelt mit dem Ziel Forschungsergebnisse mit Kollegen auszutauschen
##### WWW
The WorldWideWeb (W3) us a wide-area-hypermedia information retrieval initiative aiming to give universal access to a large universe of documents.
### 1.4.1. Dokumente im Internet
- Format: HTML (HyperText Markup Language)
- Aktuell in Version 5 vom W3C standardisiert
- Wird von allen Browsern verstanden
- Diverse Erweiterungen gehören nicht zum Standard
	- z.B. Frames, JavaScript
	- Erweiterungen des W3C Standards sind i.d.R. browseranhängig
## 1.5. Domain name System (DNS)
- Adressierung von Webseiten des WWW wird durch das Domain Name System (DNS) unterstützt
- Hierarchischer Verzeichnisdienst
## 1.6. Verweise
- Verknüpfungen von Inhalten und weiteren Webseiten (Hyperlinks) erfolgt mittels
	- Uniform Ressource Identifier (URI)
		- Uniform Ressource Locator (URL)
		- Uniform Ressource Name ( URN)
	- URI sind allgemeine Bezeichner für abstrakte oder physikalische Ressourcen
	- Beispiele:
		- URI: th-wildau.de
		- URL: https://www.th-wildau.de
		- URN: urn:isbn:3827370191
## 1.7. Klassisches Web
- Statische miteinander durch Hyperlinks verknüpfte HTML-Dokumente
- Der Inhalt con Webseiten verändert sich nicht
## 1.8. Web 2.0
- Entstehung mit dem Beginn der 2000er Jahre
- Zeichnet sich durch User-Generated-Content (UGS; alternativ: User-Driven-Content) aus, aber auch interaktive Elemente
- Beispiele:
	- Soziale Netzwerke
	- Videoplattformen
	- Blogs
## 1.9. Web 3.0
- Aka Semantisches Web oder vom W3C als Web of Data bezeichnet
- Thematische Verknüpfung von Inhalten
	- Erweiterung von HTML um zusätzliches Vokabular (z.B. Ressource Description Framework - RDF)
	- Bereitstellung von Metainformationen
- Maschinen können Informationen leichter in Beziehung zueinander setzen (Data Mining, maschinelles Lernen, KI)
- Dezentrale Anwendungen
	- Beispiele: Mastodon, PeerTube