from typing import TypedDict


class AgentGraphState(TypedDict):
    question: str
    user_id: str
    session_id: str
    decision: str
    tool_input: str
    tool_result: str
    answer: str
    memory_context: str
    tool_used: str
    sources: list