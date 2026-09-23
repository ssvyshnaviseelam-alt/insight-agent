from langchain_core.messages import HumanMessage

from app.memory.memory_graph import create_memory_graph


def get_saved_messages(graph, thread_id):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    state = graph.get_state(config)

    return state.values.get("messages", [])


def main():

    graph = create_memory_graph()

    # ---------------------------------
    # User A
    # ---------------------------------

    user_a_config = {
        "configurable": {
            "thread_id": "user-A-session"
        }
    }

    graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="My favorite AI technology is RAG."
                )
            ]
        },
        config=user_a_config,
    )

    # ---------------------------------
    # User B
    # ---------------------------------

    user_b_config = {
        "configurable": {
            "thread_id": "user-B-session"
        }
    }

    graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="My favorite AI technology is MCP."
                )
            ]
        },
        config=user_b_config,
    )

    # ---------------------------------
    # Retrieve User A memory
    # ---------------------------------

    user_a_messages = get_saved_messages(
        graph,
        "user-A-session"
    )

    # ---------------------------------
    # Retrieve User B memory
    # ---------------------------------

    user_b_messages = get_saved_messages(
        graph,
        "user-B-session"
    )

    print("\n==============================")
    print("Memory Isolation Test")
    print("==============================")

    print("\nUser A Memory:")
    for message in user_a_messages:
        print("------------------------------")
        print("Type:", message.type)
        print("Content:", message.content)

    print("\nUser B Memory:")
    for message in user_b_messages:
        print("------------------------------")
        print("Type:", message.type)
        print("Content:", message.content)

    # ---------------------------------
    # Verify isolation
    # ---------------------------------

    user_a_text = " ".join(
        str(message.content)
        for message in user_a_messages
    )

    user_b_text = " ".join(
        str(message.content)
        for message in user_b_messages
    )

    user_a_correct = (
        "RAG" in user_a_text
        and "MCP" not in user_a_text
    )

    user_b_correct = (
        "MCP" in user_b_text
        and "RAG" not in user_b_text
    )

    print("\n==============================")
    print("Verification")
    print("==============================")

    print(
        "User A isolated:",
        "YES" if user_a_correct else "NO"
    )

    print(
        "User B isolated:",
        "YES" if user_b_correct else "NO"
    )

    if user_a_correct and user_b_correct:
        print("\nMemory isolation test: PASS")
    else:
        print("\nMemory isolation test: FAIL")


if __name__ == "__main__":
    main()