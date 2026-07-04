def test_register(client):
    res = client.post("/auth/register", json={"username": "test", "password": "123"})
    assert res.status_code == 201
    body = res.json()
    assert body["username"] == "test"
    assert "hashed_password" not in body
    assert "password" not in body


def test_login(client):
    client.post("/auth/register", json={"username": "test2", "password": "123"})

    res = client.post("/auth/token", data={"username": "test2", "password": "123"})

    assert res.status_code == 200
    assert "access_token" in res.json()


def test_token_structure(client):
    client.post("/auth/register", json={"username": "test3", "password": "123"})

    res = client.post("/auth/token", data={"username": "test3", "password": "123"})
    data = res.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_create_patient_auth(client):
    client.post("/auth/register", json={"username": "test4", "password": "123"})
    login = client.post("/auth/token", data={"username": "test4", "password": "123"})
    token = login.json()["access_token"]

    res = client.post(
        "/patients",
        json={"name": "Ali", "age": 30, "condition": "Flu", "risk_score": 50},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert res.status_code == 201
    assert res.json()["name"] == "Ali"


def test_create_patient_no_auth(client):
    res = client.post(
        "/patients",
        json={"name": "Ali", "age": 30, "condition": "Flu", "risk_score": 50},
    )
    assert res.status_code == 401


def test_login_invalid(client):
    res = client.post("/auth/token", data={"username": "wrong", "password": "wrong"})
    assert res.status_code == 401


def test_duplicate_user(client):
    client.post("/auth/register", json={"username": "dupe", "password": "123"})
    res = client.post("/auth/register", json={"username": "dupe", "password": "123"})
    assert res.status_code == 409


def test_invalid_token(client):
    res = client.post(
        "/patients",
        json={"name": "Ali", "age": 30, "condition": "Flu", "risk_score": 50},
        headers={"Authorization": "Bearer invalid"},
    )
    assert res.status_code == 401


def test_invalid_token_format(client):
    res = client.post(
        "/patients",
        json={"name": "Ali", "age": 30, "condition": "Flu", "risk_score": 50},
        headers={"Authorization": "Bearer"},
    )
    assert res.status_code == 401


def test_register_validation(client):
    res = client.post("/auth/register", json={"username": "", "password": ""})
    assert res.status_code == 422


def test_register_missing_field(client):
    res = client.post("/auth/register", json={"username": "test5"})
    assert res.status_code == 422