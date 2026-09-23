from app.memory.memory_aware_chat import answer_with_memory
from app.memory.memory_models import MemoryItem
from app.memory.memory_store import save_memory


def main():

    user_id = "memory-chat-user"

    # Save a user preference
    save_memory(
        user_id,
        MemoryItem(
            memory_type="preference",
            key="response_style",
            value="concise",
        ),
    )

    print("\n==============================")
    print("Memory-Aware Chat Test")
    print("==============================")

    print("\nUser:")
    print("Explain RAG.")

    answer = answer_with_memory(
        user_id,
        "Explain RAG."
    )

    print("\nInsightAgent:")
    print(answer)


if __name__ == "__main__":
    main()