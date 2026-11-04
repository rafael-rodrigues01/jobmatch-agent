from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.profile import (
    CandidateProfileCreate,
    CandidateProfileUpdate,
    CandidateProfileResponse,
)
from app.repositories.profile_repository import CandidateProfileRepository

router = APIRouter(prefix="/profile", tags=["profile"])


@router.get("", response_model=CandidateProfileResponse)
def get_candidate_profile(db: Session = Depends(get_db)):
    repo = CandidateProfileRepository(db)
    profile = repo.get_first_profile()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Candidate profile not found",
        )
    return profile


@router.put("", response_model=CandidateProfileResponse)
def upsert_candidate_profile(
    profile_data: CandidateProfileCreate,
    db: Session = Depends(get_db),
):
    repo = CandidateProfileRepository(db)
    existing = repo.get_first_profile()
    if existing:
        update_in = CandidateProfileUpdate(
            full_name=profile_data.full_name,
            headline=profile_data.headline,
            summary=profile_data.summary,
            email=profile_data.email,
            phone=profile_data.phone,
            location=profile_data.location,
            linkedin_url=profile_data.linkedin_url,
            github_url=profile_data.github_url,
            portfolio_url=profile_data.portfolio_url,
            target_roles=profile_data.target_roles,
            work_modes=profile_data.work_modes,
            base_resume_raw=profile_data.base_resume_raw,
            experiences=profile_data.experiences,
            educations=profile_data.educations,
            skills=profile_data.skills,
        )
        updated = repo.update_profile(existing.id, update_in)
        if not updated:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update candidate profile",
            )
        return updated
    else:
        return repo.create_profile(profile_data)


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_candidate_profile(db: Session = Depends(get_db)):
    repo = CandidateProfileRepository(db)
    existing = repo.get_first_profile()
    if existing:
        repo.delete_profile(existing.id)
    return None
