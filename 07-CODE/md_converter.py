'''
Author: Patryk Gadziomski
Created: 01.12.2025
Modified: 01.12.2025
Version: 1.0
Desciption: This script converting different file types to the markdown type.

sources:
  - https://github.com/microsoft/markitdown
  - https://github.com/docling-project/docling
'''

## MarkItDown from Microsoft (Output not in MD format)
# from markitdown import MarkItDown

# md = MarkItDown()

# result = md.convert("05_Convolutional_Neural_Networks.pdf")
# print(result)

## Docling from IBM (Better output, but still needs postprocessing)
from docling.document_converter import DocumentConverter

source = "05_Convolutional_Neural_Networks.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
