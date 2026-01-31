---
title: 13_Funknetze
date: 2025-10-13
modified: 2025-12-25
tags:
  - master
origin: "[[Spektrum_Informatik]]"
sources:
  - "[[Prof. Birgit Wilkes]]"
  - "[[13_Funknetze.pdf]]"
language: german
note-type: lecture
file-format: markdown (.md)
relations:
  - "[[Technische Hochschule Wildau]]"
---
## Elektromagnetische Strahlung
- Die Wellenlänge der hochfrequenten elektromagnetischen Felder liegt zwischen 3km und 1mm
- Die elektrische und die magnetische Komponente sich bei HF-EMV sehr eng miteinander gekoppelt. Daher kann man die Wirkung dieser Strahlung kaum nicht auf de Wirkung einer der beiden Komponenten zurückführen

![[Pasted image 20251225211358.png]]
## Spezifische Absorptionsrate SAR
- Die SAR ist eine physikalische Größe und ist ein Maß für die Absorption von elektromagnetischen Feldern in biologischem Gewebe, welche zu dessen Erwärmung führt
- Sie ergibt sich theoretisch aus dem Betragsquadrat der elektrischen Feldstärke multipliziert mit der elektrischen Leitfähigkeit und geteilt durch die Dichte des jeweiligen Gewebes
- Sie ist wohl stark von der Frequenz, als auch aufgrund von Resonanzeffekten von der Größe des absorbierenden Körpers abhängig. Je kleiner der Körper, desto mehr verschiebt sich die maximale aufgenommene Energie zu hohen Frequenzen
- Man unterscheidet zwischen einem Ganzkörper-SAR-Wert (bei Basisstationen, der über den ganzen Körper gemittelt wird, und einen Teilkörper-SAR-Wet (Handys) über 10g Gewebe
- Nebenstehende Grafik zeigt die durchschnittliche spezifische Absorptionsrate für drei Spezies, die einer Leistungsflussdichte von $10 W/m^2$ bei verschiedenen Frequenzen ausgesetzt werden, jeweils gemittelt über den ganzen Körper
- Die Absorption der Hochfrequenz hängt von mehreren Faktoren ab, wobei dir Größe des Objekts eine wichtige Rolle spielt: Die Resonanzfrequenz ergibt sich, wenn die halbe Wellenlänge etwas der Größe des Objekts entspricht. Bei kleineren Personen, Kinder und Babys liegt die Resonanzfrequenz daher höher. Man erkennt, dass bei 2,45 GHz eine Maus etwa 60 mal mehr Energie absorbiert als der Mensch
## Existieren Gesundheitsrisiken?
Gibt es Gesundheitsrisiken durch elektromagnetische Felder? 
Folgende Faktoren sind zu beachten:
- Thermische Wirkungen (Erwärmung)
- Nicht-thermische Wirkungen (weniger erforscht)
- Maximale Sendeleistungen der Funk-Standards. Die Sendeleistung ist für jeden Standard begrenzt.
- Zunehmende Vielzahl von Strahlungsquellen besonders in Ballungsgebieten. Sie liegt heute noch weit unter den Grenzwerten im unteren einstelligen Prozentbereich
## Funkfrequenzen und -standards
Folgende Frequenzen gehören zu den lizenzfreien ISM (Industrial, Scientific, Medical) Bändern:

![[Pasted image 20251226011555.png]]
## 868 Mhz
- 868 MHZ ist die meistgebrauchte Frequenz für Sensoren
- Der Frequenzbereich von 868 bis 870 MHz wurde vom rat der Europäischen Postbehörden (CEPT) als spezieller Frequenzbereich ausschließlich für Short Range Devices reserviert
- Um die gegenseitigen Störungen in diesem Frequenzband so gering wie möglich zu halten, wurden Beschränkungen für die Funkgeräte definiert, z.B.:
	- Beschränkung der Sendeleistung für alle Nutzer
	- Beschränkung der maximalen Sendedauer (Duty Cycle)
- Der Frequenzbereich von 868 bis 870 MHz ist in mehrere Bänder unterteilt, in denen unterschiedliche Duty-Cycles zulässig sind
## Duty Cycles
- Durch die Duty Cycles wird sichergestellt, dass auch bei verstärkter Nutzung dieser Funkfrequenzen, wie das im Bereich der Hausautomation zu erwarten ist, der störungsfreie Betrieb mehrere Systeme gewährleistet ist
- Mit zunehmenden Duty Cycle nimmt auch die Wahrscheinlichkeit von Störungen zu

![[Pasted image 20251226012301.png]]
## Frequenzen und Protokolle
- Auch wenn Produkte dieselben Frequenzen nutzen, können sie sich oft nicht untereinander verständigen, da sie verschiedenen Protokolle nutzen
- Beispielprotokolle für 868 MHz: enocean, zigbee, easywave, etc.
- Daraus resultiert das große Problem der Inkompatibilität der verschiedenen Funksysteme
## 2,4 GHz
- Durch die höhere Frequenz (kürzere Wellenlänge) ist die Durchdringung von Wänden schlechter
- Die mögliche Übertragungskapazität ist höher als in den niedrigen Frequenzen
- Für Audio- und Videoübertragung wird diese Frequenz genutzt
- Durch die starke und weiter zunehmende Belegung dieser Frequenz steigt die Gefahr für Störungen
- Als Alternative wurde der Frequenzbereich > 5 GHz eingerichtet
## Elektrosmog durch Funk
Elektromagnetische Felder haben Auswirkungen auf Menschen.
- Thermische Auswirkung: Wasser und damit auch menschliches Gewebe absorbiert elektromagnetische Strahlung und erwärmt sich dabei
- Nicht-thermische Auswirkung: Veränderung der Hirnströme und Schlafstörungen sind bei einigen Menschen nachgewiesen, die Ursachen sind noch nicht geklärt
## Alternative Powerline Communication
- Daten werden über das Stromnetz durch Steckdosenadapter übertragen
- Inhaus-Powerline gibt  es Schmalband- und Breitbandübertragung. Häufig genutzt wird Breitband.
- Eingespeiste Daten können an jeder Steckdose der gleichen Phase abgerufen werden

![[Pasted image 20251226013439.png]]
