from langchain_core.messages import HumanMessage

from app.agents.message_graph import create_message_graph

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
def main():

    graph = create_message_graph()

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Explain RAG in one sentence."
                )
            ],
            "user_id": "user-001",
            "session_id": "session-001",
        }
    )

    print("\nInsightAgent Message Graph")
    print("==========================")

    print("\nConversation:")

    for message in result["messages"]:
        print(
            f"\n{message.__class__.__name__}:"
        )
        print( extract_text(message.content))


if __name__ == "__main__":
    main()