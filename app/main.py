from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.risk_scores import router as risk_router

app = FastAPI(
    title="SecureTheCloud RiskDNA API",
    description="Human-to-Cloud Risk Scoring Engine",
    version="1.0.0",
)

app.include_router(health_router, prefix="/health", tags=["Health"])
app.include_router(risk_router, prefix="/risk", tags=["Risk"])
