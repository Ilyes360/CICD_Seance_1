from django.test import Client


def test_post_valid_data_returns_201_and_student_with_id():
    client = Client()
    payload = {
        "firstName": "Nora",
        "lastName": "Elm",
        "email": "nora.elm@example.com",
        "grade": 17.25,
        "field": "chimie",
    }

    response = client.post("/api/etudiants/", data=payload, content_type="application/json")

    assert response.status_code == 201
    data = response.json()
    assert isinstance(data.get("id"), int)
    assert data["firstName"] == payload["firstName"]
    assert data["lastName"] == payload["lastName"]
    assert data["email"] == payload["email"]
    assert data["grade"] == payload["grade"]
    assert data["field"] == payload["field"]


def test_post_without_required_field_returns_400():
    client = Client()
    payload = {
        "firstName": "Nora",
        "email": "nora.elm@example.com",
        "grade": 17.25,
        "field": "chimie",
    }

    response = client.post("/api/etudiants/", data=payload, content_type="application/json")

    assert response.status_code == 400


def test_post_with_invalid_grade_returns_400():
    client = Client()
    payload = {
        "firstName": "Nora",
        "lastName": "Elm",
        "email": "nora.grade@example.com",
        "grade": 25,
        "field": "chimie",
    }

    response = client.post("/api/etudiants/", data=payload, content_type="application/json")

    assert response.status_code == 400


def test_post_with_existing_email_returns_409():
    client = Client()
    payload = {
        "firstName": "Other",
        "lastName": "Person",
        "email": "orphie.magnusson@example.com",
        "grade": 14,
        "field": "informatique",
    }

    response = client.post("/api/etudiants/", data=payload, content_type="application/json")

    assert response.status_code == 409

