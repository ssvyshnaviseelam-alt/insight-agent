from app.memory.memory_extractor import extract_memory
from app.memory.memory_store import (
    save_memory,
    get_user_memories,
)


def main():

    user_id = "user-001"

    messages = [
        "I prefer concise answers.",
        "My favorite AI topic is RAG.",
    ]

    print("\n==============================")
    print("Structured Memory Store Test")
    print("==============================")

    for message in messages:

        print("\nUser message:")
        print(message)

        memory = extract_memory(message)

        print("\nExtracted:")
        print(memory)

        save_memory(
            user_id,
            memory
        )

    memories = get_user_memories(user_id)

    print("\n==============================")
    print("Saved User Memories")
    print("==============================")

    for memory in memories:
        print("------------------------------")
        print("Type:", memory["memory_type"])
        print("Key:", memory["key"])
        print("Value:", memory["value"])

    print("\nTotal memories:", len(memories))

    if len(memories) >= 2:
        print("\nMemory store test: PASS")
    else:
        print("\nMemory store test: FAIL")


if __name__ == "__main__":
    main()