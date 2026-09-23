from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

from app.agents.llm import get_llm


def create_parallel_chain():
    llm = get_llm()

    explanation_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an AI tutor. Explain the topic clearly "
                "in 3 sentences."
            ),
            (
                "human",
                "Explain: {topic}"
            ),
        ]
    )

    advantages_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an AI engineer. List 3 important advantages "
                "of the given topic."
            ),
            (
                "human",
                "Topic: {topic}"
            ),
        ]
    )

    explanation_chain = explanation_prompt | llm
    advantages_chain = advantages_prompt | llm

    parallel_chain = RunnableParallel(
        explanation=explanation_chain,
        advantages=advantages_chain,
    )

    return parallel_chain