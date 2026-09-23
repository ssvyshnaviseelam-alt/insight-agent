from app.agents.mcp_node import mcp_node


def main():

    print("\n==============================")
    print("MCP + LangGraph Node Test")
    print("==============================")

    state = {
        "question": "What is the current project status?",
        "decision": "mcp",
        "tool_input": "",
        "tool_result": "",
        "answer": ""
    }

    result = mcp_node(state)

    print("\nMCP Result:")
    print(result["tool_result"])

    print("\n==============================")
    print("Verification")
    print("==============================")

    if "InsightAgent" in result["tool_result"]:
        print(
            "MCP + LangGraph node: PASS"
        )
    else:
        print(
            "MCP + LangGraph node: FAIL"
        )


if __name__ == "__main__":
    main()