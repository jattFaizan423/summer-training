from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from app.auth import create_access_token, hash_password, verify_password
from app.database import get_session
from app.models import User, UserCreate, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=UserRead,
    summary="Register a new user",
)
def register(user: UserCreate, session: Session = Depends(get_session)):
    existing = session.exec(
        select(User).where(User.username == user.username)
    ).first()

    if existing:
        raise HTTPException(status.HTTP_409_CONFLICT, "Username already exists")

    new_user = User(
        username=user.username,
        hashed_password=hash_password(user.password),
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@router.post(
    "/token",
    summary="Log in and obtain a JWT access token",
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.exec(
        select(User).where(User.username == form_data.username)
    ).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}