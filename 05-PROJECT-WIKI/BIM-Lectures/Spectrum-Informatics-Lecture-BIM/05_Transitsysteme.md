---
rdf:type: schema:Course
dcterms:title: 05_Transitsysteme
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
## Repeater/Hubs
- Zur Kopplung von Netzwerken auf der Schicht 1 werden Repeater oder Hubs (Sternkoppler) eingesetzt
- Ein Repeater dient zur Regeneration und Verstärkung von Signalen
- Ein Hub koppelt zusätzlich noch mehrere Endsysteme sternförmig zu einem Netz
## Bridges
- Bridges koppeln Netzwerke auf Schicht 2 und leiten datenpunkte von einem Netz in das andere
- Es werden sowohl homogene Netze (IEEE 802.x mit IEEE 802.x), als auch heterogene Netze (IEEE 802.x mit IEEE 802.y, $x\neq y$) gekoppelt
## Transparente, lernende Bridges
- Problematisch ist die Existenz von redundanten Wegen zwischen Netzen, da durch die Broadcast-Weiterleitung endlos kreisende Pakete entstehen würden.
- Daher wird eine logische Baumstruktur über alle Bridges der involvierte Netzwerke gebildet. Verbreitet wird der z.B. Spannbaum Algorithmus benutzt.
- Die Bridge mit der kleinsten Kennung wird zur Root-Bridge
- Jede Bridge bestimmt den kostengünstigen Pfad zur Root-Bridge
- Für jedes LAN wird bestimmt, welche Bridge den günstigen Root-Anschluss besitzt
## Router
- Router koppeln Netzwerke auf ISO Schicht 3
- Sie ermöglichen die Kommunikation entfernter Endsysteme
- Routing dient in vermaschten Netzen der Findung des besten Weges
- Sie halten dazu spezielle, sehr umfangreiche Tabellen zur Wegewahl
- Router können Datenpakete auch segmentieren oder reassemblieren
- Aufgrund ihrer oben genannten Funktionen bekommen Router auch immer mehr Bedeutung als Firewall
## Routing-Tabelle
- Mit Hilf der Routing-Tabelle werden die in einem Netz verfügbaren Routen ermittelt
- Routing-Tabellen können verschiedenste Einträge enthalten, die zur Routenwahl dienen:
	- Adressen der Nachbarnetze
	- Wegbeschreibungen zu entfernten Netzen über andere Router
	- Standardrouten (default routes) für unbekannte Adressen
	- Kosten bzw. Entscheidungskriterien für Routen
## Entscheidungen zur Routenwahl
- Routing-Verfahren treffen die Entscheidung, über welchen Weg Daten geleitet werden
	- Primäre Ziele:
		- Hoher Netzdurchsatz
		- Geringe Datenverzögerung
	- Daten sollen über den Pfad mit den geringsten Kosten geleitet werden. Kosten können sein:
		- Tatsächliche Kosten
		- Kapazität oder Fehlerrate einer Verbindung
		- Auslastung oder Verzögerung einer Verbindung
		- etc.
	- Ort des Verfahrens:
		- Zentral durch Netzkontrollzentrum
		- Dezentral durch Verteilung des Algorithmus auf den Routern
	- Dynamik des Verfahrens:
		- Statistisch: Routing-Tabelle wird manuell vom Administrator aufgestellt
		- Dynamisch (adaptiv): Router erstellt die Routing-Tabelle selbst gemäß aktuellem Zustand des Netzes. Dazu werden Routing-Protokolle verwendet.
	- Zeitpunkt der Wegewahl:
		- Bei verbindungsorientierten Verbindungen nur zu Beginn, bei verbindungslosen für jedes Paket
## Routingverfahren
- Hot Potato: Jeder Router versucht, ein Datenpaket möglichst schnell wieder los zu werden und zum Ausgang mit der kürzesten Schlange zu leiten. Oft mit statistischem Routing kombiniert.
- Distance-Vector-Algorithmus: Ein verteiltes, adaptives Verfahren; jeder Router verwaltet eine Tabelle mit den kürzestem Wegen (Hop-Counts). Langsame Adaption bei Ausfall von Routern.
- Link-Status-Algorithmus: Nachbarrouter testen aktiv Verbindung mit Informationen und errechnen selbst z.B. Verzögerung und Kosten zu jedem Nachbarn. nach diesen Informationen wird der beste Pfad ausgewählt.
## Distance-Vector-Algorithmus
## Anforderungen an Routing-Protokolle
- Kosten der Routen müssen bekannt gemacht werden
- Mehr als eine Route zwischen zwei Netzen muss möglich sein
- Die Routing-Tabelle soll möglichst immer auf dem aktuellsten Stand sein
- Nach Topologieänderungen muss die Routenwahl sich möglichst schnell anpassen
- Die durch das Protokoll verursachte Netzlast soll möglichst gering sein
- Die Netzlast soll verteilt werden können
- Die Priorisierung von Datenströmen soll unterstützt werden
- Routenänderungen dürfen keine Belastungsspitzen im Netz hervorrufen
- Beliebige Netzgrößen können verwaltet werden
- Routenwahlfehler wirken sich nur lokal aus
- Gefälschte Routinginformationen werden durch Sicherheitsmechanismen abgeblockt
## Routing-Protokolle
- Im Internet wird unter anderem das RIP (Routing Information Protocol) eingesetzt, das auf dem Distance-Vector-Verfahren basiert. Zusätzliche Verfeinerungen werden zur schnelleren Adaption eingesetzt.
- Favorisiert im Internet wird das OSPF Protokoll (Open Shortest Path First), das das Link-Status-Verfahren benutzt
## Gateways#
- Gateways verbinden Netzwerke auf Schicht 4 des ISO Protokolls oder höher
- Gateways übersetzen nicht nur Protokollinformationen von einer Syntax in eine andere, sondern auch die Dateninhalte
- Gateways finden sich häufig an Übergängen von einem Netzbetreiber zum anderen
- Gateways werden auch applikationsbezogen eingesetzt, z.B. um Informationen für ein anderes Ausgabegerät nutzbar zu machen