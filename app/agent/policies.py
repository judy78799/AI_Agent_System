from app.agent.state import AgentContext, RunState


def should_retry(ctx: AgentContext) -> bool:
    return ctx.state == RunState.RETRY and ctx.retry_count < ctx.max_retries


def should_fallback(ctx: AgentContext) -> bool:
    return ctx.state == RunState.EMPTY


def should_fail(ctx: AgentContext) -> bool:
    return ctx.state == RunState.FAIL or (
        ctx.state == RunState.RETRY and ctx.retry_count >= ctx.max_retries
    )
