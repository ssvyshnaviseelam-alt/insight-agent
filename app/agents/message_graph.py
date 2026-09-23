from langgraph.graph import StateGraph, START, END

from app.agents.message_state import InsightMessageState
from app.agents.llm import get_llm


def chatbot_node(state):
    llm = get_llm()

    response = llm.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


def create_message_graph():

    graph = StateGraph(InsightMessageState)

    graph.add_node(
        "chatbot",
        chatbot_node
    )

    graph.add_edge(
        START,
        "chatbot"
    )

    graph.add_edge(
        "chatbot",
        END
    )

    return graph.compile()