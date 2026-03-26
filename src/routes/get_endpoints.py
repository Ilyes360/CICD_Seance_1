"""GET students endpoints."""

from django.http import JsonResponse

from src.data.students_store import get_etudiants
from src.routes.common import student_to_json


def list_etudiants(request):
    students = [student_to_json(student) for student in get_etudiants()]
    return JsonResponse(students, safe=False, status=200)


def get_etudiant_by_id_get(request, student_id):
    try:
        parsed_id = int(student_id)
    except (TypeError, ValueError):
        return JsonResponse({"error": "ID invalide."}, status=400)

    students = get_etudiants()
    student = next((item for item in students if item.id == parsed_id), None)
    if student is None:
        return JsonResponse({"error": "Etudiant introuvable."}, status=404)

    return JsonResponse(student_to_json(student), status=200)


def etudiants_stats(request):
    students = get_etudiants()
    total_students = len(students)
    if total_students == 0:
        return JsonResponse(
            {"totalStudents": 0, "averageGrade": 0.0, "studentsByField": {}, "bestStudent": 0.0},
            status=200,
        )

    average_grade = round(sum(student.grade for student in students) / total_students, 2)
    students_by_field = {}
    for student in students:
        students_by_field[student.field] = students_by_field.get(student.field, 0) + 1
    best_grade = max(student.grade for student in students)

    return JsonResponse(
        {
            "totalStudents": total_students,
            "averageGrade": average_grade,
            "studentsByField": students_by_field,
            "bestStudent": best_grade,
        },
        status=200,
    )


def search_etudiants(request):
    term = request.GET.get("term")
    if term is None or term.strip() == "":
        return JsonResponse({"error": "Le parametre 'term' est obligatoire et non vide."}, status=400)

    normalized_term = term.strip().lower()
    matches = [
        student_to_json(student)
        for student in get_etudiants()
        if normalized_term in student.firstName.lower() or normalized_term in student.lastName.lower()
    ]
    return JsonResponse(matches, safe=False, status=200)

