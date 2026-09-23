from app.memory.memory_extractor import extract_memory
from app.memory.memory_store import save_memory


def process_message_for_memory(
    user_id: str,
    message: str
):
    """
    Automatically extract useful long-term memory
    and save it.

    If the same memory key already exists,
    memory_store updates the existing value.
    """

    memory = extract_memory(message)

    if memory.memory_type == "none":
        return None

    save_memory(
        user_id,
        memory
    )

    return memory