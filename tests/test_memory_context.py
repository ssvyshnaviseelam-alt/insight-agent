from app.memory.memory_context import get_memory_context
from app.memory.memory_models import MemoryItem
from app.memory.memory_store import save_memory


def main():

    user_id = "context-test-user"

    # Create test memories
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

    # Retrieve memories
    context = get_memory_context(user_id)

    print("\n==============================")
    print("Memory Context")
    print("==============================")

    print(context)

    print("\n==============================")
    print("Verification")
    print("==============================")

    if (
        "response_style: concise" in context
        and "favorite_ai_topic: RAG" in context
    ):
        print("Memory retrieval: PASS")
    else:
        print("Memory retrieval: FAIL")


if __name__ == "__main__":
    main()