'''
author: Patryk Gadziomski
updateed: 16.02.2026
'''

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
# from marker.converters.pdf import PdfConverter
# from marker.models import create_model_dict
# from marker.config.parser import ConfigParser
import yaml
import re
from pathlib import Path
from datetime import date, datetime
from rag_project_utils import data_processing as rag_dp


def pypdf_basic_loader(path):
    folder_path = Path(path)
    docs = []

    for file_path in folder_path.rglob('*.pdf'):
        loader = PyMuPDFLoader(str(file_path))
        doc = loader.load()
        doc[0].page_content = doc[0].page_content.replace("\xad", "")
        doc[0].page_content = re.sub(r"\n{3,}", "\n\n", doc[0].page_content)
        docs.extend(doc)

    return docs


def pypdf_structure_loader(path):
    folder_path = Path(path)
    docs = []

    for file_path in folder_path.rglob('*.pdf'):
        # loader = PyPDFLoader(str(file_path))
        loader = PyMuPDFLoader(str(file_path))
        raw_docs = loader.load()
        full_text = "\n\n".join([d.page_content for d in raw_docs])
        paper_meta = raw_docs[0].metadata  # author, title, etc.
        markdown_text = rag_dp.text_to_markdown(full_text)
        # docs.extend()
        section_chunks = rag_dp.head_structure_splitter(markdown_text)
        final_chunks = rag_dp.text_structure_splitter(section_chunks)

        for i, chunk in enumerate(final_chunks):
            chunk.metadata.update({
                "source":      paper_meta.get("source", ""),
                "title":       paper_meta.get("title", ""),
                "author":      paper_meta.get("author", ""),
                "chunk_index": i,
                "total_chunks": len(final_chunks),
            })
        
        # for chunk in final_chunks[:3]:
        #     print("SECTION:", chunk.metadata.get("section", "—"))
        #     print("SUBSECTION:", chunk.metadata.get("subsection", "—"))
        #     print("TEXT:", chunk.page_content[:200])
        #     print("---")

        # for doc in raw_docs[:2]:
        #     print("=== PAGE", doc.metadata["page"], "===")
        #     print(repr(doc.page_content))
        #     print()

        # header_lines = [l for l in markdown_text.split("\n") if l.startswith("#")]
        # print("Erkannte Header:")
        # for h in header_lines:
        #     print(h)

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


class MarkerPDFLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    # def load(self) -> list[Document]:
    #     config = ConfigParser({})
    #     converter = PdfConverter(
    #         config=config.generate_config_dict(),
    #         artifact_dict=create_model_dict(),
    #     )
    #     rendered = converter(self.file_path)

    #     return [Document(
    #         page_content=rendered.markdown,
    #         metadata={
    #             "source": self.file_path,
    #         }
    #     )]

