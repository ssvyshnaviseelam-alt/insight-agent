from langchain_core.messages import HumanMessage

from app.memory.memory_graph import create_memory_graph


def main():

    graph = create_memory_graph()

    user_id = "user-001"
    session_id = "session-001"

    thread_id = f"{user_id}-{session_id}"

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    print("\n==============================")
    print("User Context Memory Test")
    print("==============================")

    print("\nUser ID:", user_id)
    print("Session ID:", session_id)
    print("Thread ID:", thread_id)

    graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="My favorite AI topic is LangGraph."
                )
            ],
            "user_id": user_id,
            "session_id": session_id,
        },
        config=config,
    )

    state = graph.get_state(config)

    messages = state.values.get("messages", [])

    print("\nSaved conversation:")

    for message in messages:
        print("------------------------------")
        print("Type:", message.type)
        print("Content:", message.content)

    print("\n==============================")
    print("Verification")
    print("==============================")

    saved_user_id = state.values.get("user_id")
    saved_session_id = state.values.get("session_id")

    print("Saved User ID:", saved_user_id)
    print("Saved Session ID:", saved_session_id)

    if (
        saved_user_id == user_id
        and saved_session_id == session_id
    ):
        print("\nUser/session context test: PASS")
    else:
        print("\nUser/session context test: FAIL")


if __name__ == "__main__":
    main()