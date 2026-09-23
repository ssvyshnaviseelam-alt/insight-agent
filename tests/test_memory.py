from langchain_core.messages import HumanMessage, AIMessage


def main():

    messages = []

    # First conversation turn
    messages.append(
        HumanMessage(
            content="My name is Vyshnavi."
        )
    )

    messages.append(
        AIMessage(
            content="Nice to meet you, Vyshnavi!"
        )
    )

    # Second conversation turn
    messages.append(
        HumanMessage(
            content="What is my name?"
        )
    )

    print("\nInsightAgent Memory Test")
    print("========================")

    print("\nConversation history:")

    for message in messages:
        print(
            f"{message.__class__.__name__}: "
            f"{message.content}"
        )


if __name__ == "__main__":
    main()