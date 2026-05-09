"""Pydantic models for Flight entity."""

from datetime import datetime
from pydantic import BaseModel, Field

class FlightBase(BaseModel):
    flight_number: str = Field(..., example="AA123")
    origin: str = Field(..., example="JFK")
    destination: str = Field(..., example="LAX")
    departure_time: datetime
    arrival_time: datetime
    aircraft_id: int

class FlightCreate(FlightBase):
    pass

class FlightUpdate(BaseModel):
    departure_time: datetime | None = None
    arrival_time: datetime | None = None

class FlightInDBBase(FlightBase):
    id: int

    class Config:
        orm_mode = True

class Flight(FlightInDBBase):
    pass
