import re

from app.memory.memory_store import get_user_memories


def normalize_text(text: str) -> set[str]:
    """
    Convert text into normalized words.
    """

    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    return set(text.split())


def get_relevant_memories(
    user_id: str,
    question: str
):
    """
    Return memories that have meaningful word overlap
    with the current question.
    """

    memories = get_user_memories(user_id)

    question_words = normalize_text(question)

    relevant = []

    for memory in memories:

        memory_text = (
            f"{memory['key']} "
            f"{memory['value']}"
        )

        memory_words = normalize_text(
            memory_text
        )

        # Check whether question words overlap
        # with the stored memory.
        if question_words.intersection(
            memory_words
        ):
            relevant.append(memory)

    return relevant