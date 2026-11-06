from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.profile import router as profile_router
from app.core.database import Base, active_database_type, engine
import app.models.entities  # noqa: F401 - registrar modelos no Base.metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Se estiver rodando em SQLite local, garante criação das tabelas
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="JobMatch Agent API",
    description="API local-first para busca e preparação de candidaturas a empregos",
    version="1.0.0",
    lifespan=lifespan,
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
    return {
        "status": "ok",
        "app": "JobMatch Agent",
        "database": active_database_type,
    }
