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

file_path = r"C:\Users\gadzi\Documents\GitHub\RAG_Obsidian\05-PROJECT-WIKI\BIM-Lectures"

# OpenAI Client
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

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
    for file_path in folder_path.rglob('*.md'): # Das funcktioniert nicht
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

    return [doc]

# -------- 1. Load & Split --------

docs = load_markdown(file_path)
print('1. Data Loaded!')

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = text_splitter.split_documents(docs)

# -------- 2. Embeddings & Vector Store --------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory="./chroma_md_db"
)
print("2. Data indexed!")

# -------- 3. RAG Funktionen --------

@traceable(run_type="retriever", name="Chroma Retriever")
def retrieve_docs(question: str, k: int):
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
def rag_query(question: str, k: int = 3):
    retrieval = retrieve_docs(question, k)

    docs = retrieval["raw_docs"]
    logged_docs = retrieval["documents"]

    # Kontext (Inhalt)
    context = "\n\n".join(doc.page_content for doc in docs)

    # Metadaten extrahieren (z. B. author)
    authors = set()
    for doc in docs:
        author = doc.metadata.get("dcterms:contributor")
        if author:
            authors.add(author)

    authors_text = ", ".join(authors) if authors else "unbekannt"

    system_prompt = """Du bist ein fachlicher Assistent.
Beantworte die Frage anhand des Kontexts.
Nutze Metadaten explizit, wenn nach Personen, Quellen oder Expertise gefragt wird.
Antworte sachlich und präzise.
"""

    user_prompt = f"""
Kontext:
{context}

Bekannte Expert:innen aus den Metadaten:
{authors_text}

Frage:
{question}

Antwort:
"""

    answer = llm_call(system_prompt, user_prompt)

    return {
        "answer": answer,
        "experts": list(authors),
        "retrieved_documents": logged_docs
    }

# -------- 4. Frage --------

question = """Was ist KI und wer könnte darüber mehr wissen?
WICHTIG:
- Nenne nur Personen, die explizit in den Metadaten genannt sind.
- Wenn keine Person vorhanden ist, sage: "Es ist keine konkrete Ansprechperson bekannt."
"""

answer = rag_query(question)
