from pydantic import BaseModel, Field
from app.agent.state import RunState


class ValidationResult(BaseModel):
    """validator 결과 계약 담당"""
    state: RunState
    confidence: float
    reason: str
    issues: list[str] = Field(default_factory=list)
