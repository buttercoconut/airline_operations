from sqlalchemy.orm import Session
from app.api.flight import models
from app.core.database import Base
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
    aircraft_id = Column(Integer, ForeignKey("aircrafts.id"))
    seats_total = Column(Integer, default=180)
    seats_available = Column(Integer, default=180)

# Service functions

def create_flight(db: Session, flight_in: models.FlightCreate) -> models.Flight:
    flight = FlightORM(**flight_in.dict())
    db.add(flight)
    db.commit()
    db.refresh(flight)
    return models.Flight.from_orm(flight)


def get_all_flights(db: Session):
    flights = db.query(FlightORM).all()
    return [models.Flight.from_orm(f) for f in flights]


def get_flight_by_id(db: Session, flight_id: int):
    flight = db.query(FlightORM).filter(FlightORM.id == flight_id).first()
    return models.Flight.from_orm(flight) if flight else None


def is_flight_available(db: Session, flight_id: int) -> bool:
    flight = db.query(FlightORM).filter(FlightORM.id == flight_id).first()
    if not flight:
        return False
    return flight.seats_available > 0
