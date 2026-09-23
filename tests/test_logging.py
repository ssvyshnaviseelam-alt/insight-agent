from pathlib import Path


FILES_TO_CHECK = {
    "API": Path("app/api/main.py"),
    "Streamlit": Path("app/streamlit_app.py"),
    "Agent": Path("app/agents/graph_nodes.py"),
    "Logger": Path("app/utils/logger.py"),
}


def check_file(name, path):
    if not path.exists():
        print(f"{name} file: FAIL - file not found")
        return False

    content = path.read_text(encoding="utf-8")

    if "get_logger" not in content:
        print(f"{name} logger import: FAIL")
        return False

    print(f"{name} logger integration: PASS")
    return True


results = []

for name, path in FILES_TO_CHECK.items():
    results.append(
        check_file(name, path)
    )


log_file = Path("logs/insightagent.log")

print(
    "Log file exists:",
    log_file.exists(),
)

results.append(
    log_file.exists()
)

overall = all(results)

print(
    "Overall logging validation:",
    overall,
)