---
title: 02_Internet
date: 2025-10-13
modified: 2025-12-18
tags:
  - master
origin: "[[Spektrum_Informatik]]"
sources:
  - "[[Prof. Birgit Wilkes]]"
  - "[[02_Internet.pdf]]"
language: german
note-type: lecture
file-format: markdown (.md)
relations:
  - "[[Technische Hochschule Wildau]]"
---
## Was bedeutet "Internet"?
- Globales Netzwerk aus Rechnersystemen, die selbst wieder Netzwerke darstellen können
- Rechner bilden Knoten des Netzes und sind eindeutig adressierbar
- "Internet" bezeichnet eine spezielle logische Struktur (Topologie, Adressierung, Protokolle) eines solchen Netzwerks
- Keine Festlegung der Hardware, der Art der Verarbeitung und der Betriebssysteme
## Client-Server-Architektur
- Ein Server bietet einen Dienst über eine definierte Schnittstelle an. Er antwortet auf Anfragen synchron (innerhalb eines bestimmten Zeitintervalls).
- Ein Client stellt asynchron (zu einem beliebigen Zeitpunkt) Anfragen an den Server

![[Pasted image 20251014065050.png|500]]
## Netzwerk-Nodes
Die Geräte eines Netzwerks können in zwei Gruppen aufgeteilt werden:
- Solche, die Informationen erzeugen und verarbeiten (Endsysteme, End-Host)
- Solche, die den Datenfluss im Netzwerk regeln und verschiedene Teilnetze miteinander verbinden (Zwischen- oder Transitsysteme oder Interworking Units (IWU))

Je nach Verwendungszweck können diese Zwischensysteme auf verschiedenen Schichten des OSI Referenzmodells angesiedelt werden.
