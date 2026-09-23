from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import settings


def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=settings.LLM_API_KEY,
    )