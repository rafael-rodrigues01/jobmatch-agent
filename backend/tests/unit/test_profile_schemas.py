import pytest
from datetime import date
from pydantic import ValidationError

from app.models.profile import (
    CandidateProfileCreate,
    CandidateProfileUpdate,
    CandidateProfileResponse,
    ExperienceSchema,
    EducationSchema,
    SkillSchema,
    SkillCategory,
    WorkMode,
)


def test_experience_valid_creation():
    exp = ExperienceSchema(
        company="Tech Corp",
        role="Senior Backend Engineer",
        start_date=date(2022, 1, 1),
        end_date=date(2024, 1, 1),
        is_current=False,
        description="Desenvolvimento de microsserviços em Python e FastAPI.",
        skills_used=["Python", "FastAPI", "PostgreSQL"],
    )
    assert exp.company == "Tech Corp"
    assert exp.is_current is False
    assert len(exp.skills_used) == 3


def test_experience_end_date_before_start_date_fails():
    with pytest.raises(ValidationError) as exc_info:
        ExperienceSchema(
            company="Tech Corp",
            role="Backend Engineer",
            start_date=date(2023, 1, 1),
            end_date=date(2022, 1, 1),
            is_current=False,
        )
    assert "end_date must be after start_date" in str(exc_info.value)


def test_experience_current_role_cannot_have_end_date():
    with pytest.raises(ValidationError) as exc_info:
        ExperienceSchema(
            company="Tech Corp",
            role="Backend Engineer",
            start_date=date(2023, 1, 1),
            end_date=date(2024, 1, 1),
            is_current=True,
        )
    assert "current role cannot have an end_date" in str(exc_info.value)


def test_education_valid_creation():
    edu = EducationSchema(
        institution="Universidade de São Paulo",
        degree="Bacharelado",
        field_of_study="Ciência da Computação",
        start_date=date(2018, 1, 1),
        end_date=date(2022, 12, 31),
    )
    assert edu.institution == "Universidade de São Paulo"
    assert edu.degree == "Bacharelado"


def test_skill_valid_creation():
    skill = SkillSchema(
        name="Python",
        category=SkillCategory.TECHNICAL,
        proficiency_level="ADVANCED",
        evidence="5 anos de desenvolvimento web e automação",
    )
    assert skill.name == "Python"
    assert skill.category == SkillCategory.TECHNICAL


def test_candidate_profile_create_requires_full_name():
    with pytest.raises(ValidationError):
        CandidateProfileCreate(full_name="")


def test_candidate_profile_create_success():
    profile = CandidateProfileCreate(
        full_name="Rafael Dev",
        headline="Software Engineer",
        summary="Desenvolvedor focado em Python e automações.",
        email="rafael@example.com",
        target_roles=["Backend Engineer", "Software Engineer"],
        work_modes=[WorkMode.REMOTE, WorkMode.HYBRID],
        base_resume_raw="# Rafael Dev\n\nExperiência em Python...",
    )
    assert profile.full_name == "Rafael Dev"
    assert len(profile.target_roles) == 2
    assert WorkMode.REMOTE in profile.work_modes
