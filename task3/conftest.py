# Present so pytest adds this project directory to sys.path, which lets the
# tests import the application package with `from app.main import app`
# regardless of how pytest is invoked.

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine


sys.path.insert(0, str(Path(__file__).parent))

from app.database import get_session  
from app.main import app  


from sqlalchemy.pool import StaticPool  

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


def _override_get_session():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = _override_get_session


@pytest.fixture(name="client")
def client_fixture():
    SQLModel.metadata.create_all(engine)
    with TestClient(app) as c:
        yield c
    SQLModel.metadata.drop_all(engine)