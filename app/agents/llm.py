from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import settings


def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=settings.LLM_API_KEY
        
    )