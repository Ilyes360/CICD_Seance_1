"""API endpoints for students resources."""

from dataclasses import asdict

from django.http import JsonResponse
from django.views.decorators.http import require_GET

from src.data.students_store import get_etudiants


@require_GET
def list_etudiants(request):
    """Return all students in JSON format."""
    students = [asdict(student) for student in get_etudiants()]
    return JsonResponse(students, safe=False, status=200)


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

