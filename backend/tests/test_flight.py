# tests for flight service
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.api.flight.service import create_flight, get_all_flights, get_flight_by_id, is_flight_available
from app.api.flight import models

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")

def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture

def flight_data():
    return models.FlightCreate(
        flight_number="AB123",
        origin="JFK",
        destination="LAX",
        departure_time="2024-01-01T08:00:00",
        arrival_time="2024-01-01T11:00:00",
        aircraft_id=1,
    )

def test_create_and_fetch_flight(db_session, flight_data):
    flight = create_flight(db_session, flight_data)
    assert flight.id is not None
    fetched = get_flight_by_id(db_session, flight.id)
    assert fetched is not None
    assert fetched.flight_number == flight_data.flight_number

def test_availability(db_session, flight_data):
    flight = create_flight(db_session, flight_data)
    assert is_flight_available(db_session, flight.id) is True
    # simulate booking all seats
    flight.seats_available = 0
    db_session.commit()
    assert is_flight_available(db_session, flight.id) is False
