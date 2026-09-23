from app.memory.auto_memory import (
    process_message_for_memory
)

from app.memory.memory_store import (
    get_user_memories
)


def main():

    user_id = "auto-memory-test-user"

    messages = [
        "I prefer concise answers.",
        "My favorite AI topic is RAG.",
        "What is a vector database?"
    ]

    print("\n==============================")
    print("Automatic Memory Extraction")
    print("==============================")

    for message in messages:

        print("\nUser message:")
        print(message)

        memory = process_message_for_memory(
            user_id,
            message
        )

        if memory:
            print("\nMemory extracted:")
            print("Type:", memory.memory_type)
            print("Key:", memory.key)
            print("Value:", memory.value)
        else:
            print("\nNo long-term memory extracted.")

    print("\n==============================")
    print("Saved Memories")
    print("==============================")

    memories = get_user_memories(
        user_id
    )

    for memory in memories:
        print("------------------------------")
        print(memory)

    print("\n==============================")
    print("Verification")
    print("==============================")

    has_concise = any(
        memory["value"].lower() == "concise"
        for memory in memories
    )

    has_rag = any(
        memory["value"].lower() == "rag"
        for memory in memories
    )

    if has_concise and has_rag:
        print(
            "Automatic memory extraction: PASS"
        )
    else:
        print(
            "Automatic memory extraction: FAIL"
        )


if __name__ == "__main__":
    main()