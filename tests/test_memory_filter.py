from app.memory.memory_filter import (
    should_store_memory,
    extract_memory,
)


def main():

    test_messages = [
        "Remember that my favorite AI topic is RAG.",
        "My favorite framework is LangGraph.",
        "What is RAG?",
        "Explain vector databases.",
        "I prefer concise answers.",
        "Calculate 125 * 8.",
    ]

    print("\n==============================")
    print("Memory Filter Test")
    print("==============================")

    for message in test_messages:

        store = should_store_memory(message)
        memory = extract_memory(message)

        print("\nMessage:", message)
        print("Store:", store)

        if memory:
            print("Memory:", memory)
        else:
            print("Memory: Not stored")


if __name__ == "__main__":
    main()