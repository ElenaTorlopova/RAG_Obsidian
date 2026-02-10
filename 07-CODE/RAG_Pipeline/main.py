'''
title: RAG_Pipeline.main
author: Patryk Gadziomski
date updated: 30.01.2026
'''

from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_chroma import Chroma
from langchain_core.documents import Document
from pathlib import Path
from pathlib import Path
import re
import yaml
from datetime import date, datetime


def clean_md_data(content):
    content = content.replace('\t', ' ')
    content = re.sub(' +', ' ', content)
    return content

def clean_metadata(metadata):
    """Konvertiert alle Metadaten in Vector-Store-kompatible Formate"""
    cleaned = {}
    
    for key, value in metadata.items():
        if value is None:
            cleaned[key] = ''
            
        # Datum/Zeit Objekte → String
        elif isinstance(value, (date, datetime)):
            cleaned[key] = value.isoformat()  # z.B. "2026-01-30"
            
        # Listen → String
        elif isinstance(value, list):
            clean_items = []
            
            for item in value:
                item_str = str(item)
                clean_items.append(f'[[{item_str}]]')
            
            cleaned[key] = ', '.join(clean_items)        
        
        # Erlaubte Typen direkt übernehmen
        elif isinstance(value, (str, int, float, bool)):
            cleaned[key] = value
        
        # Alles andere → String konvertieren
        else:
            cleaned[key] = str(value)
    
    return cleaned

def parse_frontmatter(content):
    """Extrahiert YAML-Frontmatter aus Markdown"""
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    
    if yaml_match:
        yaml_content = yaml_match.group(1)
        markdown_content = yaml_match.group(2)
        
        try:
            metadata = yaml.safe_load(yaml_content) or {}
        except yaml.YAMLError as e:
            print(f"YAML-Fehler: {e}")
            metadata = {}
        
        return metadata, markdown_content.strip()
    else:
        return {}, content

def choose_llm_model(model_name, model_provider):
    model = init_chat_model(
        model=model_name,
        model_provider=model_provider,
        temperature=0.7,
        max_tokens=1024,
    )
    return model

def choose_embedding_model(embedding_name):
    embeddings = HuggingFaceEmbeddings(model_name=embedding_name)
    return embeddings

def create_db(embeddings):
    vector_store = Chroma(
        collection_name="rag-ld-collection",
        embedding_function=embeddings,
        persist_directory="./chorma-rag-ld-db",
    )
    return vector_store

def load_data(data_path):
    folder_path = Path(data_path)
    docs = []
    
    for file_path in folder_path.rglob('*.md'):
        with open(file_path, 'r', encoding='UTF-8') as f:
            content = f.read()
        
        yaml_metadata, page_content = parse_frontmatter(content)

        metadata = {
            'source': str(file_path),
            'filename': file_path.name,
            **yaml_metadata
        }
        
        # Metadaten bereinigen!
        cleaned_metadata = clean_metadata(metadata)
        
        doc = Document(
            page_content=page_content,
            metadata=cleaned_metadata
        )
        docs.append(doc)

    return docs

def document_splitter(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # chunk size (characters)
        chunk_overlap=200,  # chunk overlap (characters)
        add_start_index=True,  # track index in original document
    )
    all_splits = text_splitter.split_documents(docs)
    return all_splits

def indexing(all_splits, vector_store):
    batch_size = 1
    for i in range(0, len(all_splits), batch_size):
        batch = all_splits[i:i + batch_size]
        vector_store.add_documents(documents=batch)
        print(f"Processed batch {i//batch_size + 1}")

@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


if __name__ == '__main__':
    model = choose_llm_model("Qwen/Qwen2.5-0.5B-Instruct", 'huggingface')
    embeddings = choose_embedding_model("Qwen/Qwen3-Embedding-0.6B")
    vector_store = create_db(embeddings)
    docs = load_data(r'..\..\05-PROJECT-WIKI\BIM-Lectures\AI-Lecture-BIM')
    all_splits = document_splitter(docs)
    document_ids = vector_store.add_documents(documents=all_splits)
    indexing(all_splits, vector_store)
    tools = [retrieve_context]

    system_prompt = """Du bist ein hilfreicher Assistent, der Fragen basierend auf bereitgestellten Dokumenten beantwortet.
WICHTIG: 
- Gib bei deiner Antwort IMMER die Quelle(n) an, aus denen die Information stammt.
- Zitiere die Metadaten (filename, source, etc.) der verwendeten Dokumente.
- Format: "Laut [Quelle: filename] ..." oder am Ende "Quellen: ..."
"""

    agent = create_agent(model, tools, system_prompt=system_prompt)

    query = (
        "Was ist KI?"
    )

    for event in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode="values",
    ):
        event["messages"][-1].pretty_print()

# TODO:
# - Metadata output with the retrieval not the model
# - Try Graph RAG
