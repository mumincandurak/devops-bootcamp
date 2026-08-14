import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_positive(client):
    response = client.post("/models/sentiment", json={"text": "I am feeling great today!"})
    assert response.status_code == 200
    assert response.json()["label"] == "positive"

def test_predict_negative(client):
    response = client.post("/models/sentiment", json={"text": "This is a terrible experience."})
    assert response.status_code == 200
    assert response.json()["label"] == "negative"

def test_predict_empty_is_422(client):
    response = client.post("/models/sentiment", json={"text": ""})
    assert response.status_code == 422