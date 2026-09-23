from app.api.session_manager import create_session_context


def test_session_context():

    context = create_session_context(
        "user1",
        "session1",
    )

    assert context.user_id == "user1"
    assert context.session_id == "session1"
    assert context.session_key == "user1:session1"


def test_different_sessions():

    session1 = create_session_context(
        "user1",
        "session1",
    )

    session2 = create_session_context(
        "user1",
        "session2",
    )

    assert session1.session_key != session2.session_key


def test_different_users():

    user1 = create_session_context(
        "user1",
        "session1",
    )

    user2 = create_session_context(
        "user2",
        "session1",
    )

    assert user1.session_key != user2.session_key


if __name__ == "__main__":
    test_session_context()
    test_different_sessions()
    test_different_users()

    print("SESSION MANAGEMENT TEST: PASS")