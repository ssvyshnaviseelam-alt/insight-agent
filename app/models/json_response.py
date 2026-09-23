from typing import TypedDict


class JSONResponse(TypedDict):
    answer: str
    category: str
    confidence: float