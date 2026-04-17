from fastapi import APIRouter

from app.agent.graph import run_agent
from app.schemas.response import AgentResponse

router = APIRouter()


@router.post("/ask", response_model=AgentResponse)
def ask(query: str) -> AgentResponse:
    result = run_agent(query)
    return AgentResponse(
        answer=result.answer,
        state=result.state,
        confidence=result.confidence,
        reason=result.reason or "",
        retries=result.retry_count,
        trace_id=result.trace_id,
    )
