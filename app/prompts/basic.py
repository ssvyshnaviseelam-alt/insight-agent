from langchain_core.prompts import ChatPromptTemplate


basic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are InsightAgent, a helpful AI assistant. "
            "Answer clearly and accurately."
        ),
        (
            "human",
            "{question}"
        ),
    ]
)