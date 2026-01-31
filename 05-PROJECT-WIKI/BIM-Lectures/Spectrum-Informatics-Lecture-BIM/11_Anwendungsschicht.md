---
title: 11_Anwendungsschicht
date: 2025-10-13
modified: 2025-12-25
tags:
  - master
origin: "[[Spektrum_Informatik]]"
sources:
  - "[[Prof. Birgit Wilkes]]"
  - "[[11_Anwendungsschicht.pdf]]"
language: german
note-type: lecture
file-format: markdown (.md)
relations:
  - "[[Technische Hochschule Wildau]]"
---
![[Pasted image 20251225190643.png]]
## Dienste in der Anwendungsschicht
- Computersysteme fernbedienen über das Internet (telnet)
- Fernbedienen mit verschlüsselter Datenübertragung (ssh=secure shell)
- Dateien übertragen im Internet (ftp)
- Elektronische Post im Internet (e-mail)
- Nachrichtengruppen (newsgroups)
- Plaudern im Internet (chat)
- WWW (word wide web)
- Alle Dienste der Anwendungsschicht benutzen eigene - auf TCP/IP aufgesetzte - Protokolle, um ihre Dienstleistungen zu erbringen

![[Pasted image 20251225191013.png]]
## Telnet
### Computersysteme fernbedienen (telnet)
- Entfernte Computersysteme fernsteuern
- Das eigene Computersystem arbeitet dabei wie ein an ein zentrales Computersystem angeschlossenes Terminal
- Änderungen auf dem entfernten Computersystem können direkt vorgenommen werden
## Secure Shell
### Sichere Alternative: Secure Shell (ssh)
- Es dient ebenfalls zur Fernbedienung
- Zwischen Transport- und Anwendungsschicht wird ein Security Layer eingefügt, der alle Daten verschlüsselt überträgt

![[Pasted image 20251225191313.png]]
## FTP
### Dateien übertragen im Internet (ftp)

![[Pasted image 20251225191351.png]]
## E-Mail
### Elektronische Post im Internet
- Protokoll: SMTP (simple mail transport protocol)
	- Über entsprechende SMLTP-Server werden e-Mails an den Zielrechner weitergeleitet
- Email-Adresse
	- Auf dem Server des Providers existiert ein elektronisches Postfach (mailbox)
	- Die für diese Adresse eintreffende Post wird in diesem Postfach - es handelt sich dabei um eine Datei - gespeichert
	- Um die eingegangene Post zu lesen, müssen mit einer Email-Software die Verbindung zu dieser Datei hergestellt und die Daten in das eigene Computersystem übertragen werden (Post Office Protocol = POP)
### Email-Charakteristika
- Das Zielcomputersystem:
	- nimmt die Post ohne Authentifizierung an
	- hält für den Empfänger in einem besonderen Bereich die Post bereit
- Der E-mail-Dienst erlaubt den:
	- schnellen,
	- asynchronen
	- informellen Austausch von (schriftlichen) Nachrichten
- Der geographische Ort des Empfängers spielt keine Rolle mehr
## Newsgroups
- Newsgroups ermöglichen es, Computer-Konferenzen und -Diskussionen abzuhalten
- Asynchrone Kommunikation
- Schwarze Bretter
- Zu verschiedenen Themengebieten gibt es Diskussionsforen
	- Jeder Teilnehmer kann auf die bisher eingebrachten Beiträge eines Forums zugreifen und bei Bedarf eigene hinzufügen
- Es ergeben sich threads (Diskussionsfäden)
## Chat
- Unterhaltung mit anderen Benutzern in nahezu Echtzeit
- Internet Relay Chat (IRC)
	- Weltumfassendes, textorientiertes Kommunikationswerkzeug
	- Es gibt unterschiedliche Kanäle (channels), die sich um jeweils ein Thema drehen
	- Zugang mit speziellen Programmen oder z.B. über http://www.ircchat.de (webchat.de)
- kanalunabhängige Chats über WWW
## TCP/IP Ports
- Jedem Anwendungsprozess, der über TCP mit einem anderen Anwendungsprozess kommuniziert, ist ein abstrakter Zielpunkt in Form einer Portnummer zugewiesen
- Die Protokollinstanzen verwenden die Nummer des Zielports, um ankommende Daten den jeweiligen Zielprozessen zuzuordnen
- Die ersten 1024 Portnummern bezeichnet man als Well-Known Ports. Bei ihnen ist eine feste Zuordnung zu einem Dienst festgelegt
- Die Erstellung einer Verbindung erfolgt in der Regel über Well-Known Ports
- Spricht ein Browser einen Web-Server an, tut er das auf dem Port 80
- Beim Versenden einer Mail wird der Mail-Server über Port 25 angesprochen
- Wird eine Mail abgefragt, so erfolgt dies über den Port 110
- Bei der Abfrage eines News-Servers wird Port 119 genutzt
- Auch bei der Kommunikation über UDP werden Ports als abstrakte Zielpunkte genutzt
- Listen der TCP- und UDP-Ports findet man im Internet
## Well-Knows Ports
Ein Überblick über die bekanntesten Well-Known TCP-Ports:

![[Pasted image 20251225193033.png]]
