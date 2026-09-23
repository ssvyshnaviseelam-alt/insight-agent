from langgraph.graph import MessagesState


class InsightMessageState(MessagesState):
    user_id: str
    session_id: str