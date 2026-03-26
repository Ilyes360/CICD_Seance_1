"""In-memory JSON-like storage for Etudiant."""

from copy import deepcopy

from src.app.models import Etudiant

# JSON-like array stored in memory (you can edit values freely).
ETUDIANTS_JSON = [
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

_INITIAL_ETUDIANTS_JSON = deepcopy(ETUDIANTS_JSON)


def reset_etudiants_data() -> None:
    """Reset in-memory data to its original order and values."""
    ETUDIANTS_JSON.clear()
    ETUDIANTS_JSON.extend(deepcopy(_INITIAL_ETUDIANTS_JSON))


def get_etudiants() -> list[Etudiant]:
    """Return validated student objects from in-memory JSON array."""
    students = [Etudiant(**item) for item in ETUDIANTS_JSON]
    for student in students:
        student.validate()
    return students

