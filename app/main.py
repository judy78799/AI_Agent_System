import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.route import router as api_router
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # [Startup] 에이전트가 사용할 리소스 초기화 (DB, Redis, LLM 커넥션 등)
    print("🚀 에이전트 시스템을 시작합니다.")
    yield
    # [Shutdown] 리소스 정리
    print("🛑 에이전트 시스템을 종료합니다.")

def create_app() -> FastAPI:
    app = FastAPI(
        title="State-aware AI Agent System",
        description="운영 관측 가능하고 신뢰성 높은 상태 기반 Agent API",
        version="1.0.0",
        lifespan=lifespan
    )
    
    # 1. 미들웨어 설정
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # 2. 라우터 및 엔드포인트 등록
    app.include_router(api_router, prefix="/api")
    
    @app.get("/health")
    async def health_check() -> dict[str, str]:  # type: ignore[reportUnusedFunction]
        return {"status": "healthy"}
        
    # 3. 모든 설정이 끝난 후 마지막에 반환
    return app

app = create_app()

if __name__ == "__main__":
    # 개발 환경에서는 reload=True, 운영 환경에서는 설정을 별도로 관리하세요.
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )