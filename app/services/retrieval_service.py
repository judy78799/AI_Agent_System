class RetrievalService:
    def retrieve(self, query: str) -> list[str]:
        if "langgraph" in query.lower():
            return [
                "LangGraph is a framework for building stateful, multi-step LLM applications.",
                "It is useful for agent workflows with explicit state transitions."
            ]
        return []
