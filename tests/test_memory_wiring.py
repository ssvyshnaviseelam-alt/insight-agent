from pathlib import Path


streamlit_code = Path(
    "app/streamlit_app.py"
).read_text(
    encoding="utf-8"
)

api_code = Path(
    "app/api/main.py"
).read_text(
    encoding="utf-8"
)

graph_code = Path(
    "app/agents/graph_agent.py"
).read_text(
    encoding="utf-8"
)

production_code = Path(
    "app/agents/production_agent.py"
).read_text(
    encoding="utf-8"
)


print(
    "Streamlit user/session:",
    (
        'key="user_id"' in streamlit_code
        and 'key="session_id"' in streamlit_code
    ),
)

print(
    "API thread config:",
    "create_thread_config" in api_code,
)

print(
    "Graph checkpointer:",
    (
        "SqliteSaver" in graph_code
        and "checkpointer=checkpointer" in graph_code
    ),
)

print(
    "Long-term memory:",
    "get_relevant_memories" in production_code,
)


overall = all(
    [
        'key="user_id"' in streamlit_code,
        'key="session_id"' in streamlit_code,
        "create_thread_config" in api_code,
        "checkpointer=checkpointer" in graph_code,
        "get_relevant_memories" in production_code,
    ]
)


print(
    "Overall memory wiring:",
    overall,
)