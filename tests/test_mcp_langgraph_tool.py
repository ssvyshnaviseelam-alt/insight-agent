from app.tools.mcp_tool import (
    get_insightagent_project_status
)


def main():

    print("\n==============================")
    print("MCP + LangChain Integration")
    print("==============================")

    result = (
        get_insightagent_project_status.invoke({})
    )

    print("\nMCP Tool Result:")
    print(result)

    print("\n==============================")
    print("Verification")
    print("==============================")

    if "InsightAgent" in result:
        print(
            "MCP + LangChain tool integration: PASS"
        )
    else:
        print(
            "MCP + LangChain tool integration: FAIL"
        )


if __name__ == "__main__":
    main()