from pathlib import Path

from langchain_community.vectorstores import FAISS

from app.rag.embeddings import get_embeddings


VECTORSTORE_PATH = "data/vectorstore"


def create_vector_store(chunks):
    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings,
    )

    return vector_store


def save_vector_store(vector_store):
    Path(VECTORSTORE_PATH).mkdir(
        parents=True,
        exist_ok=True,
    )

    vector_store.save_local(VECTORSTORE_PATH)

    print("FAISS vector store saved successfully!")


def load_vector_store():
    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )

    return vector_store


def search_vector_store(vector_store, query, k=3):
    results = vector_store.similarity_search(
        query,
        k=k,
    )

    return results