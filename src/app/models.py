"""Domain model for student data."""

from dataclasses import dataclass

ALLOWED_FIELDS = {"informatique", "mathematiques", "physique", "chimie"}


@dataclass(slots=True)
class Etudiant:
    id: int
    firstName: str
    lastName: str
    email: str
    grade: float
    field: str

    def validate(self) -> None:
        if len(self.firstName.strip()) < 2:
            raise ValueError("firstName doit contenir au moins 2 caracteres.")
        if len(self.lastName.strip()) < 2:
            raise ValueError("lastName doit contenir au moins 2 caracteres.")
        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            raise ValueError("email doit avoir un format valide.")
        if not 0 <= self.grade <= 20:
            raise ValueError("grade doit etre compris entre 0 et 20.")
        if self.field not in ALLOWED_FIELDS:
            raise ValueError(
                "field doit etre l'une des valeurs: informatique, mathematiques, physique, chimie."
            )

