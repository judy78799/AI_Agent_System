from typing import Any, Optional

class LangfuseClientPlaceholder:
    def __init__(self):
        self.trace_ids = []

    def start_trace(self, query: str) -> str:
        # TODO: 실제 Langfuse 연동 시 구현, trace id 발급
        trace_id = f"trace_{hash(query)}"
        self.trace_ids.append(trace_id)
        return trace_id

    def log_node_execution(self, node_name: str, state: str, latency: float):
        # TODO: 실제 Langfuse 연동 시 구현 (span / generation 기록)
        pass

    def log_validation_result(self, validation_result: Any):
        # TODO: Validation 통과 여부 로깅 이벤트 기록
        pass

    def finish_trace(self, trace_id: str, final_state: str):
        # TODO: Trace 기록 종료 및 최종 상태 갱신
        pass

# Singleton instance for now
langfuse_client = LangfuseClientPlaceholder()
