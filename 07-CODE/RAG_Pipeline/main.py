import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langsmith import traceable
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import yaml
import re
from pathlib import Path

load_dotenv()

# KISSKI Setup
api_key = os.getenv('AI_API_KEY')
base_url = os.getenv('AI_API_ENDPOINT')
ai_model = 'qwen3-30b-a3b-instruct-2507'

file_path = r"C:\Users\gadzi\Documents\GitHub\RAG_Obsidian" #\05-PROJECT-WIKI\BIM-Lectures"

# OpenAI Client
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

question = """Was ist KI und wer könnte darüber mehr wissen? In welchem Studiengang kommt das Thema vor?
WICHTIG:
- Nenne nur zusätzliche Daten, die explizit in den Metadaten genannt sind.
- Wenn keine passenden Metadaten vorhanden ist, sage: "Es ist keine konkrete Informationen bekannt."
"""

# question = "Wann haben Elena und ich (Patryk) die Präsentation und die Folien aufgeteilt?"

# -------- Markdown + YAML Loader --------

def clean_metadata(metadata: dict) -> dict:
    """
    Macht alle Metadata-Werte Chroma-kompatibel:
    - list → string mit [[...]]
    - date/datetime → ISO string
    - None → ""
    - alles andere → str()
    """
    from datetime import date, datetime

    cleaned = {}

    for key, value in metadata.items():

        # None → leerer String
        if value is None:
            cleaned[key] = ""

        # Datum / Zeit → ISO-String
        elif isinstance(value, (date, datetime)):
            cleaned[key] = value.isoformat()

        # LISTEN → STRING mit [[...]]
        elif isinstance(value, list):
            wrapped_items = []
            for item in value:
                wrapped_items.append(f"{str(item)}")
            cleaned[key] = ", ".join(wrapped_items)

        # Erlaubte Primitive direkt
        elif isinstance(value, (str, int, float, bool)):
            cleaned[key] = value

        # Alles andere → String
        else:
            cleaned[key] = str(value)

    return cleaned

def parse_markdown_with_yaml(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if match:
        metadata = yaml.safe_load(match.group(1)) or {}
        body = match.group(2)
        return metadata, body.strip()
    return {}, content

def load_markdown(path):
    folder_path = Path(path)
    docs = []
    for file_path in folder_path.rglob('*.md'):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        metadata, text = parse_markdown_with_yaml(content)

        metadata.update({
            "source": file_path,
            "filename": Path(file_path).name,
            "filetype": "markdown"
        })

        cleaned_metadata = clean_metadata(metadata)

        doc = Document(
            page_content=text,
            metadata=cleaned_metadata
        )

        docs.append(doc)

    return docs

def text_splitter(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(docs)
    return splits

def create_embeddings(model_name):
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return embeddings

def create_vecstore(splits, embeddings, persist_directory):
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    return vectorstore

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

@traceable(run_type="llm", name="KISSKI LLM Call")
def llm_call(system_prompt: str, user_prompt: str):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model=ai_model,
        temperature=0,
        max_tokens=2000
    )
    return response.choices[0].message.content

@traceable(run_type="chain", name="RAG Query")
def rag_query(vecstore, question: str, k: int = 3):
    retrieval = retrieve_docs(question, k, vecstore)

    docs = retrieval["raw_docs"]
    logged_docs = retrieval["documents"]

    # Kontext (Inhalt)
    context = "\n\n".join(doc.page_content for doc in docs)

    # Dictionary für die gesammelten Metadaten (dynamisch)
    metadata_sets = {}

    # Metadaten extrahieren
    for doc in docs:
        for field_key, value in doc.metadata.items():
            # Nur Werte mit doppelten eckigen Klammern akzeptieren
            # if value and isinstance(value, str) and value.startswith("[[") and value.endswith("]]"):
                # Set für dieses Feld erstellen, falls noch nicht vorhanden
            if field_key not in metadata_sets:
                metadata_sets[field_key] = set()
            
            metadata_sets[field_key].add(value)

    system_prompt = """Du bist ein fachlicher Assistent.
Beantworte die Frage anhand des Kontexts.
Nutze Metadaten explizit, wenn nach zusätzlichen Informationen oder Expertise gefragt wird.
Antworte sachlich und präzise.
"""

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

    answer = llm_call(system_prompt, user_prompt)

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
    docs = load_markdown(file_path)
    splits = text_splitter(docs)
    # -------- 2. Embeddings & Vector Store --------
    embeddings = create_embeddings("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    vecstore = create_vecstore(splits, embeddings, "./chroma_md_db")
    # -------- 3. RAG Funktionen & 4. Frage --------
    answer = rag_query(vecstore, question)
