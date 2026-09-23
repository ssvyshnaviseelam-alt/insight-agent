from dataclasses import dataclass


@dataclass
class SessionContext:
    user_id: str
    session_id: str

    @property
    def session_key(self) -> str:
        return f"{self.user_id}:{self.session_id}"


def create_session_context(
    user_id: str,
    session_id: str,
) -> SessionContext:

    return SessionContext(
        user_id=user_id.strip(),
        session_id=session_id.strip(),
    )