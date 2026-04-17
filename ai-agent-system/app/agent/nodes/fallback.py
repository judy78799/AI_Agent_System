from app.agent.state import AgentContext, RunState


def fallback_node(ctx: AgentContext) -> AgentContext:
    ctx.answer = "I could not find enough supporting context to answer reliably."
    ctx.state = RunState.EMPTY
    ctx.confidence = 0.0
    ctx.reason = "Fallback response returned due to empty retrieval."
    return ctx
