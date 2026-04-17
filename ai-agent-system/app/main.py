from fastapi import FastAPI
from app.api.route import router as api_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="State-aware AI Agent System",
        description="운영 관측 가능하고 신뢰성 높은 상태 기반 Agent API",
        version="1.0.0"
    )
    
    app.include_router(api_router, prefix="/api")
    
    return app

app = create_app()
