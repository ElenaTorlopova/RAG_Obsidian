'''
author: Patryk Gadziomski
updated: 16.02.2026
'''

from langsmith import traceable

@traceable(run_type="retriever", name="Chroma Retriever")
def retrieve_docs(question: str, k: int, vectorstore):
    docs = vectorstore.similarity_search(question, k=k)

    logged_docs = [
        {
            "content": doc.page_content,
            "metadata": doc.metadata
        }
        for doc in docs
    ]

    return {
        "documents": logged_docs,
        "raw_docs": docs
    }

@traceable(run_type="retriever", name="Chroma Retriever")
def retrieve_docs_V2(question: str, k: int, vectorstore, keyword_weight: float = 0.3):
    # 1. Standard-Semantische Suche
    raw_docs = vectorstore.similarity_search(question, k=k * 2)  # Mehr Docs holen für Re-Ranking

    # 2. Re-Ranking mit Keywords (wenn vorhanden)
    scored_docs = []
    for doc in raw_docs:
        score = 1.0  # Basis-Score

        # Wenn Keywords vorhanden → Boost, wenn sie in der Frage vorkommen
        if "keywords" in doc.metadata and doc.metadata["keywords"]:
            keywords = [k.lower().strip() for k in doc.metadata["keywords"]]
            question_lower = question.lower()

            # Zähle Übereinstimmungen
            keyword_matches = sum(1 for kw in keywords if kw in question_lower)
            if keyword_matches > 0:
                score += keyword_weight * keyword_matches  # z. B. +0.3 pro Match

        scored_docs.append((score, doc))

    # 3. Sortiere nach Score absteigend
    scored_docs.sort(key=lambda x: x[0], reverse=True)

    # 4. Nimm die Top-k
    top_docs = [doc for _, doc in scored_docs[:k]]

    logged_docs = [
        {
            "content": doc.page_content,
            "metadata": doc.metadata,
            # Optional: Score mitspeichern
            "retrieval_score": next(s for s, d in scored_docs if d == doc)
        }
        for doc in top_docs
    ]

    return {
        "documents": logged_docs,
        "raw_docs": top_docs
    }
