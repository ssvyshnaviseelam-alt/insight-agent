import sqlite3

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

from app.agents.graph_state import AgentGraphState
from app.agents.graph_nodes import (
    agent_node,
    calculator_node,
    rag_node,
    web_search_node,
    mcp_node,
    final_answer_node,
    route_decision,
)


MEMORY_DB_PATH = "data/memory.db"


def create_agent_graph():

    graph = StateGraph(AgentGraphState)

    graph.add_node(
        "agent",
        agent_node,
    )

    graph.add_node(
        "calculator",
        calculator_node,
    )

    graph.add_node(
        "rag",
        rag_node,
    )

    graph.add_node(
        "web_search",
        web_search_node,
    )

    graph.add_node(
        "mcp",
        mcp_node,
    )

    graph.add_node(
        "final_answer",
        final_answer_node,
    )

    graph.add_edge(
        START,
        "agent",
    )

    graph.add_conditional_edges(
        "agent",
        route_decision,
        {
            "calculator": "calculator",
            "rag": "rag",
            "web_search": "web_search",
            "mcp": "mcp",
            END: END,
        },
    )

    graph.add_edge(
        "calculator",
        "final_answer",
    )

    graph.add_edge(
        "rag",
        "final_answer",
    )

    graph.add_edge(
        "web_search",
        "final_answer",
    )

    graph.add_edge(
        "mcp",
        "final_answer",
    )

    graph.add_edge(
        "final_answer",
        END,
    )

    connection = sqlite3.connect(
        MEMORY_DB_PATH,
        check_same_thread=False,
    )

    checkpointer = SqliteSaver(
        connection
    )

    return graph.compile(
        checkpointer=checkpointer
    )