from app.agent.state import AgentContext, RunState
from app.services.generation_service import GenerationService
from app.services.retrieval_service import RetrievalService


retrieval_service = RetrievalService()
generation_service = GenerationService()


def executor_node(ctx: AgentContext) -> AgentContext:
    docs = retrieval_service.retrieve(ctx.query)
    ctx.retrieved_docs = docs

    if not docs:
        ctx.state = RunState.EMPTY
        ctx.answer = None
        ctx.reason = "No documents retrieved."
        return ctx

    ctx.answer = generation_service.generate(ctx.query, docs)
    ctx.state = RunState.GENERATED
    return ctx
