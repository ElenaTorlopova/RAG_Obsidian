---
title: 03_Schichtenmodelle
date: 2025-10-13
modified: 2025-12-19
tags:
  - master
origin: "[[Spektrum_Informatik]]"
sources:
  - "[[Prof. Birgit Wilkes]]"
  - "[[03_Schichtenmodelle.pdf]]"
language: german
note-type: lecture
file-format: markdown (.md)
relations:
  - "[[Technische Hochschule Wildau]]"
---
,,- Realisierung komplexer Aufgaben auf Computernetzen
- Verwendung monolithischer Lösungen ungeeignet
	- unflexibel
	- wartungsintensiv
- Daher: funktionale Zerlegung und Realisierung in Schichtenarchitektur (layered architectures)
## Schichtenarchitektur
Schichtenhierarchische Architektur
- Grundidee: Austausch von Diensten (services) zwischen den Schichten
- Für jeden Dienst gibt es einen service user und einen service provider
- Jede Schicht kann als service user und als service provider auftreten

![[Pasted image 20251014065747.png]]

- Jeder Schicht sind bestimmte Funktionalitäten zugeordnet
- Eine Schicht baut auf der darunterliegenden auf, d.h. sie nutzt deren Funktionen zur Erbringung ihrer eigenen
- Die Schichten kommunizieren über Schnittstellen (Interfaces) miteinander
- Die Anzahl und Funktionalität der Schichten kann je nach Architektur verschieden sein
- Für jede Schicht der Kommunikationsarchitektur wird eine Verbindung aufgebaut
- Meist ist nur die Verbindung auf der untersten Schicht real, die andren sind virtuell
## Dienste
- Jede Schicht stellt Dienste für die nächste höhere Schicht zur Verfügung (vertikale Kommunikation)
- Jede Schicht hat Zugriff auf Dienste der nächstniedrigeren Schicht
- Dienste werden über Schnittstellen an Dienstzugangspunkte (SAP = Service Access Point) zugänglich gemacht
- Innerhalb der Schichten sind die Instanzen (entities) die dienstbringenden Einheiten. Sie bedienen die Dienstzugangspunkte.

Eine Instanz darf mehrere SAPs bedienen und nutzen.
![[Pasted image 20251014070322.png]]
## Beispiel eines Dienstes
- Ein Dienst ist gekennzeichnet durch den Dienstnamen:
	- CONNECT für den Verbindungssaufbau
	- DATA für den Datentransfer
	- DISCONNECT für den Verbindungsabbau
- Der Dienstelementtyp kennzeichnet die Funktion des Dienstelements eines Dienstes. Es gibt vier Dienstelementtypen:
	- request: Anforderungen eines Dienstes (vom Nutzer)
	- indication: Anzeige am Partner-Dienstzugangspunkt
	- response: Antwort vom Partner-Dienstnutzer
	- confirm: Bestätigung beim Initiator

Beispiel eines Verbindungsaufbaus einer verbindungsorientierten Verbindung.
![[Pasted image 20251014070739.png]]
## Protokolle
Die Regeln, denen Kommunikation auf einer Schnittstelle folgen muss, die Angaben, welche Kommunikationselemente auf dieser Schnittstelle ausgetauscht werden können und die Beschreibungen der Repräsentation dieser Kommunikationselemente werden Protokoll genannt.

- Für jede Schicht der Kommunikationsarchitektur wird ein Protokoll definiert
- Es wird zwischen den Softwarekomponenten abgewickelt, die diese Schicht repräsentieren
- Diese Softwarekomponenten stellen über systeminterne Schnittstellen der darüberliegenden Schicht einen Dienst (Service) zur Verfügung.
## Dienste und Protokolle
![[Pasted image 20251014213158.png|500]]
## Vorteile der Schichtenarchitektur
- Unabhängige Entwicklung von Komponenten
- Austausch von Protokollen
- Standardisierung einzelner Komponenten
- Verbesserung der Kompatibilität zwischen heterogenen Systemen
- Bessere Wartbarkeit
- Erweiterbarkeit (Baukastenprinzip)
## Kriterien zur Schichtentrennung
- Nicht zu viele Schichten (Unübersichtlichkeit)
- Anzahl der Interaktionen über Schnittstellen minimieren
- Ähnliche Funktionen in eine Schicht
- Neue Protokolle und Redesign auf Software- und Hardwarebasis sollte möglich sein, ohne Schnittstellendienste zu ändern
- Berücksichtigung existierender Standards
- Abstraktionsgrad
