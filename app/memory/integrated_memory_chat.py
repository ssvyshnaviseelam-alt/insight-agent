from app.agents.llm import get_llm
from app.memory.memory_relevance import get_relevant_memories


def extract_text(content):
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        return "".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

    return str(content)


def get_relevant_memory_context(
    user_id: str,
    question: str
):
    memories = get_relevant_memories(
        user_id,
        question
    )

    if not memories:
        return "No relevant long-term memories."

    lines = []

    for memory in memories:
        lines.append(
            f"- {memory['key']}: {memory['value']}"
        )

    return "\n".join(lines)


def answer_with_integrated_memory(
    user_id: str,
    conversation_messages,
    question: str
):
    """
    Generate an answer using:

    1. Short-term conversation memory
    2. Relevant long-term user memory
    """

    llm = get_llm()

    long_term_memory = get_relevant_memory_context(
        user_id,
        question
    )

    conversation_text = "\n".join(
        f"{message.type}: {extract_text(message.content)}"
        for message in conversation_messages
    )

    prompt = f"""
You are InsightAgent, a helpful AI assistant.

Use both short-term conversation context
and relevant long-term user memories.

SHORT-TERM CONVERSATION:
{conversation_text}

RELEVANT LONG-TERM MEMORIES:
{long_term_memory}

CURRENT USER QUESTION:
{question}

Rules:
1. Use conversation context when relevant.
2. Use long-term memories only when relevant.
3. Do not mention internal memory systems.
4. Do not invent memories.
5. Answer clearly and naturally.
"""

    response = llm.invoke(prompt)

    return extract_text(response.content)