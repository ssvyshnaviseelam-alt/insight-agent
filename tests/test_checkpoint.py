from langchain_core.messages import HumanMessage

from app.memory.memory_graph import create_memory_graph


def main():
    graph = create_memory_graph()

    config = {
        "configurable": {
            "thread_id": "user-session-1"
        }
    }

    # Read the existing saved state from SQLite.
    state = graph.get_state(config)

    print("\n==============================")
    print("Saved Checkpoint State")
    print("==============================")

    if not state.values:
        print("\nNo saved state found for this thread.")
        print("Run the memory test first:")
        print("python -m tests.test_memory_graph")
        return

    messages = state.values.get("messages", [])

    print("\nNumber of saved messages:")
    print(len(messages))

    print("\nSaved messages:")

    for message in messages:
        print("------------------------------")
        print("Type:", message.type)
        print("Content:", message.content)

    print("\n==============================")
    print("Checkpoint Verification")
    print("==============================")

    print("Thread ID:", config["configurable"]["thread_id"])
    print("Memory loaded from SQLite: YES")
    print("Checkpoint inspection: PASS")


if __name__ == "__main__":
    main()