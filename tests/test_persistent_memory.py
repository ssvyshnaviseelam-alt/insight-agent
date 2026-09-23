from langchain_core.messages import HumanMessage

from app.memory.memory_graph import create_memory_graph


def main():

    thread_id = "persistent-test-1"

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    print("\n==============================")
    print("Persistent Memory Test")
    print("==============================")

    # ---------------------------------
    # Graph Instance 1
    # ---------------------------------

    print("\nCreating Graph Instance 1...")

    graph1 = create_memory_graph()

    graph1.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Remember that my favorite AI framework is LangGraph."
                )
            ]
        },
        config=config,
    )

    print("Memory saved by Graph Instance 1.")


    # ---------------------------------
    # Graph Instance 2
    # ---------------------------------

    print("\nCreating Graph Instance 2...")

    graph2 = create_memory_graph()

    state = graph2.get_state(config)

    messages = state.values.get("messages", [])

    print("\nMemory retrieved by Graph Instance 2:")

    for message in messages:
        print("------------------------------")
        print("Type:", message.type)
        print("Content:", message.content)


    # ---------------------------------
    # Verification
    # ---------------------------------

    memory_found = any(
        "LangGraph" in str(message.content)
        for message in messages
    )

    print("\n==============================")
    print("Verification")
    print("==============================")

    print("Thread ID:", thread_id)
    print("Memory persisted:", "YES" if memory_found else "NO")

    if memory_found:
        print("Persistent memory test: PASS")
    else:
        print("Persistent memory test: FAIL")


if __name__ == "__main__":
    main()