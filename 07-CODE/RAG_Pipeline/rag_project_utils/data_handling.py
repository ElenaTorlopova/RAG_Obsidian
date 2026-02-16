'''
author: Patryk Gadziomski
updateed: 16.02.2026
'''

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
import yaml
import re
from pathlib import Path
from datetime import date, datetime


def load_pdf_data(path):
    folder_path = Path(path)
    docs = []

    for file_path in folder_path.rglob('*.pdf'):
        loader = PyPDFLoader(str(file_path))
        doc = loader.load()
        docs.extend(doc)

    return docs


def clean_metadata(metadata: dict) -> dict:
    """
    Macht alle Metadata-Werte Chroma-kompatibel:
    - list → string mit [[...]]
    - date/datetime → ISO string
    - None → ""
    - alles andere → str()
    """
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


def load_md_data(path):
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


def create_vecstore(splits, embeddings, persist_directory):
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    return vectorstore

