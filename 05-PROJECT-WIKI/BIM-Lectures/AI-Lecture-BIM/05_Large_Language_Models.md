---
dcterms:title: 05_Large_Language_Models
dcterms:contributor:
  - "[[M. Eng. Janine Breßler]]"
dcterms:created: 2026-01-30
dcterms:modified: 2026-01-30
dcterms:subjects:
  - "[[Artificial Intelligence]]"
  - "[[Large Language Models]]"
  - "[[Transformer Networks]]"
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
# Large Language Models
- Sind ein Unterbereich der Künstlichen Netze
- Verarbeitung, Interpretation und Generierung von natürlicher menschlicher Sprache
## Natural Language Processing
Einsatzgebiete:
- Textklassifikation
	- Eingabetext wird in vordefinierte Gruppen kategorisiert bspw. Sentimentanalyse
- Automatisches Übersetzen
	- Text aus einer Sprache in eine andere übersetzen
- Beantworten von Fragen
	- Beantwortung erfolgt basierend auf einem gegebenen Text, z.B. FAQs eines Onlinekundenserviceportals
- Textgenerierung
	- Generierung eines kohärenten und relevanten Ausgabetextes, der auf einem Eingabetext basiert, dem sogenannten Prompt
## Large Language Models
- (Sehr) große Sprachmodelle, die versuchen, natürliche, menschliche Sprache zu verarbeiten, zu interpretieren und zu erzeugen
- Sie sind in der Lage sprachbezogene Aufgaben auszuführen
- Large Language Models (LLM) werden hierfür mit der großen Textmengen trainiert, um Muster und Beziehungen zwischen Wörtern in Sätzen zu erkennen
- Datenquellen hierfür: Bücherarchive, Wikipedia, Reddit, GitHub, Webseiten aus dem Internet u.v.m.
## Die Anfänge: Recurrent Neural Networks
- Recurrent Neural Networks (RNN) stellen eine Familie von Netzwerkarchitekturen dar
- RNN sind git geeignet für die Verarbeitung von sequenzieller Daten, deren einzelne Komponente in Beziehung zueinander stehen
	- Sprache
	- Schrift
	- Tonsignale
- Ein RNN besteht aus Eingabeschicht, beliebig vielen versteckten Schichten und einer Ausgabeschicht
- Die Berechnung setzt sich aus Eingabe und Zustand zusammen --> durch Rückkopplung möglich
	- Verbindung von Neuronen einer Schicht zu Neuronen derselben oder einer vorangegangen Schicht
- Zustand repräsentiert bisher verarbeitete gesamte Sequenz --> Speicher von früheren Berechnungen und Eingaben
### One-Hot-Darstellung (One-Hot-Encoding)
- Klassische vektorielle Darstellung
- Länge des Vektors entspricht der Anzahl der Wörter im Trainingsvokabular V
- Jedem Wort des Wortschatzes wird ein Index zugewiesen
### Verteilte Wortvektoren (Distributed-Word-Vectors)
- Erstellung und Einbettung von Wortvektoren in einem multidimensionalen Raum
- Der Abstand zwischen den Wortvektoren spiegelt ihre semantische und syntaktische Beziehung wieder
- Wörter mit ähnlicher Bedeutung können in Gruppen zusammengefasst werden, Wörter mit unterschiedlichen Bedeutungen liegen weiter auseinander
- Bekannter Vertreter: Word2Vec
	- Continuous Bag-of-Words
	- Skip-Gram
### Continuous Bag-of-Words (COBW)
- Ziel: Vorhersage eines Wortes anhand des Kontextes
- Es werden die Wörter vor und nach dem zu erratenden Wort betrachtet (Kontext), um daraus das Zielwort vorherzusagen
- Hierfür wird z.B. die One-Hot-Darstellung verwendet und ein einfaches Neuronales Netz zum Antrainieren eingesetzt
- Bei der Bestimmung des Zielwortes wird der Kontext im Training als Eingabe in das Neuronale Netzwerk verwendet
- Die Ausgabe ist das Zielwort mit der höchsten Wahrscheinlichkeit
### Skip-Gram
- Ähnlich wie CBOW, nur genau umgekehrt
- Die Eingabe für das Neuronales Netz ist ein Wort
- Die Ausgabe sind Wörter innerhalb eines bestimmten Bereichs vor und nach dem Eingabewort voraus, also der Kontext
### Architektur de Neuronalen Netzes
- 1 Eingabeschicht (One-Hot)
- 1 versteckte Schicht (Die berechneten Gewichte von der Eingabe zu der versteckten Schicht sind die verteilten Wortvektoren)
- 1 Ausgabeschicht
- Die antrainierten Gewichte der verdeckten Schicht repräsentieren die Wortvektoren
- Jedem Eingabewert kann ein Wortvektor zugeordnet werden mit der Eigenschaft eines räumlichen Bezugs zu ähnlichen Worten
- Klassische RNN werden mit diesen verteilten Wortvektoren trainiert
## Long-Short-Term-Memory
- Auch bei RNN besteht das Problem des verschwindenden Gradienten im Training
	- Erschwert das Erlernen von Beziehungen über längere Zeiträume hinweg
	- Frühere Eingaben werden vergessen, je weiter in der Sequenz vorangeschritten wird --> Kurzzeitgedächtnis
- Um dem entgegenzuwirken, wurde die Long-Short-Term-Memory-Architektur (LSTM) entwickelt:
## Transformer
### Transformer-Architektur
- State of the Art heutzutage im Natural Language Processing
- Erstmals vorgestellt in der Veröffentlichung von Vaswani et. al. "Attention is All You Need" 2017
- Vorteil gegenüber rekurrenten anderen Modellen: Bewahren des Kontexts über lange Sequenzen hinweg, effizienter, das Parallelisierung möglich
- Zentraler Bestandteil: Attention-Mechanismus
	- Nicht alle Wörter in einer Sequenz sind gleich wichtig
	- Relevante, signifikante Begriffe erhalten besondere Aufmerksamkeit
	- Dadurch kann der Kontext besser erfasst werden
## Attention Is All You Need
### Self-Attention
- Aufmerksamkeitsmechanismus, der alle Tokens einer Sequenz miteinander in Beziehung setzt
- Dadurch können Token einer Sequenz nach Relevanz gewichtet sowie Kontext Informationen und langfristige Abhängigkeiten erfasst werden
- Wird typischer Weise in sogenannten Encodern eines Transformer-Netzwerks eingesetzt
- Jedes Wort bzw. Token schenkt jedem anderen Token, je nach Abhängigkeit, mehr oder weniger Aufmerksamkeit
### Cross-Attention
- Arbeitet auf zwei unterschiedlichen Sequenzen, z.B. auf der Eingabe- und Ausgabesequenz einer Übersetzung
- Wird typischer Weise in sogenannten Decodern eines Transformer-Netzwerks eingesetzt
- Ermöglicht des Fokus auf relevante Tokens in der Eingabesequenz, Ausgabesequenz zu generieren

Die Klassische Transformer-Architektur aus der Veröffentlichung "Attention Is All You Need" von Vaswani et. al.
## Tokenisierung
- Umwandlung einer Textfolge in kleinere Teile, damit diese maschinell besser verarbeitet werden können
- In einem GPT-Modell wäre dies z.B. die Texteingabe, d.h. der Prompt
- Jedes Sprachmodell verfügt über einen Tokenizer, der die Umwandlung durchführt
- Ein Token steht für ein Wort, ein Wortteil oder Leer- und Satzzeichen

```python
"Die Hauptstadt von Österreich ist Wien"
Die|Haupt|statd|von|Öster|reich|ist|Wien
```
Ergebnis: 8 Tokens
## Input Embedding + Positional Encoding
### Input Embedding
- Jedes Token word in einen Vektor mit einer Dimension von z.B. 512 übersetzt
	- Verwendung von vortrainierten Modellen
	- Abbildung der Token mit Hilfe derer Position im Vokabular (ID), der Vektor wird im Training optimiert
### Positional Embedding
- Der Abstand der Wörter zueinander in einer Textfolge ist wichtig
- Da die Transformer-Architektur über keine rekurrenten Strukturen verfügt, verfügt es keine Informationen über die Reihenfolge der Wörter und damit deren Abstand zueinander
- Deshalb wird für jedes Token ein Vektor mit gleicher Dimension wie beim Input-Embedding erstellt, die die Positionsinformationen des Tokens in der Textfolge enthalten
## Multi-Head-Attention
### Single-Head-Attention
- Unter Single-Head-Attention ist die klassische Self-Attention zu verstehen:
	- Die Eingabe wird in dreifacher Ausfertigung dem Attention-Mechanismus übergeben
	- Anhand der Eingabesequenz entstehen drei Matrizen mit antrainierten Werten: $Query(Q),Key(K),Value(V)$

Query: Anfrage für ein Token an andere Token
- "Welche Token sind für das Token relevant?"

Key: Merkmale eines Tokens
- Repräsentiert die Eigenschaften, dass es sich bei dem aktuellen abgefragten Token z.B. um ein Subjekt handelt.

Value: Der Inhalt eines Tokens
- Wird bei Relevanz bei der Ausgabe berücksichtigt
### Multi-Head-Attention
- Bei Single-Head-Attention wird die Aufmerksamkeit für die Tokens nur einmal berechnet, d.h. es kann nur eine/n Aspekt/Art von Beziehung zwischen den Tokens analysiert werden
- Bei Multi-Head-Attention berechnen mehrere Köpfe (z.B. 3) die Aufmerksamkeit der einzelnen Token mit unterschiedlichen Aspekten oder auch Perspektiven
- Unterschiedliche Aspekte können sein:
	- Head 1 lernt die syntaktischen Beziehungen zwischen den Tokens
	- Head 2 lernt die semantischen Beziehungen zwischen den Tokens
	- Head 3 lernt die positionsabhängigen Beziehungen
- Die Kombination der Ergebnisse der einzelnen Heads deckt verschiedene Aspekte der Beziehungen zwischen den Tokens ab

Wie viele Heads wurden hier bei der Multi-Head-Attention verwendet?
Antwort: 8
## Feed-Forward-Netz & Co.
### Feed-Forward-Netz
- Arbeitet im Anschluss an die Multi-Head-Attention-Schicht
- Hat die Aufgabe die individuellen Repräsentationen der Tokens zu spezialisieren bzw. zu verfeinern
- Dafür wird jedes Eingabe-Token unabhängig voneinander nicht-linear transformiert
### Residuale Verbindungen
- Ohne residuale Verbindungen würde die ursprüngliche Eingabe in die Schicht vollständig transformiert
- Die ursprüngliche Eingabe wird durch die residuale Verbindung zu der Ausgabe der Schicht hinzuaddiert
- Teil der ursprünglichen Informationen wird unverändert durch die Schichten weitergegeben
### Add & Norm
- Add ist das Hinzuaddieren der ursprünglichen Eingabe zu der Ausgabe der Schicht
- Normalisiert die resultierende Summe --> wirkt dem verschwinden oder explodierenden Gradienten entgegen
## Masked Multi-Head-Attention
### Cross Attention
- Szenario: Training zur Textübersetzung von Deutsch nach Englisch
- Fokus auf relevante Tokens in der Eingabesequenz im Encoder (Deutsch), um in Abhängigkeit davon das nächste Token für die Ausgabesequenz im Decoder (Englisch) zu generieren
	- Query --> Decoder
	- Key und Value --> Encoder
- Dabei ist es wichtig, dass der Decoder die Query ausschließlich in Abhängigkeit des aktuellen und der bisher generierten englischen Tokens erstellt, dafür sorgt die Maskierung
## Linear- und Softmax-Schicht
### Linear-Schicht
- Projiziert die Ausgabe des Decoders in den Vokabelraum
- Jedes Token im Vokabular erhält einen sogenannten Logit-Wert
### Softmax-Schicht
- Wandelt die Logit-Werte für jedes Token in Wahrscheinlichkeitswerte um
- Besonderheit Softmax-Funktion: Die Summe aller Wahrscheinlichkeiten ist 1
- Das Token mit der höchsten Wahrscheinlichkeit wird ausgewählt