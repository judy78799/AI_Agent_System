from fastapi import APIRouter

from app.agent.graph import run_agent
from app.schemas.response import AgentResponse
from app.agent.state import RunState

router = APIRouter()


@router.post("/ask", response_model=AgentResponse)
def ask(query: str) -> AgentResponse:
    result = run_agent(query)

    return AgentResponse(
    answer=getattr(result, "answer", None),
    state=getattr(result, "state", RunState.FAIL),
    confidence=getattr(result, "confidence", 0.0),
    reason=getattr(result, "reason", ""),
    retries=getattr(result, "retry_count", 0),
    trace_id=getattr(result, "trace_id", None),
    )
