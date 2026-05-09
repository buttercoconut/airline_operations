# tests/test_flight.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_and_get_flight():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "flight_number": "AA123",
            "departure_airport": "JFK",
            "arrival_airport": "LAX",
            "departure_time": "2024-10-01T08:00:00Z",
            "arrival_time": "2024-10-01T11:00:00Z",
            "capacity": 200
        }
        r = await ac.post("/flights/", json=payload)
        assert r.status_code == 200
        data = r.json()
        flight_id = data["id"]
        r2 = await ac.get(f"/flights/{flight_id}")
        assert r2.status_code == 200
        assert r2.json()["flight_number"] == "AA123"
