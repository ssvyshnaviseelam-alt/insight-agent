from app.agents.llm import get_llm
from app.tools.calculator import calculate


def decide_and_execute(question: str):
    llm = get_llm()

    tools = [calculate]

    llm_with_tools = llm.bind_tools(tools)

    response = llm_with_tools.invoke(question)

    print("\nAgent Decision")
    print("--------------")

    if response.tool_calls:
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]

            print(f"Decision: USE {tool_name.upper()}")

            if tool_name == "calculate":
                expression = tool_call["args"]["expression"]

                print(f"Expression: {expression}")

                result = calculate.invoke(
                    tool_call["args"]
                )

                print(f"Tool result: {result}")

                return result

    print("Decision: ANSWER DIRECTLY")
    return response.content