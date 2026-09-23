from app.agents.llm import get_llm
from app.tools.calculator import calculate
from app.tools.rag_tool import search_knowledge_base
from app.tools.search_tool import web_search


def extract_text(content):
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        return "".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

    return str(content)


def run_multi_tool_agent(question: str):
    llm = get_llm()

    tools = [
        calculate,
        search_knowledge_base,
        web_search,
    ]

    llm_with_tools = llm.bind_tools(tools)

    response = llm_with_tools.invoke(question)

    print("\nAgent Decision")
    print("--------------")

    if not response.tool_calls:
        print("Decision: ANSWER DIRECTLY")
        return extract_text(response.content)

    tool_results = []

    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]

        print(f"Decision: USE {tool_name}")

        if tool_name == "calculate":
            result = calculate.invoke(
                tool_call["args"]
            )

        elif tool_name == "search_knowledge_base":
            result = search_knowledge_base.invoke(
                tool_call["args"]
            )

        elif tool_name == "web_search":
            result = web_search.invoke(
                tool_call["args"]
            )

        else:
            result = "Unknown tool."

        print(f"Tool result received.")

        tool_results.append(
            {
                "tool": tool_name,
                "result": result,
            }
        )

    final_prompt = (
        f"User question: {question}\n\n"
        f"Tool results: {tool_results}\n\n"
        "Provide a clear final answer to the user. "
        "Use the tool results as the source of truth."
    )

    final_response = llm.invoke(final_prompt)

    return extract_text(final_response.content)