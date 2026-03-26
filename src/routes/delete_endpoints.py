"""DELETE students endpoints."""

from django.http import JsonResponse

from src.data.students_store import ETUDIANTS_JSON


def delete_etudiant_by_id(request, student_id):
    try:
        parsed_id = int(student_id)
    except (TypeError, ValueError):
        return JsonResponse({"error": "ID invalide."}, status=404)

    student_index = next((idx for idx, item in enumerate(ETUDIANTS_JSON) if item["id"] == parsed_id), None)
    if student_index is None:
        return JsonResponse({"error": "Etudiant introuvable."}, status=404)

    ETUDIANTS_JSON.pop(student_index)
    return JsonResponse({"message": "Etudiant supprime avec succes."}, status=200)

