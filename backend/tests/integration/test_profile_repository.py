import pytest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base
from app.models.profile import (
    CandidateProfileCreate,
    CandidateProfileUpdate,
    ExperienceSchema,
    EducationSchema,
    SkillSchema,
    SkillCategory,
    WorkMode,
)
from app.repositories.profile_repository import CandidateProfileRepository


@pytest.fixture
def db_session():
    # SQLite em memória para testes isolados e rápidos de repositório
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)


def test_create_and_get_profile(db_session):
    repo = CandidateProfileRepository(db_session)
    profile_in = CandidateProfileCreate(
        full_name="Maria Silva",
        headline="Full Stack Developer",
        summary="Especialista em React e Python",
        email="maria@example.com",
        target_roles=["Full Stack Engineer"],
        work_modes=[WorkMode.REMOTE],
        base_resume_raw="# Maria Silva\n\nResumo...",
        experiences=[
            ExperienceSchema(
                company="Empresa A",
                role="Desenvolvedora",
                start_date=date(2021, 1, 1),
                end_date=date(2023, 1, 1),
                is_current=False,
                description="Desenvolvimento web",
                skills_used=["React", "Python"],
            )
        ],
        educations=[
            EducationSchema(
                institution="Faculdade XYZ",
                degree="Graduação",
                field_of_study="Engenharia de Software",
            )
        ],
        skills=[
            SkillSchema(
                name="React",
                category=SkillCategory.TECHNICAL,
                proficiency_level="ADVANCED",
            )
        ],
    )

    created = repo.create_profile(profile_in)
    assert created.id is not None
    assert created.full_name == "Maria Silva"
    assert len(created.experiences) == 1
    assert created.experiences[0].company == "Empresa A"
    assert len(created.educations) == 1
    assert len(created.skills) == 1

    fetched = repo.get_profile(created.id)
    assert fetched is not None
    assert fetched.full_name == "Maria Silva"
    assert fetched.email == "maria@example.com"


def test_update_profile(db_session):
    repo = CandidateProfileRepository(db_session)
    profile_in = CandidateProfileCreate(
        full_name="Maria Silva",
        target_roles=["Dev"],
    )
    created = repo.create_profile(profile_in)

    update_in = CandidateProfileUpdate(
        full_name="Maria Silva Santos",
        headline="Senior Engineer",
    )
    updated = repo.update_profile(created.id, update_in)
    assert updated.full_name == "Maria Silva Santos"
    assert updated.headline == "Senior Engineer"


def test_delete_profile(db_session):
    repo = CandidateProfileRepository(db_session)
    profile_in = CandidateProfileCreate(
        full_name="Maria Silva",
    )
    created = repo.create_profile(profile_in)
    assert repo.get_profile(created.id) is not None

    deleted = repo.delete_profile(created.id)
    assert deleted is True
    assert repo.get_profile(created.id) is None
