from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class RunState(str, Enum):
    SUCCESS = "success"
    RETRY = "retry"
    FAIL = "fail"
    EMPTY = "empty"
    GENERATED = "generated"


class AgentContext(BaseModel):
    query: str
    plan: str | None = None

    retrieved_docs: list[str] = Field(default_factory=list)
    answer: str | None = None

    state: RunState | None = None
    reason: str | None = None
    confidence: float = 0.0

    retry_count: int = 0
    max_retries: int = 2

    trace_id: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
