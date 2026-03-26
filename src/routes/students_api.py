"""API endpoints for students resources."""

import json
from dataclasses import asdict

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_http_methods

from src.app.models import Etudiant
from src.data.students_store import ETUDIANTS_JSON, get_etudiants


@require_http_methods(["GET", "POST"])
def etudiants_collection(request):
    """Handle listing and creation of students."""
    if request.method == "GET":
        students = [asdict(student) for student in get_etudiants()]
        return JsonResponse(students, safe=False, status=200)

    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (TypeError, ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "Body JSON invalide."}, status=400)

    required_fields = {"firstName", "lastName", "email", "grade", "field"}
    missing_fields = [field for field in required_fields if field not in payload]
    if missing_fields:
        return JsonResponse(
            {"error": f"Champs obligatoires manquants: {', '.join(sorted(missing_fields))}."},
            status=400,
        )

    if any(str(payload[field]).strip() == "" for field in ["firstName", "lastName", "email", "field"]):
        return JsonResponse({"error": "Tous les champs sont obligatoires."}, status=400)

    try:
        grade_value = float(payload["grade"])
    except (TypeError, ValueError):
        return JsonResponse({"error": "grade doit etre un nombre entre 0 et 20."}, status=400)

    existing_emails = {str(item["email"]).strip().lower() for item in ETUDIANTS_JSON}
    incoming_email = str(payload["email"]).strip().lower()
    if incoming_email in existing_emails:
        return JsonResponse({"error": "email deja utilise."}, status=409)

    next_id = (max(item["id"] for item in ETUDIANTS_JSON) + 1) if ETUDIANTS_JSON else 1
    candidate = Etudiant(
        id=next_id,
        firstName=str(payload["firstName"]).strip(),
        lastName=str(payload["lastName"]).strip(),
        email=str(payload["email"]).strip(),
        grade=grade_value,
        field=str(payload["field"]).strip(),
    )

    try:
        candidate.validate()
    except ValueError as error:
        return JsonResponse({"error": str(error)}, status=400)

    created_student = asdict(candidate)
    ETUDIANTS_JSON.append(created_student)
    return JsonResponse(created_student, status=201)


@require_GET
def get_etudiant_by_id(request, student_id):
    """Return one student by id with explicit 400/404 handling."""
    try:
        parsed_id = int(student_id)
    except (TypeError, ValueError):
        return JsonResponse({"error": "ID invalide: un nombre est attendu."}, status=400)

    students = get_etudiants()
    student = next((item for item in students if item.id == parsed_id), None)
    if student is None:
        return JsonResponse({"error": "Etudiant introuvable."}, status=404)

    return JsonResponse(asdict(student), status=200)

