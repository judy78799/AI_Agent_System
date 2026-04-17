from pydantic import BaseModel

from app.agent.state import RunState


class AgentResponse(BaseModel):
    answer: str | None
    state: RunState
    confidence: float
    reason: str
    retries: int
    trace_id: str | None = None
