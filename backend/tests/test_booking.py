# tests/test_booking.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def create_flight():
    payload = {
        "flight_number": "CD456",
        "origin": "SFO",
        "destination": "SEA",
        "departure_time": "2025-12-02T09:00:00",
        "arrival_time": "2025-12-02T10:30:00"
    }
    response = client.post("/flights/", json=payload)
    assert response.status_code == 200
    return response.json()

@pytest.fixture
def create_booking(create_flight):
    flight_id = create_flight["id"]
    payload = {
        "flight_id": flight_id,
        "passenger_name": "John Doe",
        "seat_number": "12A"
    }
    response = client.post("/bookings/", json=payload)
    assert response.status_code == 200
    return response.json()

def test_create_and_get_booking(create_booking):
    booking_id = create_booking["id"]
    response = client.get(f"/bookings/{booking_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["passenger_name"] == "John Doe"
