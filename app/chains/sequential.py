from langchain_core.prompts import ChatPromptTemplate

from app.agents.llm import get_llm


def create_sequential_chain():
    llm = get_llm()

    explanation_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an AI tutor. Explain the topic clearly "
                "for a software engineer."
            ),
            (
                "human",
                "Explain this topic: {topic}"
            ),
        ]
    )

    summary_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an AI technical writer. "
                "Summarize the explanation in 2 concise sentences."
            ),
            (
                "human",
                "{explanation}"
            ),
        ]
    )

    explanation_chain = explanation_prompt | llm
    summary_chain = summary_prompt | llm

    sequential_chain = (
        explanation_chain
        | (lambda response: {"explanation": response.content})
        | summary_chain
    )

    return sequential_chain