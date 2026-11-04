import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.pool import StaticPool
from app.core.database import Base, get_db
from app.main import app as fastapi_app
import app.models.entities  # assegura que os modelos ORM estão registrados no Base.metadata


@pytest.fixture
def client_and_db():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    fastapi_app.dependency_overrides[get_db] = override_get_db
    client = TestClient(fastapi_app)
    try:
        yield client
    finally:
        fastapi_app.dependency_overrides.clear()
        Base.metadata.drop_all(engine)


def test_get_profile_when_empty_returns_404(client_and_db):
    response = client_and_db.get("/api/v1/profile")
    assert response.status_code == 404
    assert response.json()["detail"] == "Candidate profile not found"


def test_create_and_get_profile(client_and_db):
    payload = {
        "full_name": "Ana Developer",
        "headline": "Fullstack Python & React",
        "email": "ana@example.com",
        "target_roles": ["Fullstack Developer"],
        "work_modes": ["REMOTE"],
        "experiences": [
            {
                "company": "Tech Inova",
                "role": "Engenheira de Software",
                "start_date": "2022-01-01",
                "is_current": True,
                "skills_used": ["Python", "FastAPI", "React"],
            }
        ],
        "skills": [
            {
                "name": "Python",
                "category": "TECHNICAL",
                "proficiency_level": "ADVANCED",
            }
        ],
    }

    # Criar via POST / PUT
    create_res = client_and_db.put("/api/v1/profile", json=payload)
    assert create_res.status_code == 200
    created_data = create_res.json()
    assert created_data["full_name"] == "Ana Developer"
    assert len(created_data["experiences"]) == 1
    assert created_data["experiences"][0]["company"] == "Tech Inova"

    # Buscar via GET
    get_res = client_and_db.get("/api/v1/profile")
    assert get_res.status_code == 200
    assert get_res.json()["email"] == "ana@example.com"


def test_delete_profile(client_and_db):
    payload = {"full_name": "Ana Developer"}
    client_and_db.put("/api/v1/profile", json=payload)

    # Deletar perfil
    delete_res = client_and_db.delete("/api/v1/profile")
    assert delete_res.status_code == 204

    # Verificar que agora está 404
    get_res = client_and_db.get("/api/v1/profile")
    assert get_res.status_code == 404
