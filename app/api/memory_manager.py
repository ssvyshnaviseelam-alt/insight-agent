from pathlib import Path


MEMORY_DB_PATH = Path("data/memory.db")


def get_memory_database_path() -> str:
    MEMORY_DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    return str(MEMORY_DB_PATH)


def create_thread_config(
    user_id: str,
    session_id: str,
) -> dict:

    return {
        "configurable": {
            "thread_id": f"{user_id}:{session_id}"
        }
    }


def get_thread_id(
    user_id: str,
    session_id: str,
) -> str:

    return f"{user_id}:{session_id}"