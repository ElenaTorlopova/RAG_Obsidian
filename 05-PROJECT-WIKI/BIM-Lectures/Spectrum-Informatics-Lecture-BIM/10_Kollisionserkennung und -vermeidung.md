---
title: 10_Kollisionserkennung und -vermeidung
date: 2025-10-13
modified: 2025-12-24
tags:
  - master
origin: "[[Spektrum_Informatik]]"
sources:
  - "[[Prof. Birgit Wilkes]]"
  - "[[10_Kollisionserkennung_und_-vermeidung.pdf]]"
language: german
note-type: lecture
file-format: markdown (.md)
relations:
  - "[[Technische Hochschule Wildau]]"
---
## Kollisionserkennung/ -vermeidung
- Bei einem unkontrollierten und zufälligen Zugriff auf ein geteiltes Medium können Kollisionen der gesendeten Nachrichten auftreten
- Eine Kollision tritt dann auf, wenn zwei oder mehr Datenpakete zeitgleich, am gleichen Ort, mit gleicher Frequenz und Codierung aufeinandertreffen
- Im allgemeinen können dann die Daten der Pakete nicht mehr rekonstruiert werden, die Daten sind also verloren
## Aloha-Verfahren
- Das einfachste Verfahren, das Aloha-Verfahren, wurde für ein Funknetz an der Universität Hawaii entwickelt
- Die Funktionen haben einen wahlfreien Zugriff auf den Kommunikationskanal, das heißt die können zu jeder Zeit ein Datenpaket senden
- Dabei können Paketkollisionen auftreten
- Stellt eine Station fest, dass ein Datenpaket zerstört wurde, sendet sie es nach einem gewissen Zeitintervall nochmals
- Dabei müssen die Stationen die Neuübertragung zu unterschiedlichen Zeiten vornehmen
- Sie bestimmen individuell mittels eines Zufallszahlengenerators den nächsten Sendezeitpunkt
- Im Aloha-System liegt die Wiederholungszeit zwischen 200 und 1500 ms
- Die maximale Auslastung bei des Mediums bei diesem Verfahren liegt bei 18%

![[Pasted image 20251224154145.png]]
## Slotted Aloha-Verfahren
- Eine wesentliche Verbesserung des Aloha-Verfahrens ergibt sich, wenn man das Kollisionsfenster für Datenpakete verkleinert
- Dies wird erreicht, indem man die Zeiten einschränkt, zu denen Pakete gesendet werden dürfen
- Ein Paket darf immer nur in einem festen Zeitintervall $t_i$ gesendet werden
- Pakete können sich dann immer nur ganz oder gar nicht überlappen, aber niemals teilweise
- Ist t die zur Übertragung eines Pakets notwendige Zeit, war beim reinen Aloha-Verfahren, das Kollisionsfenster 2t lang, beim Slotted Aloha-Verfahren nur noch t
- Damit verdoppelt sich die maximale Auslastung des Mediums bei diesem Verfahren auf 36%

![[Pasted image 20251224154514.png]]
## CSMA-Verfahren
- Bei CSMA-Verfahren (Carrier Sense Multiple Access) hört eine Station vor dem Senden das Medium ab
- Sie überträgt nur Daten, wenn sie festgestellt hat, dass das Medium nicht in Benutzung ist (listen before talk)
- Ist der Übertragungskanal belegt, gibt es verschiedenen Strategien um fortzufahren:
	- Warte eine zufällige Zeitspanne und teste dann erneut das Medium (non-persistent)
	- Übertrage sofort, wenn das Medium frei ist. Wenn dabei eine Kollision auftritt, warte eine zufällige Zeitspanne (1-persistent)
	- Sende bei Freiwerden des Kanals mit der Wahrscheinlichkeit p. Sonst (1-p) ware eine zufällige Zeitspanne und lauschen erneut (p-pausiert)
## CSMA/CD
- Im CSMA-Verfahren überträgt ein Sender weiter Daten, obwohl eine Kollision aufgetreten ist. Damit wird Übertragungskapazität verschwendet.
- Das CSMA/CD-Verfahren (Carrier Sense Multiple Access / Collision Detection) verfügt zusätzlich über eine Kollisionserkennung
- Sie basiert auf dem 1-persistent CSMA, hört aber auch während des Sendens den Kanal ab und bricht den Sendevorgang sofort ab, wenn eine Kollision erkannt wird
- Der Ablauf ist wie folgt:
	- Falls das Medium frei ist, beginne sofort mit dem Senden
	- Ist das Medium belegt, warte bis es drei ist und beginne dann mit dem Senden
	- Wird ein zerstörtes Paket empfangen, wird also eine Kollision erkannt, stoppe sofort die Übertragung und sende ein Jamming-Signal (dies zeigt allen Stationen, dass eine Kollision stattgefunden hat)
	- Warte nach einer Kollision eine zufällige Zeit und beginne dann den Ablauf von vorne
- Beispiel:
	- Kollision bei $t_0+t_L-\epsilon$
	- B erkennt Kollision bei $t_0+t_L$
	- A erkennt Kollision bei $t_0+2(t_L-\epsilon)$

![[Pasted image 20251224160050.png]]
## Mindestsendedauer
- Soll eine Station die Kollision seines eigenen Signals mit einem anderen erkennen können, setzt dies eine Mindestsendedauer des Signals voraus
- Diese Mindestlaufzeit errechnet sich aus der doppelten Signalverzögerung der am weitesten entfernten Stationen
- Aus der Mindestsendedauer und der Übertragungsrate lässt sich die Paketmindestlänge berechnen
## Binary Exponential Backoff
- Es handelt sich um einen Mechanismus, um die Wahrscheinlichkeit von Kollisionen weiter herunterzusetzen
- Dabei wählt jede Station, die senden will einen ganzzahligen Zufallswert aus dem Intervall $[0,1]$ aus
- Die Zufallswerte stellen Zeitschlitze dar. Die Dauer eines Zeitschlitzes entspricht der Mindestsendedauer
- Kommt es wieder zu einer Kollision, wählen die Stationen erneut einen Zufallswert aus dem Intervall $[0,3]$
- Das Intervall nach $i$ Kollisionen berechnet sich nach $[0,2^i-1]$
## CSMA/CA
- CSMA/CA (Carrier Sense Multiple Access / Collision Avoidance) ist gegenüber CSMA/CD so abgewandelt, dass Kollision von Nutzdaten vermieden werden
- Vor der Übertragung wird eine Mitteilung über den Sendewunsch an das Ziel geschickt (RTS-Frame (Request to Send))
- Das Ziel quittiert diese Nachricht (CTS-Frame (Clear to Send))
- Jede Station, die das CTS hört, senden dann nicht, bis das Senden wieder freigegeben wird
- Jede Station, die das RTS, nicht aber das CTS gehört hat, darf gleichzeitig senden
- Nach dem die Station mit dem Sendewunsch die Bestätigung empfangen hat, beginnt sie mit dem Senden
- Der Empfänger bestätigt eine Nachricht mit einem ACK-Frame (Acknowledgment)
- Alle kollidierenden Knoten müssen auf das ACK warten
- Bei diesem Verfahren können nur die Steuerinformationen kollidieren
