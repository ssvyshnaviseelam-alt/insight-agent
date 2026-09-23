from langchain_core.documents import Document


def inspect_document(document: Document):
    print("\nDocument Object")
    print("----------------")

    print("Type:")
    print(type(document).__name__)

    print("\nContent:")
    print(document.page_content[:500])

    print("\nMetadata:")
    print(document.metadata)