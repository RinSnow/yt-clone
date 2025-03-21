"""test_main.py - test cases for the main module."""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """ Test the health check endpoint. """
    response = client.get("/HealthCheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
