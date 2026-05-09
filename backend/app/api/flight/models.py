# models.py (Pydantic)
from pydantic import BaseModel, Field
from datetime import datetime

class FlightBase(BaseModel):
    flight_number: str = Field(..., example="AA123")
    departure_airport: str = Field(..., example="JFK")
    arrival_airport: str = Field(..., example="LAX")
    departure_time: datetime
    arrival_time: datetime
    capacity: int

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id: int
    class Config:
        orm_mode = True

# Booking models
class BookingBase(BaseModel):
    flight_id: int
    passenger_name: str
    seat_number: str

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    class Config:
        orm_mode = True
