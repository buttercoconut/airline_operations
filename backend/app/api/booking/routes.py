# app/api/booking/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.database import get_db
from app.core.models import Booking, Flight
from pydantic import BaseModel

router = APIRouter()

class BookingCreate(BaseModel):
    flight_id: int
    passenger_name: str
    seat_number: str

class BookingOut(BookingCreate):
    id: int
    booking_time: datetime

    class Config:
        orm_mode = True

@router.post("/", response_model=BookingOut)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    flight = db.query(Flight).filter(Flight.id == booking.flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    db_booking = Booking(**booking.dict(), booking_time=datetime.utcnow())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/", response_model=list[BookingOut])
def list_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()

@router.get("/{booking_id}", response_model=BookingOut)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking
