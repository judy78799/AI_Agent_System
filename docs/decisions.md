# Architecture & Technical Decisions

## 1. 계층 분리 구조 (Layered Architecture)
본 프로젝트는 시스템의 신뢰성과 유지보수성을 극대화하기 위해 역할을 명확히 4계층으로 분리합니다.
- **agent/**: 제어 흐름(LangGraph 노드 및 라우팅 상태 제어) 전용. 내부 RAG 디테일 몰라도 됨.
- **services/**: 실제 비즈니스 로직(검색, 생성, 검증 및 조합) 전담. 
- **infrastructure/**: 외부 종속성(LLM API, Langfuse, VectorDB)을 교체 가능하도록 격리.
- **schemas/**: 시스템 내외부의 데이터 전달 형태, API Spec 고정. 시스템의 설계 언어 역할을 수행.

## 2. 상태 머신(State Machine) 기반 흐름 제어
LLM의 결과를 무조건 수용하는 대신 `SUCCESS`, `RETRY`, `FAIL`, `EMPTY`라는 4가지 상태를 기반으로 흐름을 결정합니다.
- 상태 기반으로 설계하여, "왜 재시도가 발생했는지"와 "언제 중단해야 하는지"가 명확해집니다.
- 무한 루프를 방지하기 위해 최대 재시도(Retry Count)를 제한합니다.

## 3. 검증(Validator) 계층 독립 
- 모델의 생성 결과(answer)를 즉시 반환하지 않고, 반드시 Validator를 통과합니다.
- `ValidationResult` 구조화: 규칙 기반 검증(Answer 여부, Confidence 측정) 및 LLM 기반(환각 현상 확인) 검증에서 떨어진 항목을 `issues`에 기록합니다.
- 이 기록은 실패 원인 분석이나 다음 Executor 재시도 시 시스템 Prompt의 피드백 용도로 사용됩니다.

## 4. 관측 가능성 (Observability) 내재화
- 블랙박스가 될 수 있는 내부 로직을 해소하기 위해 `infrastructure/tracing` 계층에 Langfuse 클라이언트 인터페이스를 초기부터 마련했습니다.
- 입력에서 반환까지의 Trace ID 발급과 Node Execution 별 latency, state 로그 기록, Validation 실패 지점을 투명하게 기록하기 위한 의사결정입니다.
