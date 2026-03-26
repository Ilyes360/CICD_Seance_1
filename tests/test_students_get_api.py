from django.test import Client

from conftest import INITIAL_STUDENTS


def test_get_students_returns_200_and_array():
    client = Client()

    response = client.get("/api/etudiants/")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_students_returns_initial_students_list():
    client = Client()

    response = client.get("/api/etudiants/")

    assert response.status_code == 200
    assert response.json() == INITIAL_STUDENTS


def test_get_student_by_valid_id_returns_matching_student():
    client = Client()

    response = client.get("/api/etudiants/3/")

    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "firstName": "Vivian",
        "lastName": "Banshee",
        "email": "vivian.banshee@example.com",
        "grade": 12.75,
        "field": "chimie",
    }


def test_get_student_by_non_existing_id_returns_404():
    client = Client()

    response = client.get("/api/etudiants/9999/")

    assert response.status_code == 404


def test_get_student_by_invalid_id_returns_400():
    client = Client()

    response = client.get("/api/etudiants/abc/")

    assert response.status_code == 400


def test_get_students_stats_returns_expected_fields():
    client = Client()

    response = client.get("/api/etudiants/stats/")

    assert response.status_code == 200
    data = response.json()
    assert "totalStudents" in data
    assert "averageGrade" in data
    assert "studentsByField" in data
    assert "bestStudent" in data


def test_get_students_search_with_term_returns_matching_students():
    client = Client()

    response = client.get("/api/etudiants/search/?term=vi")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert any(
        "vi" in student["firstName"].lower() or "vi" in student["lastName"].lower() for student in data
    )

