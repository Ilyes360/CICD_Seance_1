from django.test import Client


def test_delete_with_valid_id_returns_200():
    client = Client()

    response = client.delete("/api/etudiants/1/")

    assert response.status_code == 200


def test_delete_with_non_existing_id_returns_404():
    client = Client()

    response = client.delete("/api/etudiants/9999/")

    assert response.status_code == 404

