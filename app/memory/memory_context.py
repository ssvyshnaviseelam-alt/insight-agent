from app.memory.memory_store import get_user_memories


def get_memory_context(user_id: str) -> str:
    """
    Convert saved user memories into text that can
    be included in an LLM prompt.
    """

    memories = get_user_memories(user_id)

    if not memories:
        return "No saved user memories."

    lines = []

    for memory in memories:
        lines.append(
            f"- {memory['key']}: {memory['value']}"
        )

    return "\n".join(lines)