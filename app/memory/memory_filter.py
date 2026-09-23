def should_store_memory(message: str) -> bool:
    """
    Decide whether a message contains information
    worth storing as long-term memory.
    """

    message_lower = message.lower()

    memory_indicators = [
        "remember that",
        "my favorite",
        "i prefer",
        "i like",
        "i don't like",
        "my name is",
        "call me",
        "i work as",
        "i work at",
    ]

    return any(
        indicator in message_lower
        for indicator in memory_indicators
    )


def extract_memory(message: str) -> str:
    """
    Return the message as a memory candidate
    when it contains useful persistent information.
    """

    if should_store_memory(message):
        return message.strip()

    return ""