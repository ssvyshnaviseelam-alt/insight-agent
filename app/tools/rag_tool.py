from langchain_core.tools import tool

from app.rag.rag_pipeline import ask_rag


@tool
def search_knowledge_base(question: str) -> dict:
    """
    Search the InsightAgent knowledge base and return
    the answer along with the source documents.
    """

    result = ask_rag(
        question,
        k=3,
        score_threshold=1.0,
    )

    return {
        "answer": result.get(
            "answer",
            "No answer returned."
        ),
        "sources": result.get(
            "sources",
            []
        ),
    }