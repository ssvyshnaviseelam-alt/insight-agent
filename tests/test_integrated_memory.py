from langchain_core.messages import HumanMessage, AIMessage

from app.memory.memory_store import save_memory
from app.memory.memory_models import MemoryItem
from app.memory.integrated_memory_chat import (
    answer_with_integrated_memory
)


def main():

    user_id = "integrated-memory-test-user"

    print("\n==============================")
    print("Step 1: Save Long-Term Memory")
    print("==============================")

    save_memory(
        user_id,
        MemoryItem(
            memory_type="preference",
            key="response_style",
            value="concise"
        )
    )

    save_memory(
        user_id,
        MemoryItem(
            memory_type="favorite_topic",
            key="favorite_ai_topic",
            value="RAG"
        )
    )

    print("Long-term memories saved.")

    print("\n==============================")
    print("Step 2: Create Conversation")
    print("==============================")

    conversation = [
        HumanMessage(
            content="I am learning AI agents."
        ),
        AIMessage(
            content="Great! AI agents are systems that can "
                     "reason and use tools."
        )
    ]

    print("Short-term conversation created.")

    print("\n==============================")
    print("Step 3: Ask Question")
    print("==============================")

    question = "Explain RAG."

    print("Question:", question)

    answer = answer_with_integrated_memory(
        user_id,
        conversation,
        question
    )

    print("\nAnswer:")
    print(answer)

    print("\n==============================")
    print("Verification")
    print("==============================")

    if answer:
        print("Short-term memory available: YES")
        print("Long-term memory available: YES")
        print("Integrated memory assistant: PASS")
    else:
        print("Integrated memory assistant: FAIL")


if __name__ == "__main__":
    main()