from langgraph.graph import END

from app.agents.llm import get_llm
from app.tools.calculator import calculate
from app.tools.rag_tool import search_knowledge_base
from app.tools.search_tool import web_search
from app.tools.mcp_tool import call_mcp_tool
from app.utils.logger import get_logger

logger = get_logger("InsightAgent.Agent")


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


def agent_node(state):
    question = state["question"]
    question_lower = question.lower()

    if (
        "project status" in question_lower
        or "status of insightagent" in question_lower
        or "current phase" in question_lower
        or "project name" in question_lower
        or "what is insightagent" in question_lower
    ):
        logger.info("Agent selected MCP directly")
        return {
            "decision": "mcp",
            "tool_input": question,
            "tool_used": "mcp",
        }
    memory_context = state.get(
        "memory_context",
        "No relevant long-term memories."
    )

    llm = get_llm()

    tools = [
        calculate,
        search_knowledge_base,
        web_search,
    ]

    llm_with_tools = llm.bind_tools(tools)

    response = llm_with_tools.invoke(
        f"""
You are the decision-making agent for InsightAgent.

Choose the most appropriate action for the user's question.

Available actions:

1. Use calculate for mathematical calculations.
2. Use search_knowledge_base for questions about information
   contained in the internal AI Agents knowledge base.
3. Use web_search for current, latest, recent, today's,
   or up-to-date information.
4. Use MCP for questions specifically about the InsightAgent
   project, such as project name or project status.
5. If the question is unrelated to these tools, answer directly.

Important MCP examples:

- "What is the project name?"
- "What is InsightAgent?"
- "What is the current project status?"
- "Which phase is InsightAgent currently in?"

For MCP-related questions, return a decision of "mcp".

Relevant long-term user memory:
{memory_context}

Use the memory only when it is relevant to the user's question.
Do not mention the internal memory system.

User question:
{question}
"""
    )

    if not response.tool_calls:
        question_lower = question.lower()

        if (
            "project status" in question_lower
            or "status of insightagent" in question_lower
            or "current phase" in question_lower
            or "project name" in question_lower
            or "what is insightagent" in question_lower
        ):
            return {
                "decision": "mcp",
                "tool_input": question,
                "tool_used": "mcp",
            }
        logger.info(
            "Agent selected direct answer"
        )
        return {
            "decision": "direct",
            "answer": extract_text(response.content),
            "tool_used": "direct",
        }

    tool_call = response.tool_calls[0]

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    logger.info(
        "Agent selected tool | "
        f"tool={tool_name}"
    )

    tool_input = ""

    if tool_name == "calculate":
        tool_input = tool_args.get(
            "expression",
            ""
        )

    elif tool_name == "search_knowledge_base":
        tool_input = tool_args.get(
            "question",
            ""
        )

    elif tool_name == "web_search":
        tool_input = tool_args.get(
            "query",
            ""
        )
   
    return {
        "decision": tool_name,
        "tool_input": tool_input,
         "tool_used": tool_name,
    }

def calculator_node(state):
    expression = state["tool_input"]

    logger.info(
        "Calculator tool executing | "
        f"expression={expression}"
    )

    result = calculate.invoke(
        {"expression": expression}
    )

    return {
        "tool_result": result
    }


def rag_node(state):
    question = state["question"]

    logger.info(
        "RAG tool executing | "
        f"question={question}"
    )

    result = search_knowledge_base.invoke(
        {"question": question}
    )

    sources = []

    if isinstance(result, dict):
        sources = result.get(
            "sources",
            []
        )

        tool_result = result.get(
            "answer",
            ""
        )

    else:
        tool_result = str(result)

    logger.info(
        "RAG tool completed | "
        f"sources={len(sources)}"
    )

    return {
        "tool_result": tool_result,
        "sources": sources,
    }



def web_search_node(state):
    question = state["question"]

    logger.info(
        "Web search tool executing | "
        f"query={question}"
    )

    result = web_search.invoke(
        {"query": question}
    )

    return {
        "tool_result": result
    }


def mcp_node(state):
    question = state["question"]
    question_lower = question.lower()

    logger.info(
        "MCP tool executing | "
        f"question={question}"
    )

    if (
        "project status" in question_lower
        or "status of insightagent" in question_lower
        or "current phase" in question_lower
    ):
        result = call_mcp_tool(
            "get_project_status",
            {}
        )

    elif (
        "project name" in question_lower
        or "what is insightagent" in question_lower
    ):
        result = call_mcp_tool(
            "get_project_name",
            {}
        )

    else:
        result = "No matching MCP tool found."

    logger.info(
        "MCP tool completed"
    )

    return {
        "tool_result": str(result)
    }


def final_answer_node(state):
    decision = state["decision"]
    tool_result = state.get("tool_result", "")

    if decision == "calculate":
        return {
            "answer": str(tool_result)
        }

    if decision == "search_knowledge_base":
        if isinstance(tool_result, dict):
            return {
                "answer": tool_result.get(
                    "answer",
                    "No answer returned."
                ),
                "sources": tool_result.get(
                    "sources",
                    []
                ),
            }

        return {
            "answer": str(tool_result)
        }

    if decision == "mcp":
        return {
            "answer": str(tool_result)
        }

    if decision == "web_search":
        question = state["question"]

        llm = get_llm()

        prompt = f"""
You are InsightAgent.

Answer the user's question using the web search
results below.

User question:
{question}

Web search results:
{tool_result}

Rules:
1. Use the search results as the source of truth.
2. Give a clear and concise answer.
3. Do not invent information.
"""

        response = llm.invoke(prompt)

        return {
            "answer": extract_text(response.content)
        }

    return {
        "answer": state.get("answer", "")
    }


def route_decision(state):
    decision = state["decision"]

    if decision == "calculate":
        return "calculator"

    if decision == "search_knowledge_base":
        return "rag"

    if decision == "web_search":
        return "web_search"

    if decision == "mcp":
        return "mcp"

    return END