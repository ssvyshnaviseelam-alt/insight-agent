import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")
    SEARCH_API_KEY: str = os.getenv("SEARCH_API_KEY", "")


settings = Settings()