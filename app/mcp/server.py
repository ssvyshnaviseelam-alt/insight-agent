from mcp.server.mcpserver import MCPServer


mcp = MCPServer(
    name="InsightAgent MCP Server"
)


@mcp.tool()
def get_project_status() -> str:
    """
    Return the current status of the InsightAgent project.
    """

    return (
        "InsightAgent is currently in Phase 9 - "
        "MCP Integration."
    )


@mcp.tool()
def get_project_name() -> str:
    """
    Return the project name.
    """

    return "InsightAgent"


if __name__ == "__main__":
    mcp.run()