from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.agents.llm import get_llm


def create_output_passing_chain():
    llm = get_llm()
    parser = StrOutputParser()

    explanation_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an AI tutor. Explain the technical topic "
                "clearly in 3 sentences."
            ),
            (
                "human",
                "Explain: {topic}"
            ),
        ]
    )

    interview_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a senior AI engineering interviewer."
            ),
            (
                "human",
                "Based on the following explanation, create "
                "one interview question:\n\n{explanation}"
            ),
        ]
    )

    explanation_chain = explanation_prompt | llm | parser
    interview_chain = interview_prompt | llm | parser

    chain = (
        explanation_chain
        | (lambda explanation: {"explanation": explanation})
        | interview_chain
    )

    return chain