from app.agents.graph_agent import create_agent_graph
from app.memory.memory_relevance import get_relevant_memories
from app.memory.memory_extractor import extract_memory
from app.memory.memory_store import save_memory


agent_graph = create_agent_graph()


def get_memory_context(
    user_id: str,
    question: str,
) -> str:

    memories = get_relevant_memories(
        user_id,
        question,
    )

    if not memories:
        return "No relevant long-term memories."

    lines = []

    for memory in memories:
        lines.append(
            f"- {memory['key']}: {memory['value']}"
        )

    return "\n".join(lines)


def save_user_memory(
    user_id: str,
    question: str,
) -> None:

    memory = extract_memory(question)

    if memory.memory_type == "none":
        return

    save_memory(
        user_id,
        memory,
    )


def prepare_agent_state(
    user_id: str,
    session_id: str,
    question: str,
) -> dict:

    # Save useful long-term memory from the
    # current user message.
    save_user_memory(
        user_id,
        question,
    )

    # Retrieve relevant memories after saving.
    memory_context = get_memory_context(
        user_id,
        question,
    )

    return {
        "question": question,
        "user_id": user_id,
        "session_id": session_id,
        "decision": "",
        "tool_input": "",
        "tool_result": "",
        "answer": "",
        "memory_context": memory_context,
        "tool_used": "",
        "sources": [],
    }