from pydantic import BaseModel, Field
from datetime import datetime

class FlightBase(BaseModel):
    flight_number: str = Field(..., example="AA123")
    origin: str = Field(..., example="JFK")
    destination: str = Field(..., example="LAX")
    departure_time: datetime
    arrival_time: datetime
    total_seats: int = Field(..., gt=0)

class FlightCreate(FlightBase):
    pass

class FlightOut(FlightBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class FlightCheckAvailability(BaseModel):
    flight_id: int
    seats_requested: int

# SQLAlchemy model for persistence
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, unique=True, index=True, nullable=False)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    total_seats = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
