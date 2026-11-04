from datetime import date, datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, Field, model_validator


class WorkMode(str, Enum):
    REMOTE = "REMOTE"
    HYBRID = "HYBRID"
    ON_SITE = "ON_SITE"


class SkillCategory(str, Enum):
    TECHNICAL = "TECHNICAL"
    SOFT_SKILL = "SOFT_SKILL"
    LANGUAGE = "LANGUAGE"


class SkillSchema(BaseModel):
    name: str = Field(..., min_length=1)
    category: SkillCategory
    proficiency_level: Optional[str] = None
    evidence: Optional[str] = None


class EducationSchema(BaseModel):
    institution: str = Field(..., min_length=1)
    degree: str = Field(..., min_length=1)
    field_of_study: str = Field(..., min_length=1)
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    order_index: int = 0


class ExperienceSchema(BaseModel):
    company: str = Field(..., min_length=1)
    role: str = Field(..., min_length=1)
    location: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    is_current: bool = False
    description: Optional[str] = None
    skills_used: List[str] = Field(default_factory=list)
    order_index: int = 0

    @model_validator(mode="after")
    def validate_dates(self) -> "ExperienceSchema":
        if self.is_current and self.end_date is not None:
            raise ValueError("A current role cannot have an end_date")
        if self.end_date is not None and self.start_date > self.end_date:
            raise ValueError("end_date must be after start_date")
        return self


class CandidateProfileBase(BaseModel):
    full_name: str = Field(..., min_length=1)
    headline: Optional[str] = None
    summary: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    target_roles: List[str] = Field(default_factory=list)
    work_modes: List[WorkMode] = Field(default_factory=list)
    base_resume_raw: Optional[str] = None


class CandidateProfileCreate(CandidateProfileBase):
    experiences: List[ExperienceSchema] = Field(default_factory=list)
    educations: List[EducationSchema] = Field(default_factory=list)
    skills: List[SkillSchema] = Field(default_factory=list)


class CandidateProfileUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=1)
    headline: Optional[str] = None
    summary: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    target_roles: Optional[List[str]] = None
    work_modes: Optional[List[WorkMode]] = None
    base_resume_raw: Optional[str] = None
    experiences: Optional[List[ExperienceSchema]] = None
    educations: Optional[List[EducationSchema]] = None
    skills: Optional[List[SkillSchema]] = None


class CandidateProfileResponse(CandidateProfileBase):
    id: UUID
    experiences: List[ExperienceSchema] = Field(default_factory=list)
    educations: List[EducationSchema] = Field(default_factory=list)
    skills: List[SkillSchema] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
