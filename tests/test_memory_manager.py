from app.api.memory_manager import (
    get_memory_database_path,
    create_thread_config,
)


def test_memory_database_path():

    path = get_memory_database_path()

    assert path.endswith(
        "data\\memory.db"
    ) or path.endswith(
        "data/memory.db"
    )


def test_thread_config():

    config = create_thread_config(
        "user1",
        "session1",
    )

    assert config["configurable"]["thread_id"] == (
        "user1:session1"
    )


def test_different_threads():

    config1 = create_thread_config(
        "user1",
        "session1",
    )

    config2 = create_thread_config(
        "user1",
        "session2",
    )

    config3 = create_thread_config(
        "user2",
        "session1",
    )

    thread1 = config1["configurable"]["thread_id"]
    thread2 = config2["configurable"]["thread_id"]
    thread3 = config3["configurable"]["thread_id"]

    assert thread1 != thread2
    assert thread1 != thread3
    assert thread2 != thread3


if __name__ == "__main__":

    test_memory_database_path()
    test_thread_config()
    test_different_threads()

    print("MEMORY MANAGER TEST: PASS")