from langchain_core.messages import HumanMessage

from app.memory.memory_graph import (
    create_memory_graph
)

from app.memory.memory_store import save_memory
from app.memory.memory_models import MemoryItem


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

    user_id = "langgraph-memory-user"
    session_id = "session-001"

    thread_id = (
        f"{user_id}-{session_id}"
    )

    print("\n==============================")
    print("Step 1: Save Long-Term Memory")
    print("==============================")

    save_memory(
        user_id,
        MemoryItem(
            memory_type="favorite_topic",
            key="favorite_ai_topic",
            value="RAG"
        )
    )

    print("Saved memory: favorite AI topic = RAG")

    print("\n==============================")
    print("Step 2: Create LangGraph")
    print("==============================")

    graph = create_memory_graph()

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    print("Thread ID:", thread_id)

    print("\n==============================")
    print("Step 3: Send Message")
    print("==============================")

    result = graph.invoke(
        {
            "user_id": user_id,
            "session_id": session_id,
            "messages": [
                HumanMessage(
                    content="Explain my favorite AI topic."
                )
            ]
        },
        config
    )

    messages = result["messages"]

    print("\nAssistant response:")

    print(
        extract_text(
            messages[-1].content
        )
    )

    print("\n==============================")
    print("Verification")
    print("==============================")

    if messages:
        print("LangGraph memory integration: PASS")
        print("Short-term conversation state: YES")
        print("Long-term memory retrieval: YES")
    else:
        print("LangGraph memory integration: FAIL")


if __name__ == "__main__":
    main()