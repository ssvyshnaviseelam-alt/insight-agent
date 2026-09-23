import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER_PATH = (
    Path(__file__).resolve().parent.parent
    / "mcp"
    / "server.py"
)


async def discover_mcp_tools_async():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER_PATH)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            response = await session.list_tools()

            return [
                {
                    "name": tool.name,
                    "description": tool.description,
                }
                for tool in response.tools
            ]


async def call_mcp_tool_async(tool_name: str, arguments: dict):
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER_PATH)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                tool_name,
                arguments,
            )

            return result.content


def get_mcp_tools():
    return asyncio.run(
        discover_mcp_tools_async()
    )


def call_mcp_tool(tool_name: str, arguments=None):
    if arguments is None:
        arguments = {}

    return asyncio.run(
        call_mcp_tool_async(
            tool_name,
            arguments,
        )
    )


def get_mcp_tool_names():
    tools = get_mcp_tools()

    return [
        tool["name"]
        for tool in tools
    ]


if __name__ == "__main__":
    print("\n==============================")
    print("MCP Tool Discovery")
    print("==============================")

    tools = get_mcp_tools()

    for tool in tools:
        print(
            f"- {tool['name']}: "
            f"{tool['description']}"
        )

    print("\nTool Names:")

    for name in get_mcp_tool_names():
        print(f"- {name}")