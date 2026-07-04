import pytest


def _auth_headers(client, username="patientuser"):
    client.post("/auth/register", json={"username": username, "password": "secret123"})
    res = client.post(
        "/auth/token",
        data={"username": username, "password": "secret123"},
    )
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def _create_patient(client, headers, **overrides):
    payload = {
        "name": "Ali Khan",
        "age": 30,
        "condition": "Diabetes",
        "risk_score": 50,
        "active": True,
    }
    payload.update(overrides)
    res = client.post("/patients", json=payload, headers=headers)
    return res




def test_create_patient_requires_auth(client):
    res = client.post(
        "/patients",
        json={"name": "Ali", "age": 30, "condition": "Flu", "risk_score": 10},
    )
    assert res.status_code == 401


def test_create_patient_success(client):
    headers = _auth_headers(client, "creator1")
    res = _create_patient(client, headers)
    assert res.status_code == 201
    body = res.json()
    assert body["name"] == "Ali Khan"
    assert body["condition"] == "Diabetes"
    assert "id" in body


@pytest.mark.parametrize(
    "overrides",
    [
        {"age": -1},        
        {"age": 200},       
        {"risk_score": 150},  
        {"name": ""},       
        {"condition": ""},  
    ],
)
def test_create_patient_validation_errors(client, overrides):
    headers = _auth_headers(client, "creator2")
    res = _create_patient(client, headers, **overrides)
    assert res.status_code == 422




def test_get_patient_by_id(client):
    headers = _auth_headers(client, "reader1")
    created = _create_patient(client, headers).json()

    res = client.get(f"/patients/{created['id']}")
    assert res.status_code == 200
    assert res.json()["id"] == created["id"]


def test_get_patient_not_found(client):
    res = client.get("/patients/999999")
    assert res.status_code == 404


def test_list_patients(client):
    headers = _auth_headers(client, "reader2")
    _create_patient(client, headers, name="Sara", condition="Asthma", active=True)
    _create_patient(client, headers, name="Bilal", condition="Asthma", active=False)

    res = client.get("/patients")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_list_patients_filter_by_active(client):
    headers = _auth_headers(client, "reader3")
    _create_patient(client, headers, name="Sana", active=True)
    _create_patient(client, headers, name="Zain", active=False)

    res = client.get("/patients", params={"active": True})
    assert res.status_code == 200
    assert all(p["active"] is True for p in res.json())


def test_list_patients_limit(client):
    headers = _auth_headers(client, "reader4")
    for i in range(5):
        _create_patient(client, headers, name=f"Patient{i}")

    res = client.get("/patients", params={"limit": 2})
    assert res.status_code == 200
    assert len(res.json()) <= 2




def test_put_patient_success(client):
    headers = _auth_headers(client, "updater1")
    created = _create_patient(client, headers).json()

    res = client.put(
        f"/patients/{created['id']}",
        json={
            "name": "Ali Khan Updated",
            "age": 31,
            "condition": "Diabetes Type 2",
            "risk_score": 60,
            "active": False,
        },
        headers=headers,
    )
    assert res.status_code == 200
    assert res.json()["name"] == "Ali Khan Updated"
    assert res.json()["active"] is False


def test_put_patient_not_found(client):
    headers = _auth_headers(client, "updater2")
    res = client.put(
        "/patients/999999",
        json={"name": "X", "age": 1, "condition": "Y", "risk_score": 1},
        headers=headers,
    )
    assert res.status_code == 404


def test_put_patient_requires_auth(client):
    res = client.put(
        "/patients/1",
        json={"name": "X", "age": 1, "condition": "Y", "risk_score": 1},
    )
    assert res.status_code == 401




def test_patch_patient_partial_update(client):
    headers = _auth_headers(client, "patcher1")
    created = _create_patient(client, headers).json()

    res = client.patch(
        f"/patients/{created['id']}",
        json={"risk_score": 90},
        headers=headers,
    )
    assert res.status_code == 200
    body = res.json()
    assert body["risk_score"] == 90
    # untouched fields stay the same
    assert body["name"] == created["name"]


def test_patch_patient_not_found(client):
    headers = _auth_headers(client, "patcher2")
    res = client.patch("/patients/999999", json={"risk_score": 1}, headers=headers)
    assert res.status_code == 404




def test_delete_patient_success(client):
    headers = _auth_headers(client, "deleter1")
    created = _create_patient(client, headers).json()

    res = client.delete(f"/patients/{created['id']}", headers=headers)
    assert res.status_code == 204

    
    follow_up = client.get(f"/patients/{created['id']}")
    assert follow_up.status_code == 404


def test_delete_patient_not_found(client):
    headers = _auth_headers(client, "deleter2")
    res = client.delete("/patients/999999", headers=headers)
    assert res.status_code == 404


def test_delete_patient_requires_auth(client):
    res = client.delete("/patients/1")
    assert res.status_code == 401