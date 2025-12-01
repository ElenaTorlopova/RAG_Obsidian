---
title: Projektbeschreibung
date: 2025-11-25
modified: 2025-11-25
authors:
  - "[[04-PERSONS/Patryk Gadziomski]]"
  - "[[Elena Torlopova]]"
tags:
  - master
  - th_wildau
  - artificial_inteligence
sources:
language: german
---
# Projektbeschreibung
Student:in: [[04-PERSONS/Patryk Gadziomski]]; Matr.: 5022632
Student:in: [[Elena Torlopova]]; Matr.: 50224937
Dozent:in: [[M. Eng. Janine Breßler]]
Datum: 27.11.2025
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
### Gliederung:
1. **Einleitung & Motivation**
	1. Kurzvorstellung der Studierenden & Dozentin
	2. Was ist Personal Knowledge Management (PKM)? Warum ist es relevant?
	3. Warum RAG? Warum Obsidian? Warum semantische Verlinkung?
	4. Ziel des Projekts: Intelligente, kontextbasierte Wissenserschließung aus einem personalen Vault
2. **Anwendungs- und Einsatzszenarien**
	1. Mögliche Anwendungsszenarien (In der Organisation, An der Universität, etc.)
3. **Technische Umsetzung**
	1. **Verwendete Technologien & Frameworks**
		1. Python als Hauptprogrammiersprache
		2. LangChain als Framework für RAG
		3. LLMs über GWDG-LLM-Service (z. B. Llama 3, Mistral, etc.)
	2. **Datenherkunft & -struktur**
		1. Obsidian-Vault als Datenquelle: Markdown-Dateien mit YAML-Metadaten
		2. Struktur: Tags, Hyperlinks, Frontmatter: semantische Vernetzung
		3. Datenbereinigung & Vorbereitung für RAG (Chunking, Embeddings) 
	3. **Architektur des RAG-Systems**
		1. Retrieval: Vectorstore + Embedding-Modelle (z. B. sentence-transformers)
		2. Generation: LLM mit Kontext aus Retrieval
		3. Optional: Kontextfilterung (thematisch) über Tags oder Metadaten
	4. **Trainingsprozess & Evaluierung**
		1. Kein klassisches Training: nur fine-tuning der Retrieval-Komponente (optional)
		2. Evaluierung: Relevanz der retrieved Dokumente, Qualität der generierten Antworten
		3. Metriken: BLEU, ROUGE, manuelle Bewertung durch Nutzer
4. **Herausforderungen & Lösungen**
	1. Probleme: Unstrukturierte Notizen, inkonsistente Tags, LLM-Halluzinationen
	2. Lösungen: Metadaten-Standardisierung, Prompt-Engineering, Reranking
	3. Limitationen: Kein „echtes Lernen“ des LLM, Abhängigkeit von GWDG-Service
5. **Vor- und Nachteile des RAG-Ansatzes**
	1. Vorteile
		1. Kein Training nötig: schnelle Implementierung
		2. Kontextreiche Antworten durch semantische Verknüpfung
		3. Datenschutz: Daten bleiben lokal (Obsidian-Vault), LLM-Service optional anonym
		4. Flexibel: Erweiterbar auf andere Notizsysteme
	2. Nachteile
		1. Abhängigkeit von LLM-Qualität & Verfügbarkeit
		2. Retrieval kann ungenau sein bei schlecht strukturierten Daten
		3. Keine „tiefe“ Wissensverarbeitung wie bei Fine-tuning
6. Vergleich mit konventionellen Methoden
	1. Suchmaschinen (z. B. Obsidian-Search): nur keywordbasiert, keine semantische Verknüpfung
	2. traditionelle KI-Modelle: benötigen Training, weniger flexibel
7. **Live-Demo**
	1. Demonstration: Natürlichsprachliche Frage eingeben → Retrieval → generierte Antwort
	2. Beispiel: „Erkläre mir den Zusammenhang zwischen Linked Data und PKM in meinem Vault“ oder "Was wurde in der letzten KI Vorlesung besprochen?"
	3. Optional: Filterung nach Themen über Tags
8. **Zusammenfassung & Ausblick**
	1. Kurzzusammenfassung der wichtigsten Punkte
	2. Mögliche Erweiterungen: Multi-User-Support, Integration in Obsidian-Plugins, Automatisches Tagging
	3. Persönliche Reflexion: Was hat funktioniert? Was würde ich anders machen?
