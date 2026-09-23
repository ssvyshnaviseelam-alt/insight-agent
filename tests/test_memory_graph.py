from langchain_core.messages import HumanMessage

from app.memory.memory_graph import create_memory_graph


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

    graph = create_memory_graph()

    config = {
        "configurable": {
            "thread_id": "user-session-2"
        }
    }

    # First message
    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="My favorite AI topic is MCP."
                )
            ]
        },
        config=config,
    )

    print("\nFirst Response:")
    print(
        extract_text(
            result["messages"][-1].content
        )
    )

    # Second message using the SAME thread
    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="What is my favorite AI topic?"
                )
            ]
        },
        config=config,
    )

    print("\nSecond Response:")
    print(
        extract_text(
            result["messages"][-1].content
        )
    )


if __name__ == "__main__":
    main()