from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.profile import router as profile_router

app = FastAPI(
    title="JobMatch Agent API",
    description="API local-first para busca e preparação de candidaturas a empregos",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile_router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok", "app": "JobMatch Agent"}
