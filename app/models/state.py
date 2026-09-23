from typing import TypedDict


class AgentState(TypedDict):
    user_id: str
    session_id: str
    question: str
    answer: str