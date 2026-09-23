from app.memory.memory_extractor import extract_memory


def main():

    messages = [
        "I prefer concise answers.",
        "My favorite AI topic is RAG.",
        "My name is Vyshnavi.",
        "What is a vector database?",
    ]

    print("\n==============================")
    print("Structured Memory Extraction")
    print("==============================")

    for message in messages:

        print("\nUser message:")
        print(message)

        result = extract_memory(message)

        print("\nExtracted memory:")
        print("Type:", result.memory_type)
        print("Key:", result.key)
        print("Value:", result.value)


if __name__ == "__main__":
    main()