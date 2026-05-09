from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FlightBase(BaseModel):
    flight_number: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    aircraft_id: int

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id: int
    seats_total: int
    seats_available: int

    class Config:
        orm_mode = True
