"""Service layer for flight operations."""

from sqlalchemy.orm import Session
from datetime import datetime
from app.api.flight.models import FlightCreate, FlightUpdate, Flight
from app.core.database import Base, engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

# Simple ORM model for demonstration
class FlightORM(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, unique=True, index=True)
    origin = Column(String)
    destination = Column(String)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    aircraft_id = Column(Integer)

# Create tables (in real app use migrations)
Base.metadata.create_all(bind=engine)

# Core logic: check availability

def is_flight_available(db: Session, flight_number: str, date: datetime) -> bool:
    """Return True if flight exists and has seats available.
    For demo, we simply check existence.
    """
    flight = db.query(FlightORM).filter(
        FlightORM.flight_number == flight_number,
        FlightORM.departure_time.date() == date.date()
    ).first()
    return flight is not None

# CRUD operations

def create_flight(db: Session, flight_in: FlightCreate) -> FlightORM:
    flight = FlightORM(**flight_in.dict())
    db.add(flight)
    db.commit()
    db.refresh(flight)
    return flight

# Additional update/delete functions omitted for brevity
