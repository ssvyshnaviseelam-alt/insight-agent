from app.memory.memory_models import MemoryItem
from app.memory.memory_store import save_memory
from app.memory.memory_relevance import get_relevant_memories


def main():

    user_id = "relevance-test-user"

    # Save memories
    save_memory(
        user_id,
        MemoryItem(
            memory_type="preference",
            key="response_style",
            value="concise",
        ),
    )

    save_memory(
        user_id,
        MemoryItem(
            memory_type="favorite_topic",
            key="favorite_ai_topic",
            value="RAG",
        ),
    )

    # ---------------------------------
    # Question related to RAG
    # ---------------------------------

    question_1 = "Explain RAG."

    relevant_1 = get_relevant_memories(
        user_id,
        question_1
    )

    print("\n==============================")
    print("Question 1")
    print("==============================")

    print(question_1)

    print("\nRelevant memories:")

    for memory in relevant_1:
        print(memory)

    # ---------------------------------
    # Question unrelated to memories
    # ---------------------------------

    question_2 = "What is Python?"

    relevant_2 = get_relevant_memories(
        user_id,
        question_2
    )

    print("\n==============================")
    print("Question 2")
    print("==============================")

    print(question_2)

    print("\nRelevant memories:")

    for memory in relevant_2:
        print(memory)

    # ---------------------------------
    # Verification
    # ---------------------------------

    print("\n==============================")
    print("Verification")
    print("==============================")

    rag_found = any(
        memory["value"] == "RAG"
        for memory in relevant_1
    )

    python_has_no_memory = len(relevant_2) == 0

    print(
        "RAG memory detected:",
        "YES" if rag_found else "NO"
    )

    print(
        "Unrelated question filtered:",
        "YES" if python_has_no_memory else "NO"
    )

    if rag_found and python_has_no_memory:
        print("\nMemory relevance test: PASS")
    else:
        print("\nMemory relevance test: FAIL")


if __name__ == "__main__":
    main()
    