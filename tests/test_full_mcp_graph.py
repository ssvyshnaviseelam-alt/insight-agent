from app.agents.graph_agent import create_agent_graph


def main():
    print("\n==============================")
    print("Full LangGraph + MCP Test")
    print("==============================")

    graph = create_agent_graph()

    state = {
        "question": "What is the current project status?",
        "decision": "",
        "tool_input": "",
        "tool_result": "",
        "answer": "",
    }

    result = graph.invoke(state)

    print("\nQuestion:")
    print(state["question"])

    print("\nFinal Answer:")
    print(result["answer"])

    print("\n==============================")
    print("Verification")
    print("==============================")

    if "InsightAgent" in result["answer"]:
        print("Full LangGraph + MCP: PASS")
    else:
        print("Full LangGraph + MCP: FAIL")


if __name__ == "__main__":
    main()