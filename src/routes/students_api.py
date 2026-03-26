"""HTTP method dispatchers for students API."""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from src.routes.delete_endpoints import delete_etudiant_by_id
from src.routes.get_endpoints import (
    etudiants_stats as get_etudiants_stats,
    get_etudiant_by_id_get,
    list_etudiants,
    search_etudiants as get_search_etudiants,
)
from src.routes.post_endpoints import create_etudiant
from src.routes.put_endpoints import update_etudiant_by_id


@require_http_methods(["GET", "POST"])
def etudiants_collection(request):
    if request.method == "GET":
        return list_etudiants(request)
    if request.method == "POST":
        return create_etudiant(request)
    return JsonResponse({"error": "Methode non autorisee."}, status=405)


@require_http_methods(["GET", "PUT", "DELETE"])
def get_etudiant_by_id(request, student_id):
    if request.method == "GET":
        return get_etudiant_by_id_get(request, student_id)
    if request.method == "PUT":
        return update_etudiant_by_id(request, student_id)
    if request.method == "DELETE":
        return delete_etudiant_by_id(request, student_id)
    return JsonResponse({"error": "Methode non autorisee."}, status=405)


def etudiants_stats(request):
    return get_etudiants_stats(request)


def search_etudiants(request):
    return get_search_etudiants(request)

