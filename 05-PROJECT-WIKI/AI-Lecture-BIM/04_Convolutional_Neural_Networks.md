---
dcterms:title: 04_Convolutional_Neural_Networks
dcterms:contributor:
  - "[[M. Eng. Janine Breßler]]"
dcterms:created: 2026-01-30
dcterms:modified: 2026-01-30
dcterms:subjects:
  - "[[Artificial Intelligence]]"
  - "[[Convolution Neural Networks]]"
dcterms:isPartOf:
  - "[[Artificial_Intelligence_BIM25-Lecture]]"
  - "[[Bibliotheksinformatik]]"
dcterms:references:
---
# Convolution Neural Networks
## Motivation
Gefaltete Neuronale Netze, auch Convolutional Neural Networks (CNN), haben einen speziellen Aufbau, d.h. es gibt unterschiedliche Arten von Schichten mit unterschiedlichen Aufgaben.

CNNs oder auch ConvNets erzielen besonders in den folgenden Disziplinen gute Ergebnisse:
- Bildverarbeitung
- Verarbeitung von Sprache
- Verarbeitung von Audiosignalen
## Warum Convolutional Neural networks?
- Erkennung von räumlichen Informationen (kanten, Ecken, Formen und Texturen)
- Reduktion der Parameter (Performanz- und Effizienzsteigerung)
- Positionsunabhängige Merkmalserkennung (Translationsinvarianz)
- Pooling: Extraktion von wichtigen und Unterdrückung von unwichtigen Merkmalen
## Filter/Kernel
Die Filter haben die Aufgabe, Kanten, Formen oder Texturen zu erkennen:

Beispiel Kantenerkennung mit Hilfe des Prewitt-Filters:

Horizontaler Prewitt-Filter:

Vertikaler Prewitt-Filter:

Konkrete Kantenerkennung mit dem Prewitt-Filter:
## Aktivierungsfunktion
Rectified Linear Unit, auch ReLu
- Aktivierungsfunktion
- Schnelle und effiziente Berechnung
- Viele Neuronen werden deaktiviert, d.h. auf "0" gesetzt
- Weniger betroffen vom Vanishing-Gradient-Problem als z.B. die Sigmoid-Funktion

$$f(x)=ReLu(x)=max(0,x)$$
## Auswirkungen der Filter auf die Dimensionen der Ergebnismatrix
Problem?
## Abhilfe schafft das Padding
Durch das Anwenden von Filtern bei der Faltenoperation gehen Randinformationen verloren.

Zusätzlich werden Pixel am Rand weniger oft in die Berechnungen einbezogen als die inneren!

Die Dimension der Ausgabematrix schrumpft.

Mit Hilfe des sogenannten padding (auch Zero-Padding) lässt sich dies umgehen!
## Abhilfe schafft das Zero-Padding

**Same-Padding**: Fügt Pixel der Eingabe hinzu, sodass die Ausgabe die gleiche Größe hat und die Randpixel berücksichtigt werden.

**Valid-Padding**: Fügt keine Pixel der Eingabe hinzu, sodass die Ausgabe verkleinert und Randpixel ignoriert werden.
## Schrittweiter/Stride
Die Schrittweite definiert wie viele Einheiten der Filter gleitet!
Die hat Einfluss auf die Dimension der Eingabematrix, je größer der Schritt desto kleiner die Dimension im Ergebnis!
## Ergebnismatrix
Die Dimension einer zweidimensionalen Ergebnismatrix $O$ wird durch die folgenden Eigenschaften bestimmt:

O = Output size
n = Input size
f = Kernel size
p = Padding
s = Stride
## Pooling
Die Pooling-Schicht befindet sich in der Regel hinter einer oder mehreren Konvolutionalen Schicht(en) und verarbeitet die Ergebnisse dieser.

**Intention**:
Reduzierung der Dimensionalität (Downsampling), dem Rechenaufwand und der Parameter bei Bewahrung der wesentlichen Merkmale (Informationen)!

Bewährte Techniken: Max-Pooling, Average-Pooling und Min-Pooling

Die Filter werden, im Gegensatz zur konvolutionalen Schicht, nicht überlappend angewendet.

Ergebnis der konvolutionalen Schicht

**Max-Pooling vs. Average-Pooling vs. Min-Pooling**
Max Pooling
- Hervorheben der hellsten Pixel
- Nützlich, wenn der Hintergrund des Bildes dunkel ist und die helleren Pixel die Informationen enthalten
- Beispiel: MNIST-Datensatz --> Die Ziffern sind weiß und der Hintergrund ist schwarz

Average-Pooling
- Glättet das Bild
- Scharfe Merkmale werden u.U. nicht erkannt

Min-Pooling
- Gegenteil von Max-Pooling
- Hervorheben der dunkleren Pixel
- Nützlich, wenn der Hintergrund des Bildes hell ist und die dunkleren Pixel die Inforationen enthalten

Min- und Max-Pooling werden verwendet, um die auffälligsten Merkmale zu extrahieren.

Weniger auffällige Merkmale werden ignoriert, wie z.B. Rauchen oder "nicht relevante" Informationen.

Average-Pooling wird verwendet, wenn feine Details und/oder Texturen wichtig sind.
## Merkmalsextraktion
Die konvolutionalen und Pooling-Schichten haben die Aufgabe Merkmale zu extrahieren.

Durch die hintereinander geschalteten Faltungen erhält man:
- eine hierarchische Darstellung des Eingabebildes
- den Effekt, dass je tiefer die Ebenen im CNN, desto komplexer und abstrakter sind die Merkmale, die durch die Filterung dieser Ebene extrahiert werden können:
	- vorderste Ebene: Kanten oder Texturen
	- tiefere Ebene: Formen oder Objekte
## Vollständig verbundene Schicht
Die vollständig verbundene Schicht ist für die Klassifikation der extrahierten Merkmale aus den vorhergehenden Schichten zuständig.

Dies erfolgt mit Hilfe von klassischen Feed-Forward-Netzen, deren Schichten voll vermascht sein.

Die Ausgabe/Output der letzten Pooling-Schicht(en) dient hierfür als Eingabe/Input.

Das Format der Ausgabe/Output muss hierfür angepasst werden durch das sogenannte Flattening/Abflachen:

Anschließend erfolgt eine Klassifikation mit einem voll vermaschten Neuronalen Netzwerk (Feed Forward):