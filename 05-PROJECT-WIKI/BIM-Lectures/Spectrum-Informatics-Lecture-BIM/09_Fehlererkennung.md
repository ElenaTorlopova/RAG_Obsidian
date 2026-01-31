---
title: 09_Fehlererkennung
date: 2025-10-13
modified: 2025-12-23
tags:
  - master
origin: "[[Spektrum_Informatik]]"
sources:
  - "[[Prof. Birgit Wilkes]]"
  - "[[09_Fehlererkennung]]"
language: german
note-type: lecture
file-format: markdown (.md)
relations:
  - "[[Technische Hochschule Wildau]]"
---
## Fehlererkennung
- Bitfehler auf dem Übertragungsweg haben Nachrichtenverfälschungen zur Folge
- Es gibt zwei mögliche Grundprinzipien zur Fehlererkennung:
	- Übertragung von redundanten Informationen zur Fehlerkorrektur beim Empfänger (error correction)
	- Übertragung von Kontrollparametern und Sicherheitsinformationen zur Fehlererkennung (error detection) beim Empfänger und Wiederholung der fehlerhaft übertragenen Informationen (retransmission)
## Parity Bits
- Jedes zu übertragende Zeichen wird um ein zusätzliches Paritätsbit erweitert. Bei gerader (ungerader) Parität wird die Anzahl der Einsen durch das Paritätsbit auf eine gerade (ungerade) Zahl ergänzt.
- Durch Paritätsbits wird jede ungerade Anzahl von Bitfehlern erkannt
- Die Längs- und Querprüfung VRC/LRC (Vertical / Longitudinal Redundancy Checking) liefert neben einer besseren Erkennung von Bitfehlern auch die Möglichkeit zur Korrektur

![[Pasted image 20251223221141.png]]
## Zyklische Blocksicherung
- Jede Zahl Z, welchem Zahlensystem sie auch angehört, kann als Polynom dargestellt werden: $a_n x^{n-1} + a_{n-1} x^{n-2} + a_{n-2} x^{n-3} + ... + a_3x^2 + a_2x^1 + a_1x^0$
- Hierbei ist $n$ die Nummer der Stelle, $a$ der Stellenwert und $x$ die Basis des Zahlensystems
- Beispiel: $5*10^4 + 0*10^3 + 2*10^2 + 7*10^1 + 8*10^0 = 50000 + 0 + 200 + 70 + 8 = 50278$
- Eine effektive Form der Datensicherung ist die zyklische Blocksicherung CRC (Cycling Redundancy Check)
- Das Verfahren basiert auf der Verwendung von Prüfpolynomen in Verbindung mit der Modulo-2-Arithmetik
- Ein Prüfpolynom n-ten Grades (Generatorpolynom) P(x) kann als Binärzahl der Länger n+1 interpretiert werden.
	- Beispiel: $P(x) = 1* x^4 + 0*x^3 + 0*x^2 + 1x^1 + 1*x^0 = x^4 + x + 1 = 10011$
- Der Block der zu sendenden Binärcodes wird multipliziert mit $2^n$ (erweitert um n Bits des Wertes 0)
- Eine Division dieser Binärzahl durch die des Polynoms liefert einen Divisionsrest der Länge n
- Dieser Divisionsrest (CRC) stellt die Prüfinformation dar und wird an die ursprünglichen Sendedaten angehängt und zum Empfänger übertragen
- Er dividiert die gesamte empfangene Zahl wieder durch das gleiche Prüfpolynom
- Ergibt sich bei dieser Division kein Rest, so war die Übertragung fehlerlos

![[Pasted image 20251223223706.png]]
