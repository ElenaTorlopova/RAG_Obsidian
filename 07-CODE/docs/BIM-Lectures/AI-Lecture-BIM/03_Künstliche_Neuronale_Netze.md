---
dcterms:title: 03_Künstliche_Neuronale_Netze
dcterms:contributor:
  - "[[M. Eng. Janine Breßler]]"
dcterms:created: 2026-01-30
dcterms:modified: 2026-01-30
dcterms:subjects:
  - "[[Artificial Intelligence]]"
  - "[[Perceptron]]"
  - "[[Overfitting]]"
  - "[[Underfitting]]"
dcterms:isPartOf:
  - "[[Artificial_Intelligence_BIM25-Lecture]]"
  - "[[Bibliotheksinformatik]]"
dcterms:references:
schem:language: german
rdf:type: schema:Course
schema:educationalProgramName: "[[Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
# Künstliche Neuronale Netze
## Das Perceptron
- 1957 in den USA entwickelt, ursprünglich als Hardware-Modell
- Verwendet als Aktivierungsfunktion immer die Heaviside-Funktion
	- Klassifikation, da nur endlich viele Werte möglich (0 und 1)
- Bei Regression Spektrum von Zahlen möglich, z.B. von 0 bis 1
### Lernalgorithmus
1. Initialisiere Gewichte, z.B. alle $w_i = 0$ oder kleinen zufälligen Wert (Random)
2. Es gibt ein Trainingsset von Datenvektoren $\vec(x_1) bis (x_m),$ $\vec(x_i)=(x_{i1}...x_{in})$ $n=$ Anzahl der Inputs, jeweils mit korrektem Ergebnis (Label) $d_i$
3. Für alle $i=1,...,m$ wird folgendes ausgeführt:
	- $x_i$ als Input für das Perceptron, dieses berechnet den Output $y_i$
	- Gewichte werden aktualisiert: $w_j \leftarrow w_j + \alpha * x_{i,j} * (d_j - y_j)$
	- $\alpha$ = Lernrate/Lernfaktor (0,1]
4. Bei keinem zufriedenstellenden Ergebnis $\rightarrow$ wieder zu Punkt 2
## Das Perceptron am Beispiel
**Beispiel**: Verkauf von einem bestimmten Produkt
Das Perceptron erhält zwei Einträge, Alter und Einkommen.
Zusätzlicher dritter Eingang **Bias** mit konstantem Wert wird meist als Schwellenwert eingesetzt.

 Zwei Ergebnisse möglich:
 - 1 = Kunde kauft Produkt
 - 0 = Kunde kauft nicht Produkt

**Trainingsvorbereitung**:
- alle Gewichte auf 0: $w_0 = w_1 = w_2 = 0$ (üblicherweise random)
- Lernfaktor: $\alpha = 0.5$
- Trainingsset: $(20, 10) \rightarrow 1; (40, 50) \rightarrow 0$ (d (Label))

**Trainingsdurchführung**:
1. Für den ersten Trainingsdatensatz $(20, 10)$
   $H(0*1+0*20+0*10)=H(0)=1$
   Vergleich berechneter und erwarteter Wert $d:1 == 1$, also keine Korrektur des Gewichts
2. Für den zweiten Trainingsdatensatz $(40, 50)$
   $H(0*1+0*40+0*50)=H(0)=1$
   Vergleich berechneter und erwarteter Wert $d:0 != 1$, also Korrektur des Gewichts:
   $w_0 \leftarrow w_0+0.5*1*(0-1)=0-0.5=-0.5$
   $w_1 \leftarrow w_1+0.5*40*(0-1)=0-20=-20$
   $w_2 \leftarrow w_2+0.5*50*(0-1)=0-25=-25$

Wiederholung der Schritte 1 und 2, bis jeweils das gewünschte Ergebnis (Label) bei Eingabe der Trainingsdaten berechnet wird!
## Das Perceptron am weiterem Beispiel
Es entsteht eine Gerade (Hyperebene), die aus dem Ursprung verschoben ist.
Diese dient als Klassifikator, wenn die zwei Mengen linear separierbar sind:

Beim Perceptron ist die gewählte Hypereben nicht immer optimal.
Ander Ansätze des ML, wie das Modell der  _Support Vector Machine_ , bestimmen diese besser.

Die Grenzen des Perceptrons liegen darin, wenn zwei Mengen  nicht mehr durch eine Gerade trennbar sind:
## Mehrlagiges Netzwerk
Ein mehrlagiges Netzwerk aus vielen Neuronen.
**Idee**: Output von Neuronen wird Input von anderen Neuronen.
Es entstehen verdeckte bzw. versteckte Schichten (Blackbox).

Aufbau mehrlagiges Perceptron zur Berechnung von XOR:
- Eingangsschicht mit den zwei Eingangswerten $X_1$ und $X_2$
- Eine verdeckte Schicht á 3 Neuronen $p1, p2, p3$
- Ein Ausgangsneuron $q$
- Aktivierungsfunktion: Heaviside
## Lernverfahren Backpropagation
- **Gradientenverfahren**: Verfahren, um den minimalen Fehler in einer Fehlerfläche zu finden. Auch als globales Minimum bezeichnet.
- **Assoziation**:
	- Gebirge (2-dimensional)
	- Bergwanderer/in
	- Gesucht: Tiefster Punkt des Gebirges (Home sweet Home)
	- Strategie: Überprüfe aller möglichen Laufrichtungen, in die Richtung mit dem größten Abstieg werden ein paar Schritte gegangen. Dann wird wieder überprüft, so lange, bis Minimum gefunden ist.
- **Eigenschaften**:
	- Gradient zeigt in Richtung des steilsten Anstiegs
	- Umgekehrte Richtung zweigt in Richtung des steilsten Abstiegs
	- Gradient ist länger desto steiler der Anstieg
	- Schrittgröße wird in Abhängigkeit der Größe des Gradienten gewählt
		- sehr steil, große Schritte
		- weniger steil, weniger große Schritte

**Problem**: keine Informationen über die Fehlerfläche insgesamt, sondern nur aus der Kenntnis der lokalen Umgebung.

Gradienten werden für die Gewichte der letzten Schicht berechnet. Mit Hilfe von Gradient werden die Gewichte korrigiert.

Anschließend werden die Gradienten für die vorletzte Schicht berechnet und damit die Gewichte angepasst. Dabei kann auf die bereits berechneten Gradienten zurückgegriffen werden.

Gradient wird stückweise von hinten nach vorne berechnet $\rightarrow$ Fehlerrückführung
## Trainingsdurchführung
- Ein kompletter Durchlauf aller Trainings-Daten wird als Epoche bezeichnet.
- Anzahl der Trainings-Epochen ist ein wichtiger Hyperparameter für das Training von neuronalen Netzen.
## Metriken zur Bewertung des trainierten Künstlichen Neuronales Netzes
Beispiel: Spamfilter

Accuracy: $Accuracy=\frac{True Poitive+True Negative}{True Positive+True Negative+False Positive+False Negative}$
Bei einem ausgewogenen Datenset (Verteilung der Daten auf die Klassen) kann die Genauigkeit/Accuracy ein grober Indikator für die Modellqualität sein. Es sollten jedoch weitere Messwerte betrachtet werden.

Precision: $Precision=\frac{True Positive}{True Positive+False Negative}$
Maß für korrekt identifizierte positive Klassifizierung gegenüber allen positiven Klassifizierungen. Wichtig, wenn False-Positive Klassifizierungen "teuer" sind.

Recall: $Recall=\frac{True Positive}{True Positive+False Negative}$
Maß für korrekt identifizierte positive Klassifizierung gegenüber allen positiven Daten im Datenset. Wichtig, wenn False-Negative Klassifizierung "teuer" sind.

F1-Score: $F1=\frac{2*Precision*Recall}{Precision*Recall}$
Harmonisches Mittel aus Precision und Recall. Bei unausgewogenen Datensets (Verteilung der Daten auf die Klassen) ist der F1-Score besserer Metrik zur Bewertung des Modells gegenüber der Accuracy.
## Faustregel
Gelabelte Daten werden in 80% Trainings- und 20% Testdaten aufgeteilt!
Güte der Testdaten ist essentiell für Güte des Neuronalen Netzes!
## Overfitting und Underfitting
Bei der Generalisierung durch ein Künstliches Neuronales Netz können zwei Probleme auftreten:
- **Overfitting**: das Modell ist überangepasst
	- reagiert gut auf die Trainingsdaten und schlecht auf die Testdaten
	- zu stark auf Beispiele abgestimmt
	- irrelevante Unterschiede oder statistisches Rauschen werden mit einbezogen
- **Underfitting**: das Modell ist zu wenig angepasst
	- reagiert bereits schlecht auf Trainingsdaten
	- zu wenig Ausdruckskraft, um relevante Unterschiede berücksichtigen zu können