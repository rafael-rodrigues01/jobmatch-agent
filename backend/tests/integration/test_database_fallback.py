import os
from sqlalchemy import create_engine
from app.core.database import init_engine, fallback_sqlite_url


def test_sqlite_fallback_initialization():
    engine = init_engine(fallback_sqlite_url)
    assert engine is not None
    with engine.connect() as conn:
        assert conn is not None

