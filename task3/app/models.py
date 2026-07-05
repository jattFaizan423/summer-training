from typing import Optional

from sqlmodel import SQLModel, Field


class PatientBase(SQLModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=120)
    condition: str = Field(min_length=1)
    risk_score: int = Field(ge=0, le=100)
    active: bool = True


class Patient(PatientBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class PatientCreate(PatientBase):
    pass


class PatientUpdate(SQLModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    age: Optional[int] = Field(default=None, ge=0, le=120)
    condition: Optional[str] = Field(default=None, min_length=1)
    risk_score: Optional[int] = Field(default=None, ge=0, le=100)
    active: Optional[bool] = None


class PatientRead(PatientBase):
    id: int


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str


class UserCreate(SQLModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)


class UserRead(SQLModel):
    id: int
    username: str
