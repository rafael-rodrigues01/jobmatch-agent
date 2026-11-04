import uuid
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    String,
    Text,
    Date,
    Boolean,
    Integer,
    DateTime,
    ForeignKey,
    JSON,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class CandidateProfileModel(Base):
    __tablename__ = "candidate_profiles"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    full_name = Column(String(255), nullable=False)
    headline = Column(String(255), nullable=True)
    summary = Column(Text, nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    location = Column(String(255), nullable=True)
    linkedin_url = Column(String(500), nullable=True)
    github_url = Column(String(500), nullable=True)
    portfolio_url = Column(String(500), nullable=True)
    target_roles = Column(JSON, nullable=False, default=list)
    work_modes = Column(JSON, nullable=False, default=list)
    base_resume_raw = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    experiences = relationship(
        "ExperienceModel",
        back_populates="profile",
        cascade="all, delete-orphan",
        order_by="ExperienceModel.order_index",
    )
    educations = relationship(
        "EducationModel",
        back_populates="profile",
        cascade="all, delete-orphan",
        order_by="EducationModel.order_index",
    )
    skills = relationship(
        "SkillModel",
        back_populates="profile",
        cascade="all, delete-orphan",
    )


class ExperienceModel(Base):
    __tablename__ = "experiences"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey("candidate_profiles.id", ondelete="CASCADE"), nullable=False)
    company = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    is_current = Column(Boolean, default=False, nullable=False)
    description = Column(Text, nullable=True)
    skills_used = Column(JSON, default=list, nullable=False)
    order_index = Column(Integer, default=0, nullable=False)

    profile = relationship("CandidateProfileModel", back_populates="experiences")


class EducationModel(Base):
    __tablename__ = "educations"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey("candidate_profiles.id", ondelete="CASCADE"), nullable=False)
    institution = Column(String(255), nullable=False)
    degree = Column(String(255), nullable=False)
    field_of_study = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    order_index = Column(Integer, default=0, nullable=False)

    profile = relationship("CandidateProfileModel", back_populates="educations")


class SkillModel(Base):
    __tablename__ = "skills"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey("candidate_profiles.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    proficiency_level = Column(String(50), nullable=True)
    evidence = Column(Text, nullable=True)

    profile = relationship("CandidateProfileModel", back_populates="skills")
