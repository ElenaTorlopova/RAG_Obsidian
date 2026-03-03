---
rdf:type: schema:Course
dcterms:title: 06_Retrieval_Augmented_Generation
dcterms:contributor:
  - "[[M. Eng. Janine Breßler]]"
dcterms:created: 2026-01-30
dcterms:modified: 2026-01-30
dcterms:isPartOf:
  - "[[Artificial_Intelligence_BIM25-Lecture]]"
dcterms:references:
schem:language: german
schema:educationalProgramName: "[[M.Sc. Bibliotheksinformatik]]"
schema:educationalLevel: Master
schema:provider: "[[Technische Hochschule Wildau]]"
---
# Large Language Models
- Am 30. Oktober 2022 veröffentlichte OpenAI den KI-Chatbot ChatGPT
- Ein kleiner Schritt für OpenAI, ein großer Schritt für die Künstliche Intelligenz (und die Menschheit):
	- Beantwortung von Fragen
	- Unterstützung bei der Texterstellung
	- Interkation in natürlicher Sprache
	- Übersetzung u.v.m.
- Mit der explosionsartigen Nutzung und Verbreitung von Plattformen wie ChatGPT, wurden jedoch auch die Schwächen von Large Language Models (LLM) offengelegt
	- Wissenstand nut bis einem bestimmten Stichtag
		- Das Training eines LLMs ist ein kosten- und zeitintensiver Prozess
		- Es werden sehr viele Daten benötigt und mehrere Wochen oder Monate, um in LLM zu trainieren
		- Die Daten, mit denen da LLM trainiert wird, sind nicht mehr up-to-date:
		- GPT-4.1 veröffentlicht im April 2025, verfügt lediglich über Wissen bis zum 1. Juni 2024
	- Halluzinationen
		- Mit Zuversicht lügen -> Generierte Inhalte/Informationen, die zwar realistisch & plausible erscheinen, aber faktisch falsch sind
	- Wissensgrenzen
		- Die LLMs werden mit Daten, die öffentlich verfügbar sind, trainiert, z.B. dem offenen Internet
		- Interne Unternehmensdokumente, Kundeninformationen, Produktdokumente etc. stehen nicht öffentlich zur Verfügung und über solche Informationen kann das LLM auch eine Fragen beantworten

Beispiel: Anfrage vom 6. Januar 2026, Luke Littler ist am 3. Januar 2026 erneut Weltmeister im Darts geworden. Der Wissensstand der genutzt GPT-Version erstreckt sich bis ca. 2024.
# Retrieval Augmented Generation (RAG)
RAG stellt dem LLM die notwendigen bisher unbekannten (und externen) Informationen zur Verfügung für die Beantwortung der Anfrage, ohne, dass das Modell neu trainiert werden muss.

- Retrieval: Es werden relevante Informationen aus einer Datenquelle außerhalb des LLMs abgerufen
- Augmented: Die Eingabe (Prompt) in das LLM wird um diese externe Informationen erweitert
- Generation: Schließlich liefert das LLM mit Hilfe der externen Informationen ein genaueres Ergebnis

Zusammenfassung RAG:
- RAG stellt einen methodischen Ansatz dar, der die Leistungsfähigkeit des parametrischen Speichers eines LLM erweitert, indem ein explizierter, nicht-parametrischer Speicher integriert wird.
- Ein Retriever greift hierbei auf relevante Informationen aus diesem Speicher
## Grundprinzip eines RAG-Systems
Hauptziele von RAG:
- Das LLM ist durch RAG in der Lage:
	- mit aktuellen Informationen zu antworten
	- mit sachlich korrekten Informationen zu antworten
	- Aufmerksamkeit auf proprietäre Informationen zu legen
## Design eines RAG-Systems
Bei einem RAG-System gibt es zwei sogenannte Pipelines, die unterschiedliche Aufgaben haben:
- Indexing-Pipeline: Erstellt die externe Wissensbasis (nicht-parametrischer Speicher)
- Generation-Pipeline: Ermöglicht die Echtzeit-Internation mit einem Large Language Model

Gemeinsam bilden die Indexing- und die Generation-Pipeline das Grundgerüst eines RAG-Systems.
## Indexing-Pipeline
Damit eine konsolidierende Wissensbasis aufgebaut werden kann, werden in der Indexing-Pipeline 5 Stufen durchlaufen:
1. Mit zuvor identifizierten externen Quellen verbinden
2. Dokumente extrahieren und Text daraus parsen
3. Aufteilung langer Textabschnitte in kleinere, überschaubare Abschnitte
4. Konvertierung dieser kleinen Abschnitte in ein geeignetes Format
5. Speichern dieser Informationen

Die 5 Stufen werden durch 4 konkrete Komponenten umgesetzt:
1. Data-Loading: Verantwortlich für das Verbinden mit externen Quellen und das Extrahieren und Parsen von Informationen
	1. Verbinden mit der Datenquelle: Word-Dokumente, PDF- oder CSV-Dateien, HTML, etc. zum Beispiel durch Angabe der URL der HTML-Webseite
	2. Extraktion des Texts: Beispielweise der HTML-Code der verbundenen HTML-Webseite
	3. Metadaten überprüfen und aktualisieren: Sehr praktisch für den Retrieval-Prozess, wenn diese mitgeliefert werden, sollten diese auf Richtigkeit und Aktualität überprüft werden, ggf. müssen die Metadaten selbst hinzugefügt werden
	4. Daten bereinigen: Oft ist eine Bereinigung der Daten notwendig, bei HTML-Code wären dies beispielweise HTML-Tags oder auch Zeilenumbruchzeichen (\n), aber auch Duplikate oder eventuell sensible Informationen
2. Data-Splitting: Verantwortlich für das Zerlegen von langen Textabschnitten in kleinere besser handhabbare Teile genannt "Chunks"
	- Warum ist dies notwendig?
		- Die Anzahl der Tokens, mit dem ein LLM arbeiten kann, wird Kontextfenstergröße genannt und ist begrenzt
		- Umgehen des sogenannten Lost-in-the-Middle-Problems
		- Die Suchleistung des Retrievers verbessert sich in der Regel bei der Verwendung kleinerer Textsegmente um Vergleich zu größeren
	- Chunk-Prozess: Für den Chunking-Prozess müsse zwei Eigenschaften festgelegt werden:
		- die Art und Weise des Text-Splittings
		- Bemessung der Chunkgröße
	- Klassischer Ansatz: Fixed-Size Chunking
		- Text-Splitting anhand eines Zeichens
		- Chunkgröße wird durch Anzahl der Zeichen in einem Chuck definiert, ebenso die Anzahl der Zeichen für die Überlappung zwischen den Chunks
		- Weitere Ansätze: Spezialisiertes und semantisches Chunking

Chunking:
- Aufteilung des langen Textes in kompakte, aussagekräftige Einheiten (z.B. Sätze oder Absätze).
- Zusammenführen der kleinen Einheiten in größere Chunks bis eine spezifische Größe erreicht ist.
- Wenn ein neuer Chunk erstellt wird, wird ein Teil des vorherigen Chunks eingefügt. Diese Überlappung ist notwendig, um die Kontinuität des Kontexts zu gewährleisten.

3. Data Conversion: Verantwortlich für das Konvertieren der Text-Chunks in numerische Vektoren, genannt "Embedding"
	- Um mit nicht-numerischen Daten rechnen zu können, müssen diese zunächst in numerische Werte konvertiert werden
		- Word-Embedding, wie bspw. Word2Vec
		- Ziel eines Embeddings ist die Konvertierung von Wörtern, Sätzen oder Absätzen in n-dimensionale Vektoren
			- Ähnliche Wörter/Sätze/Absätze liegen im Vektorraum nah beieinander
			- Mit Hilfe der Cosinus-Ähnlichkeit z.B. bestimmbar
		- Es gibt eine Menge an vortrainierten Embeddings, diese sind in Abhängigkeit des Anwendungsszenarios und der Kosten zu Wählen
4. Data Storage: Speichert die Embeddings in nichtflüchtigen Speicher unter Verwendung von sogenannten "Vektordatenbanken"
	- Die erstellten Embeddings in Form von numerischen Vektoren werden in sogenannten Vektordatenbanken abgespeichert.
		- Datenbanken bieten die klassischen Features, wie Skalierbarkeit, Sicherheit, Versionierung, Verwaltung, etc.
		- In Abhängigkeit des Szenarios muss hier die Vektordatenbank ausgewählt werden, mögliche Kriterien:
			- Genauigkeit, Geschwindigkeit, Flexibilität, Speicher, Art des Zugriffs und ggf. Kosten
## Generation-Pipeline
Die Generation Pipeline ermöglicht kontextabhängige Interaktion in Echtzeit, die Pipeline wird in 5 Stufen durchlaufen:
1. Benutzer:in stellt eine Frage
2. Das System sucht nach relevanten Informationen
3. Die für die Eingabefrage relevanten Informationen werden abgerufen
4. Der Prompt mit der Benutzerfrage wird um die abgerufenen Informationen ergänzt
5. Das LLM antwortet mit einer kontextbezogenen Antwort

Die 5 Stufen werden durch 3 konkrete Komponenten umgesetzt:
1. Retriever: Verantwortlich für das Durchsuchen der Wissensbasis und das Abrufen der relevanten Informationen
	- Das Durchsuchen der Wissensbasis übernimmt der Retriever, er akzeptiert eine Anfrage als Eingabe und gibt eine Liste an gefundenen relevanten Chunks zurück
	- Dense-Retriever: Suche nach den semantisch ähnlichsten Chunks
		- Semantische Suche
	- Sparse-Retriever: Suche  anhand von übereinstimmenden Token in  der Benutzeranfrage (lexikalisch/tokenbasiert)
	- Hybrid-Retriever: Semantische und genaue Suche vereint
		- Sparse-Retrieval: Textähnlichkeit auf Tokenebene
		- Dense-Retrieval: Ähnlichkeit auf Bedeutungsebene
2. Prompt Management: Konstruiert finalen Prompt für LLM, indem der ursprüngliche Prompt mit den erhaltenen Informationen erweitert wird
	- Wie wird die ursprüngliche Benutzeranfrage und die erhaltenen Informationen durch den Retriever an das LLM weitergegeben werden, um die gewünschte Ausgabe zu erhalten (Prompt-Engineering)
		- Contextual Prompting
			- Dem finalen Prompt für das LLM wird bspw. die Information hinzugefügt, dass die Antwort des LLMs nur auf Basis des mit angegebenen Kontexts basieren soll
			- Die erhaltenen Inhalte aus den Chunks vom Retriever werden dem Prompt als Kontext entsprechend hinzugefügt
			- Dadurch fokussiert sich das LLM im nächsten Schritt beim Generieren der Antwort ausschließlich auf die mitgelieferten Informationen und nicht auf die Informationen aus dem internen Speicher (parametrischer Speicher)
		- Controlled Generation Prompting
			- Manchmal liegen die notwendigen Informationen zur Beantwortung einer Anfrage nicht im Kontext vor
			- In dem Fall steigt die Gefahr des Halluzinierens
			- Um dies zu verhindern, kann dem finalen Prompt die Information hinzugefügt werden, dass das LLM mit "Ich weiß es nicht" antworten soll, wenn die mitgelieferten Informationen nicht die richtige Antwort auf die Anfrage enthalten
		- Few-Shot-Prompting
			- Wenn die Antwort des LLMs in einem bestimmten Format oder Stil erfolgen soll, dann kann dies ebenfalls im finalen Prompt angegeben werden
			- Besonders effektiv erfolgt dies durch Angabe von ein paar Beispielen wie eine Antwort aussehen soll
		- Chain of Thoughts Prompting
			- Hier wird das LLM angewiesen seine "Gedankengänge" Schritt für Schritt dazulegen
			- So wird das LLM angewiesen eine Abfolge von logischen Zwischenschritten zu generieren, bevor die endgültige Antwort geliefert wird
			- Gerade bei komplexen oder mehrstufigen Aufgaben sinnvoll (logische Schlussfolgerungen, Planungs- oder Strategiefragen)
3. LLM: Generiert die finale Antwort. Ein RAG-System kann aus mehr als einem LLM bestehen
	- Die Generierung der Antwort ist das letzte Modul in der Generation-Pipeline
		- Für die Auswahl des zu verwendenden Modells sollten die folgenden Eigenschaften betrachtet werden:
			- Wie wurden die Modelle trainiert?
				- Original vs. Fine-Tuned Modelle
				- Alle modernen LLMs sind darauf trainiert, das nächste Token in einer Sequenz zu bestimmen (Pretrained-Model)
				- Sogenannte Supervised Fine-Tuning Modelle sind eine Weiterentwicklung der Large Language Models
					- Dadurch lernt das Modell bspw. durch Beispieldialoge, wie es ragen nach bestimmten Kriterien beantwortet etc. (Supervised Learning)
					- Hier gibt es unterschiedliche Fine-Tuning-Ziele, die, je nach Anwendungsfall, mehr oder weniger geeignet sind
						- Technisch juristische Beratung
						- Kreative Ideengenerierung
						- etc.
			- Wie kann auf sie zugegriffen werden?
				- Open Source vs. Proprietäre Modelle
				- Open Source Modele
					- Anpassungen möglich
					- Flexibilität bei der Bereitstellung
					- Datensicherheit und Datenschutz
					- Llama (Meta) und Mistral
				- Proprietäre Modelle
					- In der Regel einfacher zu nutzen
					- Regelmäßige Updates und Support
					- GPT (OpenAI), Claude (Anthropic), Gemini (Google) und Command R (Chore)
			- Wie groß sind die Modelle?
				- Die Größe eines Modells wird typischer Weise durch die Anzahl der Parameter angegeben
				- Große Modelle haben Milliarden, sogar Billionen Parameter, dies hat Einfluss auf
					- Leistung der logischen "Denkfähigkeit"
					- Sprachverständnis
					- Wissen
					- Inferenzzeit
					- Ressourcenverbrauch
					- Komplexität der Bereitstellung