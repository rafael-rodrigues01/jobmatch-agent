import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import declarative_base, sessionmaker

logger = logging.getLogger("jobmatch.database")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/jobmatch_db",
)

Base = declarative_base()


def init_engine(url: str):
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, connect_args=connect_args)


active_database_type = "postgresql"
fallback_sqlite_url = "sqlite:///./jobmatch.db"

try:
    engine = init_engine(DATABASE_URL)
    # Testar conexão ativa imediatamente
    with engine.connect() as conn:
        pass
    logger.info("Conexão estabelecida com sucesso no PostgreSQL.")
except (OperationalError, Exception) as exc:
    logger.warning(
        "Não foi possível conectar ao PostgreSQL em %s (%s). Ativando fallback para SQLite local: %s",
        DATABASE_URL,
        exc,
        fallback_sqlite_url,
    )
    DATABASE_URL = fallback_sqlite_url
    engine = init_engine(DATABASE_URL)
    active_database_type = "sqlite-fallback"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
