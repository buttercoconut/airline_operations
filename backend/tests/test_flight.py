# tests/test_flight.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def create_flight():
    payload = {
        "flight_number": "AB123",
        "origin": "NYC",
        "destination": "LAX",
        "departure_time": "2025-12-01T08:00:00",
        "arrival_time": "2025-12-01T11:00:00"
    }
    response = client.post("/flights/", json=payload)
    assert response.status_code == 200
    return response.json()

def test_create_and_get_flight(create_flight):
    flight_id = create_flight["id"]
    response = client.get(f"/flights/{flight_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["flight_number"] == "AB123"
