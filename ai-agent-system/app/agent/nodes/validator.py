from app.agent.state import AgentContext
from app.services.validation_service import ValidationService


validation_service = ValidationService()


def validator_node(ctx: AgentContext) -> AgentContext:
    result = validation_service.validate(ctx.answer, ctx.retrieved_docs)
    ctx.state = result.state
    ctx.confidence = result.confidence
    ctx.reason = result.reason
    return ctx
