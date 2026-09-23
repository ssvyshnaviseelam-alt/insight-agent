from app.agents.llm import get_llm
from app.memory.memory_context import get_memory_context


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


def answer_with_memory(
    user_id: str,
    question: str
):
    llm = get_llm()

    memory_context = get_memory_context(user_id)

    prompt = f"""
You are InsightAgent, a helpful AI assistant.

Use the user's saved memories when they are
relevant to the current question.

User's saved memories:
{memory_context}

User's current question:
{question}

Rules:
1. Use memories only when relevant.
2. Do not mention internal memory storage.
3. Do not invent memories.
4. Answer the user's question clearly.
"""

    response = llm.invoke(prompt)

    return extract_text(response.content)