import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER_PATH = (
    Path(__file__).resolve().parent / "server.py"
)


async def run_client():

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER_PATH)],
    )

    async with stdio_client(
        server_params
    ) as (read, write):

        async with ClientSession(
            read,
            write
        ) as session:

            await session.initialize()

            print("\n==============================")
            print("MCP Server Connected")
            print("==============================")

            # Discover tools
            response = await session.list_tools()

            print("\nDiscovered MCP Tools:")

            for tool in response.tools:
                print(
                    f"- {tool.name}"
                )

            # Call project name tool
            print("\n==============================")
            print("Calling get_project_name")
            print("==============================")

            name_result = await session.call_tool(
                "get_project_name",
                {}
            )

            print(
                "Result:",
                name_result.content
            )

            # Call project status tool
            print("\n==============================")
            print("Calling get_project_status")
            print("==============================")

            status_result = await session.call_tool(
                "get_project_status",
                {}
            )

            print(
                "Result:",
                status_result.content
            )

            print("\n==============================")
            print("Verification")
            print("==============================")

            if (
                name_result.content
                and status_result.content
            ):
                print(
                    "MCP tool execution: PASS"
                )
            else:
                print(
                    "MCP tool execution: FAIL"
                )


if __name__ == "__main__":
    asyncio.run(
        run_client()
    )