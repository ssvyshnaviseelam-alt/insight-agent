from app.memory.memory_graph import create_memory_graph


# Create the memory-enabled graph once
memory_graph = create_memory_graph()


def run_memory_graph(
    user_id: str,
    session_id: str,
    question: str,
):
    """
    Run the existing Phase 8 memory-enabled
    LangGraph using the API user/session identity.
    """

    config = {
        "configurable": {
            "thread_id": f"{user_id}:{session_id}"
        }
    }

    state = {
        "messages": [
            {
                "role": "user",
                "content": question,
            }
        ],
        "user_id": user_id,
        "session_id": session_id,
    }

    return memory_graph.invoke(
        state,
        config=config,
    )