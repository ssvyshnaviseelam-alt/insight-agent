from pydantic import BaseModel, Field


class MemoryItem(BaseModel):
    memory_type: str = Field(
        description="Type of memory, such as preference or personal_info"
    )

    key: str = Field(
        description="Short name identifying the memory"
    )

    value: str = Field(
        description="The actual information to remember"
    )