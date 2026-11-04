from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session

from app.models.entities import (
    CandidateProfileModel,
    ExperienceModel,
    EducationModel,
    SkillModel,
)
from app.models.profile import (
    CandidateProfileCreate,
    CandidateProfileUpdate,
    CandidateProfileResponse,
    ExperienceSchema,
    EducationSchema,
    SkillSchema,
)


class CandidateProfileRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_profile(self, profile_id: UUID | str) -> Optional[CandidateProfileResponse]:
        model = (
            self.db.query(CandidateProfileModel)
            .filter(CandidateProfileModel.id == str(profile_id))
            .first()
        )
        if not model:
            return None
        return self._to_response(model)

    def get_first_profile(self) -> Optional[CandidateProfileResponse]:
        model = self.db.query(CandidateProfileModel).first()
        if not model:
            return None
        return self._to_response(model)

    def create_profile(self, profile_in: CandidateProfileCreate) -> CandidateProfileResponse:
        model = CandidateProfileModel(
            full_name=profile_in.full_name,
            headline=profile_in.headline,
            summary=profile_in.summary,
            email=profile_in.email,
            phone=profile_in.phone,
            location=profile_in.location,
            linkedin_url=profile_in.linkedin_url,
            github_url=profile_in.github_url,
            portfolio_url=profile_in.portfolio_url,
            target_roles=profile_in.target_roles,
            work_modes=[m.value if hasattr(m, "value") else m for m in profile_in.work_modes],
            base_resume_raw=profile_in.base_resume_raw,
        )
        self.db.add(model)
        self.db.flush()

        for exp in profile_in.experiences:
            exp_model = ExperienceModel(
                profile_id=model.id,
                company=exp.company,
                role=exp.role,
                location=exp.location,
                start_date=exp.start_date,
                end_date=exp.end_date,
                is_current=exp.is_current,
                description=exp.description,
                skills_used=exp.skills_used,
                order_index=exp.order_index,
            )
            self.db.add(exp_model)

        for edu in profile_in.educations:
            edu_model = EducationModel(
                profile_id=model.id,
                institution=edu.institution,
                degree=edu.degree,
                field_of_study=edu.field_of_study,
                start_date=edu.start_date,
                end_date=edu.end_date,
                order_index=edu.order_index,
            )
            self.db.add(edu_model)

        for sk in profile_in.skills:
            sk_model = SkillModel(
                profile_id=model.id,
                name=sk.name,
                category=sk.category.value if hasattr(sk.category, "value") else sk.category,
                proficiency_level=sk.proficiency_level,
                evidence=sk.evidence,
            )
            self.db.add(sk_model)

        self.db.commit()
        self.db.refresh(model)
        return self._to_response(model)

    def update_profile(
        self, profile_id: UUID | str, profile_in: CandidateProfileUpdate
    ) -> Optional[CandidateProfileResponse]:
        model = (
            self.db.query(CandidateProfileModel)
            .filter(CandidateProfileModel.id == str(profile_id))
            .first()
        )
        if not model:
            return None

        update_data = profile_in.model_dump(exclude_unset=True)

        for field in [
            "full_name",
            "headline",
            "summary",
            "email",
            "phone",
            "location",
            "linkedin_url",
            "github_url",
            "portfolio_url",
            "target_roles",
            "base_resume_raw",
        ]:
            if field in update_data:
                setattr(model, field, update_data[field])

        if "work_modes" in update_data and update_data["work_modes"] is not None:
            model.work_modes = [
                m.value if hasattr(m, "value") else m for m in update_data["work_modes"]
            ]

        if "experiences" in update_data and update_data["experiences"] is not None:
            self.db.query(ExperienceModel).filter(
                ExperienceModel.profile_id == model.id
            ).delete()
            for exp in profile_in.experiences or []:
                self.db.add(
                    ExperienceModel(
                        profile_id=model.id,
                        company=exp.company,
                        role=exp.role,
                        location=exp.location,
                        start_date=exp.start_date,
                        end_date=exp.end_date,
                        is_current=exp.is_current,
                        description=exp.description,
                        skills_used=exp.skills_used,
                        order_index=exp.order_index,
                    )
                )

        if "educations" in update_data and update_data["educations"] is not None:
            self.db.query(EducationModel).filter(
                EducationModel.profile_id == model.id
            ).delete()
            for edu in profile_in.educations or []:
                self.db.add(
                    EducationModel(
                        profile_id=model.id,
                        institution=edu.institution,
                        degree=edu.degree,
                        field_of_study=edu.field_of_study,
                        start_date=edu.start_date,
                        end_date=edu.end_date,
                        order_index=edu.order_index,
                    )
                )

        if "skills" in update_data and update_data["skills"] is not None:
            self.db.query(SkillModel).filter(
                SkillModel.profile_id == model.id
            ).delete()
            for sk in profile_in.skills or []:
                self.db.add(
                    SkillModel(
                        profile_id=model.id,
                        name=sk.name,
                        category=sk.category.value if hasattr(sk.category, "value") else sk.category,
                        proficiency_level=sk.proficiency_level,
                        evidence=sk.evidence,
                    )
                )

        self.db.commit()
        self.db.refresh(model)
        return self._to_response(model)

    def delete_profile(self, profile_id: UUID | str) -> bool:
        model = (
            self.db.query(CandidateProfileModel)
            .filter(CandidateProfileModel.id == str(profile_id))
            .first()
        )
        if not model:
            return False
        self.db.delete(model)
        self.db.commit()
        return True

    def _to_response(self, model: CandidateProfileModel) -> CandidateProfileResponse:
        return CandidateProfileResponse(
            id=UUID(str(model.id)),
            full_name=model.full_name,
            headline=model.headline,
            summary=model.summary,
            email=model.email,
            phone=model.phone,
            location=model.location,
            linkedin_url=model.linkedin_url,
            github_url=model.github_url,
            portfolio_url=model.portfolio_url,
            target_roles=model.target_roles or [],
            work_modes=model.work_modes or [],
            base_resume_raw=model.base_resume_raw,
            created_at=model.created_at,
            updated_at=model.updated_at,
            experiences=[
                ExperienceSchema(
                    company=e.company,
                    role=e.role,
                    location=e.location,
                    start_date=e.start_date,
                    end_date=e.end_date,
                    is_current=e.is_current,
                    description=e.description,
                    skills_used=e.skills_used or [],
                    order_index=e.order_index,
                )
                for e in model.experiences
            ],
            educations=[
                EducationSchema(
                    institution=ed.institution,
                    degree=ed.degree,
                    field_of_study=ed.field_of_study,
                    start_date=ed.start_date,
                    end_date=ed.end_date,
                    order_index=ed.order_index,
                )
                for ed in model.educations
            ],
            skills=[
                SkillSchema(
                    name=s.name,
                    category=s.category,
                    proficiency_level=s.proficiency_level,
                    evidence=s.evidence,
                )
                for s in model.skills
            ],
        )
