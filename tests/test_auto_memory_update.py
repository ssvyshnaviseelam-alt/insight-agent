from app.memory.auto_memory import (
    process_message_for_memory
)

from app.memory.memory_store import (
    get_user_memories
)


def main():

    user_id = "auto-memory-update-user"

    print("\n==============================")
    print("Step 1: Initial Preference")
    print("==============================")

    first_message = "I prefer concise answers."

    first_memory = process_message_for_memory(
        user_id,
        first_message
    )

    print("User:", first_message)

    if first_memory:
        print(
            "Saved:",
            first_memory.key,
            "=",
            first_memory.value
        )

    print("\n==============================")
    print("Step 2: Change Preference")
    print("==============================")

    second_message = "I prefer detailed answers."

    second_memory = process_message_for_memory(
        user_id,
        second_message
    )

    print("User:", second_message)

    if second_memory:
        print(
            "Updated:",
            second_memory.key,
            "=",
            second_memory.value
        )

    print("\n==============================")
    print("Step 3: Inspect Memories")
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

    response_style_memories = [
        memory
        for memory in memories
        if memory["key"] == "response_style"
    ]

    if len(response_style_memories) == 1:

        final_value = (
            response_style_memories[0]["value"]
            .lower()
        )

        if "detailed" in final_value:

            print(
                "One response-style memory: YES"
            )

            print(
                "Preference updated to detailed: YES"
            )

            print(
                "Memory update and deduplication: PASS"
            )

        else:

            print(
                "Preference updated to detailed: NO"
            )

            print(
                "Memory update and deduplication: FAIL"
            )

    else:

        print(
            "Exactly one response-style memory: NO"
        )

        print(
            "Memory update and deduplication: FAIL"
        )


if __name__ == "__main__":
    main()