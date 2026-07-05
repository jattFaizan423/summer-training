from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import settings



def test_register(client):
    res = client.post("/auth/register", json={
        "username": "test",
        "password": "123"
    })
    assert res.status_code == 200


def test_login(client):
    client.post("/auth/register", json={
        "username": "test",
        "password": "123"
    })

    res = client.post("/auth/token", data={
        "username": "test",
        "password": "123"
    })

    assert res.status_code == 200
    assert "access_token" in res.json()


def test_token_structure(client):
    client.post("/auth/register", json={
        "username": "test",
        "password": "123"
    })

    res = client.post("/auth/token", data={
        "username": "test",
        "password": "123"
    })

    data = res.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_create_patient_auth(client):
    client.post("/auth/register", json={
        "username": "test",
        "password": "123"
    })

    login = client.post("/auth/token", data={
        "username": "test",
        "password": "123"
    })

    token = login.json()["access_token"]

    res = client.post(
        "/patients",
        json={"name": "Ali", "age": 30, "condition": "Flu", "risk_score": 50},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 201
    assert res.json()["name"] == "Ali"


def test_create_patient_no_auth(client):
    res = client.post(
        "/patients/",
        json={"name": "Ali", "age": 30, "risk_score": 50}
    )

    assert res.status_code == 401


def test_login_invalid(client):
    res = client.post("/auth/token", data={
        "username": "wrong",
        "password": "wrong"
    })

    assert res.status_code == 401


def test_duplicate_user(client):
    client.post("/auth/register", json={
        "username": "test",
        "password": "123"
    })

    res = client.post("/auth/register", json={
        "username": "test",
        "password": "123"
    })

    assert res.status_code in (400, 409)


def test_invalid_token(client):
    res = client.post(
        "/patients/",
        json={"name": "Ali", "age": 30, "risk_score": 50},
        headers={"Authorization": "Bearer invalid"}
    )

    assert res.status_code == 401


def test_invalid_token_format(client):
    res = client.post(
        "/patients/",
        json={"name": "Ali", "age": 30, "risk_score": 50},
        headers={"Authorization": "Bearer"}
    )

    assert res.status_code == 401


def test_register_validation(client):
    res = client.post("/auth/register", json={
        "username": "",
        "password": ""
    })

    assert res.status_code == 422


def test_register_missing_field(client):
    res = client.post("/auth/register", json={
        "username": "test"
    })

    assert res.status_code == 422

def test_get_session_yields_a_session():
    from app.database import get_session

    gen = get_session()
    session = next(gen)
    assert session is not None
    gen.close()


def test_token_without_sub_claim_is_rejected(client):

    bad_token = jwt.encode(
        {"exp": datetime.now(timezone.utc) + timedelta(minutes=5)},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    res = client.post(
        "/patients",
        json={"name": "Ali", "age": 30, "condition": "Flu", "risk_score": 50},
        headers={"Authorization": f"Bearer {bad_token}"},
    )
    assert res.status_code == 401


def test_token_for_nonexistent_user_is_rejected(client):

    ghost_token = jwt.encode(
        {"sub": "ghost_user_does_not_exist",
         "exp": datetime.now(timezone.utc) + timedelta(minutes=5)},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    res = client.post(
        "/patients",
        json={"name": "Ali", "age": 30, "condition": "Flu", "risk_score": 50},
        headers={"Authorization": f"Bearer {ghost_token}"},
    )
    assert res.status_code == 401