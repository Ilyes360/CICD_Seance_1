"""PUT students endpoints."""

from django.http import JsonResponse

from src.data.students_store import ETUDIANTS_JSON
from src.routes.common import (
    build_validated_student,
    parse_json_body,
    student_to_json,
    validate_payload_required_fields,
)


def update_etudiant_by_id(request, student_id):
    try:
        parsed_id = int(student_id)
    except (TypeError, ValueError):
        return JsonResponse({"error": "ID invalide."}, status=400)

    student_index = next((idx for idx, item in enumerate(ETUDIANTS_JSON) if item["id"] == parsed_id), None)
    if student_index is None:
        return JsonResponse({"error": "Etudiant introuvable."}, status=404)

    payload, error_response = parse_json_body(request)
    if error_response is not None:
        return error_response

    error_response = validate_payload_required_fields(payload)
    if error_response is not None:
        return error_response

    incoming_email = str(payload["email"]).strip().lower()
    email_conflict = any(
        str(item["email"]).strip().lower() == incoming_email and item["id"] != parsed_id for item in ETUDIANTS_JSON
    )
    if email_conflict:
        return JsonResponse({"error": "email deja utilise."}, status=409)

    student, error_response = build_validated_student(parsed_id, payload)
    if error_response is not None:
        return error_response

    updated_student = student_to_json(student)
    ETUDIANTS_JSON[student_index] = updated_student
    return JsonResponse(updated_student, status=200)

