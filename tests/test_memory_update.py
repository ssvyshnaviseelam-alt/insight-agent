from app.memory.memory_models import MemoryItem
from app.memory.memory_store import (
    save_memory,
    get_user_memories,
)


def main():

    user_id = "update-test-user"

    print("\n==============================")
    print("Memory Update Test")
    print("==============================")

    # ---------------------------------
    # Save initial preference
    # ---------------------------------

    first_memory = MemoryItem(
        memory_type="preference",
        key="response_style",
        value="concise",
    )

    save_memory(
        user_id,
        first_memory
    )

    print("\nAfter first memory:")

    memories = get_user_memories(user_id)

    for memory in memories:
        print(memory)


    # ---------------------------------
    # Update preference
    # ---------------------------------

    updated_memory = MemoryItem(
        memory_type="preference",
        key="response_style",
        value="detailed",
    )

    save_memory(
        user_id,
        updated_memory
    )

    print("\nAfter updating memory:")

    memories = get_user_memories(user_id)

    for memory in memories:
        print(memory)


    # ---------------------------------
    # Verification
    # ---------------------------------

    matching_memories = [
        memory
        for memory in memories
        if memory["key"] == "response_style"
    ]

    print("\n==============================")
    print("Verification")
    print("==============================")

    print(
        "Number of response_style memories:",
        len(matching_memories)
    )

    if (
        len(matching_memories) == 1
        and matching_memories[0]["value"] == "detailed"
    ):
        print("Memory updated correctly: YES")
        print("Memory update test: PASS")
    else:
        print("Memory updated correctly: NO")
        print("Memory update test: FAIL")


if __name__ == "__main__":
    main()