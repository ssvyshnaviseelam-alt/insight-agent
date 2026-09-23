from dataclasses import dataclass


@dataclass
class UserContext:
    user_id: str
    session_id: str
    name: str = "User"