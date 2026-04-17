from app.agent.nodes.executor import executor_node
from app.agent.nodes.fallback import fallback_node
from app.agent.nodes.planner import planner_node
from app.agent.nodes.validator import validator_node
from app.agent.policies import should_fail, should_fallback, should_retry
from app.agent.state import AgentContext, RunState


def run_agent(query: str) -> AgentContext:
    ctx = AgentContext(query=query)

    ctx = planner_node(ctx)

    while True:
        ctx = executor_node(ctx)

        if should_fallback(ctx):
            ctx = fallback_node(ctx)
            return ctx

        ctx = validator_node(ctx)

        if ctx.state == RunState.SUCCESS:
            return ctx

        if should_retry(ctx):
            ctx.retry_count += 1
            continue

        if should_fail(ctx):
            ctx.state = RunState.FAIL
            ctx.answer = "The system could not produce a reliable answer."
            ctx.reason = "Validation failed repeatedly."
            return ctx
