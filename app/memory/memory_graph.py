import sqlite3

from langgraph.graph import StateGraph, START
from langgraph.graph.message import MessagesState
from langgraph.checkpoint.sqlite import SqliteSaver

from app.agents.llm import get_llm
from app.memory.memory_relevance import get_relevant_memories


class UserMemoryState(MessagesState):
    user_id: str
    session_id: str


def extract_text(content):
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        return "".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

    return str(content)


def get_memory_context(
    user_id: str,
    question: str
):
    memories = get_relevant_memories(
        user_id,
        question
    )

    if not memories:
        return "No relevant long-term memories."

    lines = []

    for memory in memories:
        lines.append(
            f"- {memory['key']}: {memory['value']}"
        )

    return "\n".join(lines)


def chatbot_node(state):

    llm = get_llm()

    question = extract_text(
        state["messages"][-1].content
    )

    long_term_memory = get_memory_context(
        state["user_id"],
        question
    )

    prompt = f"""
You are InsightAgent.

Use the conversation history and relevant
long-term user memories to answer the user.

Relevant long-term memories:
{long_term_memory}

Conversation:
{state["messages"]}

Rules:
1. Use conversation history when relevant.
2. Use long-term memories only when relevant.
3. Do not mention internal memory storage.
4. Do not invent memories.
5. Answer clearly and naturally.
"""

    response = llm.invoke(prompt)

    return {
        "messages": [response]
    }


def create_memory_graph():

    graph = StateGraph(
        UserMemoryState
    )

    graph.add_node(
        "chatbot",
        chatbot_node
    )

    graph.add_edge(
        START,
        "chatbot"
    )

    connection = sqlite3.connect(
        "data/memory.db",
        check_same_thread=False
    )

    checkpointer = SqliteSaver(
        connection
    )

    return graph.compile(
        checkpointer=checkpointer
    )