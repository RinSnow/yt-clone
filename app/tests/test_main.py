"""main.py test cases."""

from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_health_check():
    response = client.get("/HealthCheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
