# tests/api/v1/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, API v1!"}
