"""POST students endpoints."""

from django.http import JsonResponse

from src.data.students_store import ETUDIANTS_JSON
from src.routes.common import (
    build_validated_student,
    parse_json_body,
    student_to_json,
    validate_payload_required_fields,
)


def create_etudiant(request):
    payload, error_response = parse_json_body(request)
    if error_response is not None:
        return error_response

    error_response = validate_payload_required_fields(payload)
    if error_response is not None:
        return error_response

    incoming_email = str(payload["email"]).strip().lower()
    existing_emails = {str(item["email"]).strip().lower() for item in ETUDIANTS_JSON}
    if incoming_email in existing_emails:
        return JsonResponse({"error": "email deja utilise."}, status=409)

    next_id = (max(item["id"] for item in ETUDIANTS_JSON) + 1) if ETUDIANTS_JSON else 1
    student, error_response = build_validated_student(next_id, payload)
    if error_response is not None:
        return error_response

    created_student = student_to_json(student)
    ETUDIANTS_JSON.append(created_student)
    return JsonResponse(created_student, status=201)

