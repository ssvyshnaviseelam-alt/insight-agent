from app.rag.vector_store import load_vector_store


def retrieve_documents_with_scores(
    query,
    k=3,
    score_threshold=1.0,
):
    vector_store = load_vector_store()

    results = vector_store.similarity_search_with_score(
        query,
        k=k,
    )

    filtered_results = [
        (document, score)
        for document, score in results
        if score <= score_threshold
    ]

    return filtered_results