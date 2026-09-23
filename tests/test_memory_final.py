import os

from app.memory.memory_filter import should_store_memory
from app.memory.memory_store import (
    save_memory,
    get_user_memories
)
from app.memory.memory_models import MemoryItem
from app.memory.memory_relevance import (
    get_relevant_memories
)


def main():

    user_id = "final-memory-test-user"

    print("\n========================================")
    print("INSIGHTAGENT — FINAL MEMORY VALIDATION")
    print("========================================")

    # -------------------------------------
    # 1. Memory Filter
    # -------------------------------------

    print("\n[1] Memory Filter")
    print("----------------------------------------")

    memory_message = "I prefer concise answers."
    normal_message = "What is RAG?"

    memory_result = should_store_memory(
        memory_message
    )

    normal_result = should_store_memory(
        normal_message
    )

    print(
        "Persistent information detected:",
        memory_result
    )

    print(
        "Normal question filtered:",
        not normal_result
    )

    filter_pass = (
        memory_result is True
        and normal_result is False
    )

    print(
        "Memory Filter:",
        "PASS" if filter_pass else "FAIL"
    )

    # -------------------------------------
    # 2. Long-Term Memory Store
    # -------------------------------------

    print("\n[2] Long-Term Memory Store")
    print("----------------------------------------")

    save_memory(
        user_id,
        MemoryItem(
            memory_type="preference",
            key="response_style",
            value="concise"
        )
    )

    save_memory(
        user_id,
        MemoryItem(
            memory_type="favorite_topic",
            key="favorite_ai_topic",
            value="RAG"
        )
    )

    memories = get_user_memories(
        user_id
    )

    print(
        "Saved memories:",
        len(memories)
    )

    store_pass = (
        len(memories) >= 2
    )

    print(
        "Long-Term Memory Store:",
        "PASS" if store_pass else "FAIL"
    )

    # -------------------------------------
    # 3. Memory Relevance
    # -------------------------------------

    print("\n[3] Memory Relevance")
    print("----------------------------------------")

    rag_memories = get_relevant_memories(
        user_id,
        "Explain RAG."
    )

    python_memories = get_relevant_memories(
        user_id,
        "What is Python?"
    )

    print(
        "RAG question relevant memories:",
        rag_memories
    )

    print(
        "Python question relevant memories:",
        python_memories
    )

    rag_found = any(
        memory["value"].lower() == "rag"
        for memory in rag_memories
    )

    python_filtered = (
        len(python_memories) == 0
    )

    relevance_pass = (
        rag_found
        and python_filtered
    )

    print(
        "Memory Relevance:",
        "PASS" if relevance_pass else "FAIL"
    )

    # -------------------------------------
    # 4. Persistence
    # -------------------------------------

    print("\n[4] Persistence")
    print("----------------------------------------")

    persistence_pass = os.path.exists(
        "data/user_memories.json"
    )

    print(
        "user_memories.json exists:",
        persistence_pass
    )

    print(
        "Memory Persistence:",
        "PASS"
        if persistence_pass
        else "FAIL"
    )

    # -------------------------------------
    # Final Result
    # -------------------------------------

    print("\n========================================")
    print("FINAL RESULT")
    print("========================================")

    checks = [
        filter_pass,
        store_pass,
        relevance_pass,
        persistence_pass
    ]

    if all(checks):

        print(
            "Phase 8 Memory System: PASS"
        )

        print(
            "All core memory components "
            "are working correctly."
        )

    else:

        print(
            "Phase 8 Memory System: FAIL"
        )

        print(
            "One or more memory components "
            "need attention."
        )


if __name__ == "__main__":
    main()