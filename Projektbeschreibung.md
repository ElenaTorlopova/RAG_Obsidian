---
title: Project
date: 2025-11-25
modified: 2025-11-25
author:
  - "[[Patryk Gadziomski]]"
  - "[[Elena Torlopova]]"
tags:
  - master
  - th_wildau
  - artificial_inteligence
origin:
sources:
reused-for:
description: Beschreibung und Planung des Projektes für das Modul "Künstliche Intelligenz" im Studiengang Bibliotheksinformatik an der technischen Hochschule Wildau.
language: german
file-format: markdown (.md)
note-type: project
---
# Projektbeschreibung
Student:in: [[Patryk Gadziomski]]; Matr.: 5022632
Student:in: [[Elena Torlopova]]; Matr.: 50224937
Dozent:in: [[M. Eng. Janine Breßler]]
Datum: 12.11.2025
## Entwicklung eines RAG-basierten Wissenserschliessungssystems
Im Rahmen dieses Projekts wird ein [Retrieval Augmented Generation](https://de.wikipedia.org/wiki/Retrieval-Augmented_Generation) (RAG)-System entwickelt,
das auf einem gemeinsamen [Obsidian](https://obsidian.md/)-Vault basiert. Der Vault enthält akademische und berufliche Inhalte. Die Notizen sind durch Hyperlinks und Tags semantisch vernetz –
ein Ansatz, der den Prinzipien der [Linked Data](https://en.wikipedia.org/wiki/Linked_data) und des [Personal Knowledge Managements](https://de.wikipedia.org/wiki/Pers%C3%B6nliches_Wissensmanagement) (PKM) folgt.
#### Das Ziel des Projekts ist es, ein RAG-System zu implementieren, das:
1. Semantisch relevante Dokumente aus dem Vault extrahiert (Retrieval), basierend auf natürlichsprachlichen Anfragen
2. Zusammenhänge zwischen verlinkten Notizen nutzt, um kontextreiche Antworten zu generieren (Generation)
3. Daten nach Kontext trennen kann (akademisch vs. beruflich); optional über Tags, um die Relevanz zu steuern
### Motivation:
Persönliche Faszination für Personal Knowledge Management und die Strukturierung von Wissen
durch Verlinkung. Dazu kommt mein Interesse an der praktischen Anwendung moderner KI-
Methoden (RAG, LLMs) zur intelligenten Wissenserschließung.
### Technische Umsetzung:
• Programmiersprache: Python
• Framework: [LangChain](https://www.langchain.com/)
• LLMs: Mehrere Modelle werden über den [LLM-Service](https://kisski.gwdg.de/en/leistungen/2-02-llm-service/) der GWDG getestet
• Vault-Dokumente: Markdown Dateien mit Metadaten im YAML-Format
