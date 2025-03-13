from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_valid_sales_request():
    response = client.post(
        "/assistance-request/",
        json={"topic": "sales", "description": "Need help with a sale"},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "sent"}


def test_valid_pricing_request():
    response = client.post(
        "/assistance-request/",
        json={"topic": "pricing", "description": "Need help with pricing"},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "sent"}


def test_invalid_topic():
    response = client.post(
        "/assistance-request/",
        json={"topic": "invalid", "description": "Invalid topic"},
    )
    assert response.status_code == 400
