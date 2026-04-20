from app.agent.state import AgentContext, RunState
from app.services.validation_service import ValidationService


validation_service = ValidationService()


def validator_node(ctx: AgentContext) -> AgentContext:
    result = validation_service.validate(ctx.answer, ctx.retrieved_docs)

    ctx.state = result.state
    ctx.confidence = result.confidence
    ctx.reason = result.reason

    if ctx.state == RunState.RETRY:
        ctx.retry_count += 1
        if ctx.retry_count > ctx.max_retries:
            ctx.state = RunState.FAIL
            ctx.reason = "Validation failed repeatedly."

    return ctx
