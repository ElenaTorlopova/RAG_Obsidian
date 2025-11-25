---
title: Project
date: 2025-10-13
modified: 2025-10-18
author: "[[Patryk Gadziomski]]"
tags:
  - master
  - ai
  - th_wildau
origin: "[[KÜNSTLICHE_INTELLIGENZ.base]]"
sources:
  - "[[01_Intro.pdf]]"
reused-for:
description: Beschreibung und Planung des Projektes für das Modul "Künstliche Intelligenz" im Studiengang Bibliotheksinformatik an der technischen Hochschule Wildau.
language: german
file-format: markdown (.md)
note-type: project
---
# Projektbeschreibung
Student:in: [[Patryk Gadziomski]]; Matr.: 5022632
Student:in: [[Elena Torlopova]]; Matr.: XX
Dozent:in: [[M. Eng. Janine Breßler]]
Datum: 12.11.2025
## Entwicklung eines RAG-basierten Wissenserschliessungssystems
Im Rahmen dieses Projekts wird ein [Retrieval Augmented Generation](https://de.wikipedia.org/wiki/Retrieval-Augmented_Generation) (RAG)-System entwickelt,
das auf einem persönlichen [Obsidian](https://obsidian.md/)-Vault basiert. Der Vault enthält persönliche und
akademische/berufliche Inhalte. Die Notizen sind durch Hyperlinks und Tags semantisch vernetz –
ein Ansatz, der den Prinzipien der [Linked Data](https://en.wikipedia.org/wiki/Linked_data) und des [Personal Knowledge Managements](https://de.wikipedia.org/wiki/Pers%C3%B6nliches_Wissensmanagement) (PKM)
folgt.
#### Das Ziel des Projekts ist es, ein RAG-System zu implementieren, das:
1. Semantisch relevante Dokumente aus dem Vault extrahiert (Retrieval), basierend auf natürlichsprachlichen Anfragen
2. Zusammenhänge zwischen verlinkten Notizen nutzt, um kontextreiche Antworten zu generieren (Generation)
3. Daten nach Kontext trennen kann (persönlich vs. akademisch/beruflich); optional über Tags, um die Relevanz und Privatsphäre zu steuern
### Motivation:
Persönliche Faszination für Personal Knowledge Management und die Strukturierung von Wissen
durch Verlinkung. Dazu kommt mein Interesse an der praktischen Anwendung moderner KI-
Methoden (RAG, LLMs) zur intelligenten Wissenserschließung.
### Technische Umsetzung:
• Programmiersprache: Python
• Framework: [LangChain](https://www.langchain.com/)
• LLMs: Mehrere Modelle werden über den [LLM-Service](https://kisski.gwdg.de/en/leistungen/2-02-llm-service/) der GWDG getestet
• Vault-Dokumente: Markdown Dateien mit Metadaten im YAML-Format
