from app.tools.mcp_tool import (
    get_mcp_tools,
    call_mcp_tool,
)


def mcp_node(state):
    question = state["question"]
    question_lower = question.lower()

    # Discover available MCP tools
    tools = get_mcp_tools()

    tool_names = {
        tool["name"]
        for tool in tools
    }

    # Decide which discovered MCP tool to use
    if (
        "project status" in question_lower
        or "status of insightagent" in question_lower
        or "current phase" in question_lower
    ):
        tool_name = "get_project_status"

    elif (
        "project name" in question_lower
        or "what is insightagent" in question_lower
    ):
        tool_name = "get_project_name"

    else:
        return {
            "tool_result": "No matching MCP tool found."
        }

    # Make sure the requested tool actually exists
    if tool_name not in tool_names:
        return {
            "tool_result": (
                f"MCP tool '{tool_name}' "
                "is not available."
            )
        }

    # Execute discovered MCP tool
    result = call_mcp_tool(
        tool_name,
        {}
    )

    return {
        "tool_result": str(result)
    }