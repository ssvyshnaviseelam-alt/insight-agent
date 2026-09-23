import json
from pathlib import Path

from app.memory.memory_models import MemoryItem


MEMORY_FILE = Path(
    "data/user_memories.json"
)


def normalize_memory_key(
    key: str,
    value: str
) -> str:
    """
    Normalize common memory keys so that
    semantically identical memories can be
    updated instead of duplicated.
    """

    key_lower = key.lower().strip()
    value_lower = value.lower().strip()

    response_style_keys = [
        "response_style",
        "answer_style",
        "response_preference",
        "answer_preference",
        "communication_style",
    ]

    if (
        key_lower in response_style_keys
        or "concise" in value_lower
        or "detailed" in value_lower
    ):
        return "response_style"

    return key_lower


def load_memories():

    if not MEMORY_FILE.exists():
        return []

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def save_memory(
    user_id: str,
    memory: MemoryItem
):

    if memory.memory_type == "none":
        return

    memories = load_memories()

    normalized_key = normalize_memory_key(
        memory.key,
        memory.value
    )

    updated = False

    for existing_memory in memories:

        existing_key = normalize_memory_key(
            existing_memory["key"],
            existing_memory["value"]
        )

        if (
            existing_memory["user_id"] == user_id
            and existing_key == normalized_key
        ):

            existing_memory["memory_type"] = (
                memory.memory_type
            )

            existing_memory["key"] = (
                normalized_key
            )

            existing_memory["value"] = (
                memory.value
            )

            updated = True
            break

    if not updated:

        memories.append(
            {
                "user_id": user_id,
                "memory_type": memory.memory_type,
                "key": normalized_key,
                "value": memory.value,
            }
        )

    MEMORY_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memories,
            file,
            indent=2
        )


def get_user_memories(
    user_id: str
):

    memories = load_memories()

    return [
        memory
        for memory in memories
        if memory["user_id"] == user_id
    ]