from langchain_core.output_parsers import StrOutputParser

from app.agents.llm import get_llm
from app.prompts.rag import rag_prompt


def create_rag_chain():
    llm = get_llm()

    chain = (
        rag_prompt
        | llm
        | StrOutputParser()
    )

    return chain