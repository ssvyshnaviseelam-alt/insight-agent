from langchain_core.messages import HumanMessage

from app.memory.memory_graph import create_memory_graph


def get_thread_config(user_id, session_id):
    return {
        "configurable": {
            "thread_id": f"{user_id}-{session_id}"
        }
    }


def save_message(graph, config, message):
    graph.invoke(
        {
            "messages": [
                HumanMessage(content=message)
            ]
        },
        config=config,
    )


def get_messages(graph, config):
    state = graph.get_state(config)
    return state.values.get("messages", [])


def main():

    graph = create_memory_graph()

    user_id = "user-001"

    # =================================
    # Session A
    # =================================

    session_a = "session-A"

    config_a = get_thread_config(
        user_id,
        session_a
    )

    save_message(
        graph,
        config_a,
        "My favorite AI topic is RAG."
    )

    # =================================
    # Session B
    # =================================

    session_b = "session-B"

    config_b = get_thread_config(
        user_id,
        session_b
    )

    save_message(
        graph,
        config_b,
        "My favorite AI topic is MCP."
    )

    # =================================
    # Read Session A
    # =================================

    messages_a = get_messages(
        graph,
        config_a
    )

    # =================================
    # Read Session B
    # =================================

    messages_b = get_messages(
        graph,
        config_b
    )

    print("\n==============================")
    print("Multiple Session Test")
    print("==============================")

    print("\nSession A:")
    for message in messages_a:
        print("------------------------------")
        print("Type:", message.type)
        print("Content:", message.content)

    print("\nSession B:")
    for message in messages_b:
        print("------------------------------")
        print("Type:", message.type)
        print("Content:", message.content)

    # =================================
    # Verify isolation
    # =================================

    text_a = " ".join(
        str(message.content)
        for message in messages_a
    )

    text_b = " ".join(
        str(message.content)
        for message in messages_b
    )

    session_a_correct = (
        "RAG" in text_a
        and "MCP" not in text_a
    )

    session_b_correct = (
        "MCP" in text_b
        and "RAG" not in text_b
    )

    print("\n==============================")
    print("Verification")
    print("==============================")

    print(
        "Session A contains RAG:",
        "YES" if session_a_correct else "NO"
    )

    print(
        "Session B contains MCP:",
        "YES" if session_b_correct else "NO"
    )

    print(
        "Sessions isolated:",
        "YES"
        if session_a_correct and session_b_correct
        else "NO"
    )

    if session_a_correct and session_b_correct:
        print("\nMultiple session test: PASS")
    else:
        print("\nMultiple session test: FAIL")


if __name__ == "__main__":
    main()