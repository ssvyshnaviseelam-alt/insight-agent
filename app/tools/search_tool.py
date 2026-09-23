from langchain_core.tools import tool
from tavily import TavilyClient

from app.config import settings


@tool
def web_search(query: str) -> str:
    """
    Search the web for current or external information.
    """

    client = TavilyClient(
        api_key=settings.SEARCH_API_KEY
    )

    response = client.search(
        query=query,
        max_results=3,
    )

    results = []

    for item in response.get("results", []):
        results.append(
            f"Title: {item.get('title', '')}\n"
            f"Content: {item.get('content', '')}\n"
            f"URL: {item.get('url', '')}"
        )

    if not results:
        return "No web search results found."

    return "\n\n---\n\n".join(results)