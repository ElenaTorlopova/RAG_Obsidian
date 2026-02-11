
**Retrieval Augmented Generation (RAG)** ist eine KI-Methode, die ein Large Language Model (LLM) mit einer effektiven Suchfunktion kombiniert. Diese Suche kann in Dokumentensammlungen, Datenbanken oder Knowledge Graphs erfolgen. Die Informationen für die Antworten stammen aus externen Quellen und nicht direkt aus dem LLM. Die Hauptaufgabe des LLM besteht darin, die Suchergebnisse zu verarbeiten. Dies geschieht im Kontext der ursprünglichen Anfrage, zum Beispiel durch Zusammenfassungen.

**„Durch RAG wird es möglich, mit eigenen Dokumenten bzw. Daten zu chatten.“**  (Honroth et al.)

Oft wird Retrieval Augmented Generation mit einer semantischen Suche umgesetzt. Textdokumente werden in kürzere Abschnitte aufgeteilt, durch das Embedding-Modell in Vektoren überführt und in einer Vektorendatenbank gespeichert. Auch die Suchphrase wird als Vektor abgebildet. Bei der semantischen Suche werden inhaltlich relevante Textabschnitte berücksichtigt, wortähnliche Treffer sind nicht wichtig. Da die Embedding-Modelle Vektoren erzeugen, die die Semantik eines Ausdrucks umfassen, ist es möglich, über eine Ähnlichkeitssuche die passenden Vektoren zu finden und damit die ähnlichsten Textabschnitte abzurufen.

**Vorteile:**
* Kein Training nötig
* Kontext der LLM-Eingabe wird spezifisch angepasst
* Steigerung der Verlässlichkeit des Generierens, KI-Halluzinationen werden reduziert
* Nutzen des Potenzials von Large Language Models für eigene (interne) Dokumente und Daten (ohne Fine-Tuning)
* Datenschutz – sensible Daten bleiben im eigenen Netzwerk

**Herausforderungen:**
* Aktualität und Vollständigkeit der internen Dokumente muss gewährleistet sein
* Daten müssen gut strukturiert sein, da schlechtstrukturierte Daten zu unrichtigen/ungenauen Ausgaben führen
* Qualität des Embeddings – bei der Auswahl eines Embedding-Modells ist auf spezifische Anforderungen zu achten, z.B. dass dieses mit deutschsprachigen Texten trainiert wurde, wenn deutschsprachige Datenquellen verwendet werden.
* Abhängigkeit von LLM-Qualität – bei widersprüchlichen Inhalten können die Berechnungen im LLM dazu tendieren, das Wissen aus den Trainingsdaten wiederzugeben und die Inhalte aus den Datenquellen zu ignorieren.

  
**Literatur**

**Honroth, Thorsten; Siebert, Julien; Kelbert, Patricia**: Retrieval Augmented Generation (RAG): Chatten mit den eigenen Daten. Blogbeitrag des Fraunhofer IESE, 13. Mai 2024
[https://www.iese.fraunhofer.de/blog/retrieval-augmented-generation-rag/](https://www.iese.fraunhofer.de/blog/retrieval-augmented-generation-rag/) (Zugriff am 16.12.2025)

**Linders, Jasper; Tomczak, Jakub M.**: Knowledge graph-extended retrieval augmented generation for question answering. In: Applied Intelligence, 55(2025), Article No. 1102
DOI 10.1007/s10489-025-06885-5

**Konferenz der unabhängigen Datenschutzaufsichtsbehörden des Bundes und der Länder**: Orientierungshilfe zu datenschutzrechtlichen Besonderheiten generativer KI-Systeme mit RAG-Methode: Version 1.0, Stand: Oktober 2025
[https://www.datenschutzkonferenz-online.de/media/oh/DSK_OH_RAG.pdf](https://www.datenschutzkonferenz-online.de/media/oh/DSK_OH_RAG.pdf) (Zugriff am 16.12.2025)