from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["message"] == "Governance Demo API is running"
    assert payload["health"] == "/health"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_projects():
    response = client.get("/projects")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["name"] == "Website Redesign"


def test_filter_projects():
    response = client.get("/projects?status=active")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(project["status"] == "active" for project in data)
