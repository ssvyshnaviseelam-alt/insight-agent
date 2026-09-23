from langchain_core.messages import HumanMessage, AIMessage

from app.agents.message_state import InsightMessageState


def main():

    state = InsightMessageState(
        messages=[
            HumanMessage(
                content="What is RAG?"
            ),
            AIMessage(
                content="RAG retrieves relevant information before generating an answer."
            ),
        ],
        user_id="user-001",
        session_id="session-001",
    )

    print("\nInsightAgent Message State")
    print("==========================")

    print("\nUser ID:")
    print(state["user_id"])

    print("\nSession ID:")
    print(state["session_id"])

    print("\nMessages:")

    for message in state["messages"]:
        print(
            f"{message.__class__.__name__}: "
            f"{message.content}"
        )


if __name__ == "__main__":
    main()