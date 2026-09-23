from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    answer: str = Field(description="The main answer to the user's question")
    confidence: float = Field(
        description="Confidence score between 0 and 1"
    )
    category: str = Field(
        description="Category of the user's question"
    )