from app.rag.retriever import retrieve_documents_with_scores
from app.rag.rag_chain import create_rag_chain


NO_INFORMATION_MESSAGE = (
    "I don't have enough information in the provided documents."
)


def ask_rag(
    question: str,
    k: int = 3,
    score_threshold: float = 1.0,
):
    results = retrieve_documents_with_scores(
        question,
        k=k,
        score_threshold=score_threshold,
    )

    if not results:
        return {
            "question": question,
            "answer": NO_INFORMATION_MESSAGE,
            "sources": [],
        }

    context_parts = []

    for index, (document, score) in enumerate(
        results,
        start=1,
    ):
        source = document.metadata.get(
            "source",
            "Unknown",
        )

        page = document.metadata.get(
            "page",
            "Unknown",
        )

        chunk_id = document.metadata.get(
            "chunk_id",
            "Unknown",
        )

        context_parts.append(
            f"[Source {index}]\n"
            f"Document: {source}\n"
            f"Page: {page}\n"
            f"Chunk ID: {chunk_id}\n"
            f"Content:\n"
            f"{document.page_content}"
        )

    context = "\n\n---\n\n".join(context_parts)

    chain = create_rag_chain()

    answer = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    sources = []

    for index, (document, score) in enumerate(
        results,
        start=1,
    ):
        sources.append(
            {
                "source_id": index,
                "source": document.metadata.get(
                    "source"
                ),
                "page": document.metadata.get(
                    "page"
                ),
                "chunk_id": document.metadata.get(
                    "chunk_id"
                ),
                "score": float(score),
            }
        )

    return {
        "question": question,
        "answer": answer,
        "sources": sources,
    }