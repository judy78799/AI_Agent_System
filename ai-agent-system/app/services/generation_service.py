class GenerationService:
    def generate(self, query: str, docs: list[str]) -> str:
        if not docs:
            return ""
        context = " ".join(docs)
        return f"Question: {query}\nAnswer based on context: {context}"
