from app.agent.state import AgentContext


def planner_node(ctx: AgentContext) -> AgentContext:
    if "search" in ctx.query.lower() or "find" in ctx.query.lower():
        ctx.plan = "rag"
    else:
        ctx.plan = "rag"
    return ctx
