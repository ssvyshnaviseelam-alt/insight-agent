from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.agents.llm import get_llm


def create_application_flow():
    llm = get_llm()
    parser = StrOutputParser()

    explanation_prompt = ChatPromptTemplate.from_template(
        "Explain {topic} clearly for a software engineer in 3 sentences."
    )

    question_prompt = ChatPromptTemplate.from_template(
        "Based on this explanation, create one AI Engineer interview "
        "question:\n\n{explanation}"
    )

    key_point_prompt = ChatPromptTemplate.from_template(
        "Give one important interview takeaway from this question:\n\n"
        "{question}"
    )

    explanation_chain = explanation_prompt | llm | parser
    question_chain = question_prompt | llm | parser
    key_point_chain = key_point_prompt | llm | parser

    def build_question(explanation):
        return question_chain.invoke(
            {"explanation": explanation}
        )

    def build_key_point(question):
        return key_point_chain.invoke(
            {"question": question}
        )

    def application_flow(topic):
        explanation = explanation_chain.invoke(
            {"topic": topic}
        )

        question = build_question(explanation)

        key_point = build_key_point(question)

        return {
            "topic": topic,
            "explanation": explanation,
            "interview_question": question,
            "key_point": key_point,
        }

    return application_flow