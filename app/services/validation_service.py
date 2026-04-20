from pydantic import BaseModel

from app.agent.state import RunState
from app.schemas.validation import ValidationResult


class ValidationService:
    """검증 로직만 담당"""
    def validate(self, answer: str | None, docs: list[str]) -> ValidationResult:
        if not docs:
            return ValidationResult(
                state=RunState.EMPTY,
                confidence=0.0,
                reason="No retrieved documents found.",
                issues=["empty_retrieval"],
            )

        if not answer or not answer.strip():
            return ValidationResult(
                state=RunState.FAIL,
                confidence=0.0,
                reason="Generation returned an empty answer.",
                issues=["empty_answer"],
            )

        grounded = any(doc.lower() in answer.lower() for doc in docs[:1])
        if not grounded:
            return ValidationResult(
                state=RunState.RETRY,
                confidence=0.45,
                reason="Answer is not sufficiently grounded in retrieved context.",
                issues=["grounding_failed"],
            )

        return ValidationResult(
            state=RunState.SUCCESS,
            confidence=0.86,
            reason="Answer passed validation.",
            issues=[],
        )
