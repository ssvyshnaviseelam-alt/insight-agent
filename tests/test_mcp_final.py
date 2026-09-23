from app.tools.mcp_tool import (
    get_mcp_tools,
    call_mcp_tool,
)
from app.agents.graph_agent import create_agent_graph


def main():
    print("\n==============================")
    print("InsightAgent MCP Final Validation")
    print("==============================")

    # 1. Tool discovery
    tools = get_mcp_tools()

    print("\n1. MCP Tool Discovery")

    for tool in tools:
        print(f"- {tool['name']}")

    discovered_names = {
        tool["name"]
        for tool in tools
    }

    if (
        "get_project_name" in discovered_names
        and "get_project_status" in discovered_names
    ):
        print("Tool discovery: PASS")
    else:
        print("Tool discovery: FAIL")
        return

    # 2. Direct MCP execution
    print("\n2. Direct MCP Execution")

    name_result = call_mcp_tool(
        "get_project_name",
        {}
    )

    status_result = call_mcp_tool(
        "get_project_status",
        {}
    )

    if (
        "InsightAgent" in str(name_result)
        and "Phase 9" in str(status_result)
    ):
        print("Direct MCP execution: PASS")
    else:
        print("Direct MCP execution: FAIL")
        return

    # 3. Full LangGraph + MCP
    print("\n3. LangGraph + MCP Integration")

    graph = create_agent_graph()

    state = {
        "question": "What is the current project status?",
        "decision": "",
        "tool_input": "",
        "tool_result": "",
        "answer": "",
    }

    result = graph.invoke(state)

    print("\nFinal Answer:")
    print(result["answer"])

    if "InsightAgent" in result["answer"]:
        print("LangGraph + MCP: PASS")
    else:
        print("LangGraph + MCP: FAIL")
        return

    print("\n==============================")
    print("FINAL MCP VALIDATION: PASS")
    print("==============================")


if __name__ == "__main__":
    main()