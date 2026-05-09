import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def create_flight():
    payload = {
        "flight_number": "AA123",
        "origin": "JFK",
        "destination": "LAX",
        "departure_time": "2024-10-01T08:00:00Z",
        "arrival_time": "2024-10-01T11:00:00Z",
        "total_seats": 200
    }
    response = client.post("/flights/", json=payload)
    assert response.status_code == 201
    return response.json()

def test_get_flight(create_flight):
    flight_id = create_flight["id"]
    response = client.get(f"/flights/{flight_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["flight_number"] == "AA123"

def test_check_availability(create_flight):
    flight_id = create_flight["id"]
    payload = {"flight_id": flight_id, "seats_requested": 50}
    response = client.post("/flights/availability", json=payload)
    assert response.status_code == 200
    assert response.json()["available"] is True
