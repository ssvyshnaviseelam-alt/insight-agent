import re

from langchain_core.documents import Document


def clean_document(document: Document) -> Document:
    text = document.page_content

    # Replace multiple spaces with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return Document(
        page_content=text,
        metadata=document.metadata,
    )