from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.agents.production_agent import (
    agent_graph,
    prepare_agent_state,
)
from app.api.memory_manager import create_thread_config
from app.utils.logger import get_logger

logger = get_logger("InsightAgent.API")

app = FastAPI(
    title="InsightAgent API",
    description="Agentic AI Research and Knowledge Assistant",
    version="1.0.0",
)


class ChatRequest(BaseModel):
    question: str
    user_id: str = "default-user"
    session_id: str = "default-session"


class SourceInfo(BaseModel):
    source_id: int
    source: str
    page: int
    score: float


class ChatResponse(BaseModel):
    answer: str
    user_id: str
    session_id: str
    tool_used: str
    sources: list[SourceInfo] = Field(
        default_factory=list
    )


@app.get("/")
def root():
    return {
        "application": "InsightAgent",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    user_id = request.user_id.strip()
    session_id = request.session_id.strip()
    logger.info(
        "Chat request received | "
        f"user={user_id} | "
        f"session={session_id}"
    )

    if not user_id:
        raise HTTPException(
            status_code=400,
            detail="User ID cannot be empty."
        )

    if not session_id:
        raise HTTPException(
            status_code=400,
            detail="Session ID cannot be empty."
        )

    try:

        state = prepare_agent_state(
            user_id=user_id,
            session_id=session_id,
            question=request.question,
        )

        state = prepare_agent_state(
            user_id=user_id,
            session_id=session_id,
            question=request.question,
        )

        config = create_thread_config(
            user_id=user_id,
            session_id=session_id,
        )

        result = agent_graph.invoke(
            state,
            config=config,
        )

        answer = result.get(
            "answer",
            ""
        )

        tool_used = result.get(
            "tool_used",
            result.get("decision", "unknown"),
        )
        logger.info(
            "Agent tool selected | "
            f"user={user_id} | "
            f"session={session_id} | "
            f"tool={tool_used}"
        )

        sources = result.get(
            "sources",
            []
        )

        if not answer:
            raise HTTPException(
                status_code=500,
                detail="Agent returned an empty answer."
            )

        return ChatResponse(
            answer=answer,
            user_id=user_id,
            session_id=session_id,
            tool_used=tool_used,
            sources=sources,
        )

    except HTTPException:
        raise

    except Exception as e:

        logger.exception(
            "Agent execution error "
            f"for {user_id}:{session_id}"
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to process the request. Please try again."
        )