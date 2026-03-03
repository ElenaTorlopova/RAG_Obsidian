---
rdf:type: schema:Course
dcterms:title: 02_Maschinelles_Lernen
dcterms:contributor:
  - "[[M. Eng. Janine Breßler]]"
dcterms:created: 2026-01-30
dcterms:modified: 2026-01-30
dcterms:isPartOf:
  - "[[Artificial_Intelligence_BIM25-Lecture]]"
dcterms:references:
schem:language: german
schema:educationalProgramName: "[[M.Sc. Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
# Maschinelles Lernen

##### Menschliches Lernen:
"Jede Verhaltensänderung, die sich auf Erfahrung, Übung oder Beobachtung zurückführen lässt."
##### Maschinelles Lernen:
- Die Maschine bzw. das Computerprogramm lernt aus Erfahrung und bewirkt damit eine Änderung des Verhaltens
- Statt einer statischen Programmierung erlernen die Computer anhand von Daten (Erfahrungen) ein Verhalten
## Knowledge Discovery in Databases
##### KDD als Prozess
- Auswahl von relevanten Daten für angestrebtes Ziel aus Datenbank
- Vorverarbeitung der Daten, indem Daten bereinigt werden, z.B. Werte wie NaN
- Transformation der Daten, um diese an den Algorithmus anzupassen
	- String-Daten werden in numerische Werte transformiert
	- Datenreduzierung:
		- Ausreißer-Datensätze werden entfernt
		- einzelne Merkmale werden zu einem Metamerkmal zusammengefasst 
	- Normierung der Daten, bspw. auf Werte zwischen 0 und 1
- Machine Learning durch Auswahl eines geeigneten Werkzeugs durchführen
- Interpretation und Evaluation der Ergebnisse in den Daten, das Wissen
- Prozess kann iterativ durchgeführt werden, also Teilschritte wiederholt werden

--> Maschinelles Lernen und Teil des KDD-Prozesses
## Daten, Daten und noch einmal Daten
Daten stellen Dreh- und Angelpunkt des Maschinellen Lernens dar

Strukturierte Daten sind in der Regel besser als Grundlage für das maschinelle Lernen geeignet!
### Big Data
"[...] Datenbestände, die bzgl. ihrer Menge, Komplexität, schwachen Strukturierung und/oder Schnelllebigkeit ein Problem für die herkömmliche Datenverarbeitung bzw. Datenanalyse sind."

Ziel ist das Extrahieren von Informationen aus Daten, um neues Wissen zu generieren.

- Durch kombinierte und intelligente Analyse der Date sollen Muster und Beziehungen erkannt werden
	- bessere Prognosen
- Intelligente Datenanalyse transformieren Big Data in Smart Data
- Anforderungen an die Daten:
## Maschinelles Lernen
##### Alle Techniken haben gemein:
Konstruktion/Lernen einer mathematischen Funktion
$f:X \rightarrow Y$
### Überwachtes Lernen - Klassifikation
Große Mengen an Ein- und Ausgabedaten (Datenpaare), die über konkreten Funktionswert verfügen
- gelabelte oder auch markierte Daten
- Computer wird mit Datensätzen trainiert
- Anschließend soll Computer neue Bilder eigenständig den Labeln zuordnen (Klassifikation)
- Die Zielmenge $Y$ für das Ergebnis der Funktion ist diskret, die Klassifikation bildet auf Klassen (auch Label) mit nominalen Werten ab, hier: Hund oder Katze
- Generalisierung von bekannten auf bisher unbekannte Datenpaare
### Überwachtes Lernen - Regression
- Regression erfolgt analog zur Klassifikation
- Ziel ist das Erkennen von numerischen Zusammenhängen
- Zielgröße ist im Gegensatz zur Klassifikation i.d.R. ein kontinuierlicher Bereich, mögliche Problemstellungen:
	- Berechnung des optimalen Drehwinkels
	- Berechnungen des maximalen Kreditahmens
	- Prognose zur Anzahl der vermieteten Fahrräder
### Bestärktes Lernen
Ansatz interessant für Optimierungsprobleme
- optimale Strategie nicht bekannt
- Labeln von Daten nicht möglich, da nicht klar ist, welche Abfolge von Teilschritten genau richtig bzw. falsch ist
- bekannt ist jedoch, was einen wünschenswerten und nicht wünschenswerten Ausgang darstellt
- agentenbasiert, eine optimale Strategie wird anhand von Belohnung oder Bestrafung entwickelt

Voraussetzung für das bestärktes Lernen:
- Beschreibung der Aufgabe
- Angabe, welche Aktionen möglich sind
- verlässlicher Simulator, mit dem vorgenommene Aktionen bewertet werden können

--> Den rest findet die Maschine im Idealfall selbstständig heraus
### Unüberwachtes Lernen
Keine Zielwerte oder Zielergebnisse für Datenmenge vorhanden, da diese meist sehr groß und unstrukturiert
- keine Fehlerberechnung und Verteilung von Belohnung/Strafen möglich
- Finden von Strukturen/Ähnlichkeiten in unmarkierten Datenmengen anhand con Merkmalen/Features
- Einteilung in Cluster/Gruppen (Clustering)
##### Anwendungsbeispiel:
"Kunden, die diesen Artikel gekauft haben, kaufte auch..."
"Das könnte Sie auch interessieren..."

Ziel ist das Einsortieren von Kunden in Gruppen mit ähnlichen Merkmalsausprägungen, um einen Mehrwert zu erzeugen!
## Clustering vs. Klassifikation
##### Clustering
Beim **Clustering** ist die Intention, Gruppen von ähnlichen daten zu finden. Zu Beginn des Lernalgorithmus steht noch nicht fest, durch welche Merkmale und Ähnlichkeiten/Unterschiede die Gruppen entstehen.
**Beispiel E-Mail**: Bei einer Menge von E-Mails werden zwei Cluster gebildet, die ein Experte anschließend als "Spam" bzw. "Wichtig" erkennt.
##### Klassifikation
Bei der **Klassifikation** steht bereits vor Anwendung des Lernalgorithmus fest, in welche Gruppen ein Objekt eingeteilt werden kann. Das Ziel des Lernalgorithmus besteht darin, die Merkmale zu detektieren, die für die Zuordnung in die Gruppen signifikant sind.
**Beispiel E-Mail**: Spam und wichtige E-Mails unterscheiden sich z.B. in den Absendern und den verwendeten Wörtern.
## Maschinelles Lernen
Welches Lernverfahren bietet sich für welchen Problemstellung an?

Ein Beispiel: Startup für KFZ-Versicherungen
- Beitragsklasse soll anhand von **tatsächlichen** aufgetretener Schadensfälle bestimmt werden
- Folgende Daten liegen vor
	- Alter
	- Höchstgeschwindigkeit
### Herkömmlicher Ansatz
Analytisches Herangehen an die Problemstellung:
- Analysten finden anhand der Datensätze Regeln heraus
- Softwareentwickler setzen diese programmatisch  um
- Software wird zur Klassifikation von Kunden genutzt

**Regeln**:
1. Jüngere Kunden haben eher ein höheres Risiko, mit schnellen autos ein sehr hohes Risiko
2. Ältere Kunden haben tendenziell ein hohes Risiko
3. Andere Kunden haben ein geringes Risiko
### Bestärktes Lernen:
Wichtig für das bestärkte Lernen:
- Beschreibung der Aufgabe
- Angabe, welche Aktionen möglich sind
- Verlässlicher Simulator, mit dem vorgenommene Aktionen bewertet werden können

Für allgemeine Problemstellungen und auch für das erstellen der Versicherungseinstufungen nicht geeignet.
### Unüberwachtes Lernen:
Wichtig für das Clustering:
- Daten sind nicht gelabelt, die Kundendaten werden also berücksichtigt, aber nicht die Einschätzung der Schadensklasse
- Anhand von Features versucht das Clustering Verfahren die einzelnen Objekte Gruppe zuzuordnen
### Überwachtes Lernen:
Wichtig für das überwachte Lernen:
- Daten müssen gelabelt sein: passende Paare von Ein- und Ausgabedaten
- Generalisierung von bekannten auf nicht bekannte Daten
## Zusammenfassung
- Beim Maschinellen Lernen (ML) erlernen die Computer anhand von Daten (Erfahrungen) ein Verhalten
- Maschinelles Lernen ist Teil des Prozesses *Knowledge Discovery in Databases*
- Aus Big Data soll mit Hilfe von Maschinellen Lernen neues Wissen generiert werden
- Grundsätzlich wird bei ML zwischen überwachtem, unüberwachtem und bestärkendem  Lernen unterschieden
- Die Auswahl des Lernverfahrens ist abhängig von der Problemstellung und der Daten, die zur Verfügung stehen
- Die Qualität der Daten ist ausschlaggebend für den Erfolg des Maschinellen Lernprozesses