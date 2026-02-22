'''
author: Patryk Gadziomski
updated: 16.02.2026
'''

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import re

# SECTION_PATTERNS = [
#     r"^(Abstract)$",
#     r"^(\d+\.?\s+Introduction.*)$",
#     r"^(\d+\.?\s+Related Work.*)$",
#     r"^(\d+\.?\s+Background.*)$",
#     r"^(\d+\.?\s+Method(?:ology|s)?.*)$",
#     r"^(\d+\.?\s+Experiment(?:s|al Setup)?.*)$",
#     r"^(\d+\.?\s+Results?.*)$",
#     r"^(\d+\.?\s+Discussion.*)$",
#     r"^(\d+\.?\s+Conclusion.*)$",
#     r"^(\d+\.?\s+References.*)$",
#     r"^(\d+\.\s+.{3,50})$",        # generische nummerierte Section
# ]

# headers_to_split_on = [
#     ("#",  "section_h1"),
#     ("##", "section"),       # Hauptsections: Abstract, Introduction, ...
#     ("###","subsection"),    # Subsections: 2.1, 3.2, ...
# ]

# def text_to_markdown(text: str) -> str:
#     lines = text.split("\n")
#     md_lines = []

#     for line in lines:
#         stripped = line.strip()

#         # Subsection: "1.1. Titel" oder "1.1 Titel"
#         if re.match(r"^\d+\.\d+\.?\s+[A-Z].{3,60}$", stripped):
#             md_lines.append(f"### {stripped}")

#         # Hauptsection: "1. Introduction" etc.
#         elif re.match(r"^\d+\.?\s+[A-Z][a-zA-Z\s]{3,50}$", stripped):
#             md_lines.append(f"## {stripped}")

#         # Abstract/Keywords Block – als H2 markieren
#         elif re.match(r"^(Abstract|ABSTRACT|A\s*B\s*S\s*T\s*R\s*A\s*C\s*T)$", stripped):
#             md_lines.append(f"## Abstract")

#         # Alles andere normal lassen
#         else:
#             md_lines.append(line)

#     return "\n".join(md_lines)


# def head_structure_splitter(markdown_text):
#     header_splitter = MarkdownHeaderTextSplitter(
#         headers_to_split_on=headers_to_split_on,
#         strip_headers=False   # Header im Chunk-Text behalten für Kontext
#     )
#     section_chunks = header_splitter.split_text(markdown_text)
#     return section_chunks


def text_structure_splitter(section_chunks):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " "],
    )
    final_chunks = text_splitter.split_documents(section_chunks)
    return final_chunks


def text_basic_splitter(docs):
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
