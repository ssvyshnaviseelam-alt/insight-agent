from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)


def create_conversation():
    messages = [
        SystemMessage(
            content="You are InsightAgent, a helpful AI assistant."
        ),
        HumanMessage(
            content="What is an AI agent?"
        ),
        AIMessage(
            content="An AI agent is a system that can reason, use tools, and take actions to accomplish a goal."
        ),
        HumanMessage(
            content="What makes it different from a normal chatbot?"
        ),
    ]

    return messages