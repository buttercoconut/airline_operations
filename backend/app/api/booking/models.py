"""Pydantic models for Booking entity."""

from datetime import datetime
from pydantic import BaseModel, Field

class BookingBase(BaseModel):
    passenger_id: int
    flight_id: int
    seat_number: str = Field(..., example="12A")
    booking_time: datetime = Field(default_factory=datetime.utcnow)

class BookingCreate(BookingBase):
    pass

class BookingInDBBase(BookingBase):
    id: int

    class Config:
        orm_mode = True

class Booking(BookingInDBBase):
    pass
