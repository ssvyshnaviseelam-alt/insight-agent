from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.agents.llm import get_llm


def create_composed_chain():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an AI tutor. Explain technical concepts "
                "clearly and briefly."
            ),
            (
                "human",
                "Explain {topic} in 3 sentences."
            ),
        ]
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain