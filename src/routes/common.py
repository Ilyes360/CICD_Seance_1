"""Shared helpers for students API endpoints."""

import json
from dataclasses import asdict

from django.http import JsonResponse

from src.app.models import Etudiant


def parse_json_body(request):
    """Parse request JSON body or return a 400 response."""
    try:
        return json.loads(request.body.decode("utf-8")), None
    except (TypeError, ValueError, UnicodeDecodeError):
        return None, JsonResponse({"error": "Body JSON invalide."}, status=400)


def validate_payload_required_fields(payload):
    """Validate required fields and non-empty string fields."""
    required_fields = {"firstName", "lastName", "email", "grade", "field"}
    missing_fields = [field for field in required_fields if field not in payload]
    if missing_fields:
        return JsonResponse(
            {"error": f"Champs obligatoires manquants: {', '.join(sorted(missing_fields))}."},
            status=400,
        )

    if any(str(payload[field]).strip() == "" for field in ["firstName", "lastName", "email", "field"]):
        return JsonResponse({"error": "Tous les champs sont obligatoires."}, status=400)

    return None


def build_validated_student(student_id, payload):
    """Build and validate an Etudiant instance from payload."""
    try:
        grade_value = float(payload["grade"])
    except (TypeError, ValueError):
        return None, JsonResponse({"error": "grade doit etre un nombre entre 0 et 20."}, status=400)

    candidate = Etudiant(
        id=student_id,
        firstName=str(payload["firstName"]).strip(),
        lastName=str(payload["lastName"]).strip(),
        email=str(payload["email"]).strip(),
        grade=grade_value,
        field=str(payload["field"]).strip(),
    )
    try:
        candidate.validate()
    except ValueError as error:
        return None, JsonResponse({"error": str(error)}, status=400)

    return candidate, None


def student_to_json(student):
    return asdict(student)

