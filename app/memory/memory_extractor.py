from app.agents.llm import get_llm
from app.memory.memory_models import MemoryItem


def extract_memory(message: str):
    llm = get_llm()

    structured_llm = llm.with_structured_output(
        MemoryItem
    )

    prompt = f"""
You are a memory extraction system.

Determine whether the user's message contains
useful information that an AI assistant should remember.

If it contains useful memory:
- Identify the memory type.
- Create a short key.
- Extract the important value.

If the message does not contain useful persistent
information, return:

memory_type = "none"
key = "none"
value = "none"

User message:
{message}
"""

    result = structured_llm.invoke(prompt)

    return result