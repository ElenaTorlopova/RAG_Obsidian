import os
from openai import OpenAI
from dotenv import load_dotenv
from langsmith import traceable
from rag_project_utils import data_handling as rag_dh
from rag_project_utils import data_processing as rag_dp
from rag_project_utils import retrieval_utils as rag_ru
from rag_project_utils import llm_utils as rag_llm
from rag_project_utils import prompt_handling as rag_ph

load_dotenv()

api_key = os.getenv('AI_API_KEY')
base_url = os.getenv('AI_API_ENDPOINT')
ai_model = 'qwen3-30b-a3b-instruct-2507'
embedding_model = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

file_path = r"C:\Users\gadzi\Documents\GitHub\RAG_Obsidian"

# OpenAI Client
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

system_prompt = rag_ph.read_system_prompt(r'C:\Users\gadzi\Documents\GitHub\RAG_Obsidian\07-CODE\RAG_Pipeline\prompts\system_prompt.txt')

question = """Was ist KI und wer könnte darüber mehr wissen?
WICHTIG:
- Nenne nur zusätzliche Daten, die explizit in den Metadaten genannt sind.
- Wenn keine passenden Metadaten vorhanden ist, sage: "Es ist keine konkrete Informationen bekannt."
"""

@traceable(run_type="chain", name="RAG Query")
def rag_query(vecstore, system_prompt, question: str, k: int = 3):
    retrieval = rag_ru.retrieve_docs(question, k, vecstore)

    docs = retrieval["raw_docs"]
    logged_docs = retrieval["documents"]

    context = "\n\n".join(doc.page_content for doc in docs)

    metadata_sets = {}

    for doc in docs:
        for field_key, value in doc.metadata.items():
            if field_key not in metadata_sets:
                metadata_sets[field_key] = set()
            
            metadata_sets[field_key].add(value)

    # Metadaten-Text zusammenstellen
    metadata_text = "\n".join([
        f"{field_key}: {', '.join(value.replace('[[', '').replace(']]', '') for value in values) if values else 'unbekannt'}"
        for field_key, values in metadata_sets.items()
    ])

    user_prompt = f"""
Kontext:
{context}

Metadaten:
{metadata_text}

Frage:
{question}

Antwort:
"""

    answer = rag_llm.llm_call(system_prompt, user_prompt, client, ai_model)

    return {
        "answer": answer,
        "metadata": {
            field_key: [value.replace('[[', '').replace(']]', '') for value in values]
            for field_key, values in metadata_sets.items()
        },
        "retrieved_documents": logged_docs
    }
 

if __name__ == '__main__':
    # -------- 1. Load & Split --------
    docs = rag_dh.load_md_data(file_path)
    splits = rag_dp.text_basic_splitter(docs)
    # -------- 2. Embeddings & Vector Store --------
    embeddings = rag_dp.create_embeddings(embedding_model)
    vecstore = rag_dh.create_vecstore(splits, embeddings, "./chroma_bim_db")
    # -------- 3. RAG Funktionen & 4. Frage --------
    answer = rag_query(vecstore, system_prompt, question)
