import pytest

from src.data.students_store import reset_etudiants_data

INITIAL_STUDENTS = [
    {
        "id": 1,
        "firstName": "Orphie",
        "lastName": "Magnusson",
        "email": "orphie.magnusson@example.com",
        "grade": 14.5,
        "field": "informatique",
    },
    {
        "id": 2,
        "firstName": "Corin",
        "lastName": "Wickes",
        "email": "corin.wickes@example.com",
        "grade": 16.0,
        "field": "physique",
    },
    {
        "id": 3,
        "firstName": "Vivian",
        "lastName": "Banshee",
        "email": "vivian.banshee@example.com",
        "grade": 12.75,
        "field": "chimie",
    },
    {
        "id": 4,
        "firstName": "Manato",
        "lastName": "Komano",
        "email": "manato.komano@example.com",
        "grade": 18.25,
        "field": "physique",
    },
    {
        "id": 5,
        "firstName": "Yanagi",
        "lastName": "Tsukishiro",
        "email": "samir.belkacem@example.com",
        "grade": 10.0,
        "field": "mathematiques",
    },
]


@pytest.fixture(autouse=True)
def reset_students_data():
    reset_etudiants_data()

