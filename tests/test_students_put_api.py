from django.test import Client


def test_put_valid_data_returns_200_and_updated_student():
    client = Client()
    payload = {
        "firstName": "Orphie",
        "lastName": "Magnusson",
        "email": "orphie.magnusson@example.com",
        "grade": 19.2,
        "field": "informatique",
    }

    response = client.put("/api/etudiants/1/", data=payload, content_type="application/json")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "firstName": "Orphie",
        "lastName": "Magnusson",
        "email": "orphie.magnusson@example.com",
        "grade": 19.2,
        "field": "informatique",
    }


def test_put_with_non_existing_id_returns_404():
    client = Client()
    payload = {
        "firstName": "Ghost",
        "lastName": "Student",
        "email": "ghost.student@example.com",
        "grade": 11.0,
        "field": "chimie",
    }

    response = client.put("/api/etudiants/9999/", data=payload, content_type="application/json")

    assert response.status_code == 404

