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
    query: str = Field(..., description="사용자 입력 질문")
    plan: Optional[str] = Field(default=None, description="실행 계획")

    retrieved_docs: list[str] = Field(default_factory=list, description="검색된 문서 목록")
    answer: Optional[str] = Field(default=None, description="생성된 답변")
    is_valid: Optional[bool] = Field(default=None, description="답변 유효성")

    state: Optional[RunState] = None
    reason: str | None = None
    confidence: Optional[float] = None

    retry_count: int = 0
    max_retries: int = 2

    trace_id: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


# TODO: 나중에 app/schemas/plan.py로 분리
class PlanResult(BaseModel):
    strategy: str
    tool_required: bool = False
    retrieval_required: bool = True
