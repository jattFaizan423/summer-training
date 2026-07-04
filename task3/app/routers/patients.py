from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.auth import get_current_user
from app.database import get_session
from app.models import Patient, PatientCreate, PatientRead, PatientUpdate, User

router = APIRouter(prefix="/patients", tags=["patients"])


@router.get(
    "",
    response_model=list[PatientRead],
    summary="List patients",
    description="List patients, optionally filtered by active status or "
    "condition, with pagination via limit/offset.",
)
def list_patients(
    active: Optional[bool] = None,
    condition: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
    session: Session = Depends(get_session),
):
    query = select(Patient)

    if active is not None:
        query = query.where(Patient.active == active)
    if condition is not None:
        query = query.where(Patient.condition == condition)

    query = query.offset(offset).limit(limit)
    return session.exec(query).all()


@router.get(
    "/{patient_id}",
    response_model=PatientRead,
    summary="Get a single patient",
)
def get_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Patient not found")
    return patient


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=PatientRead,
    summary="Create a patient",
)
def create_patient(
    data: PatientCreate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    patient = Patient.model_validate(data)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.put(
    "/{patient_id}",
    response_model=PatientRead,
    summary="Replace a patient (full update)",
)
def replace_patient(
    patient_id: int,
    data: PatientCreate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Patient not found")

    for key, value in data.model_dump().items():
        setattr(patient, key, value)

    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.patch(
    "/{patient_id}",
    response_model=PatientRead,
    summary="Partially update a patient",
)
def update_patient(
    patient_id: int,
    data: PatientUpdate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Patient not found")

    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)

    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.delete(
    "/{patient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a patient",
)
def delete_patient(
    patient_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Patient not found")

    session.delete(patient)
    session.commit()
    return None