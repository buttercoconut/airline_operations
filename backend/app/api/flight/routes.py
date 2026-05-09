# app/api/flight/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.database import get_db
from app.core.models import Flight
from pydantic import BaseModel

router = APIRouter()

class FlightCreate(BaseModel):
    flight_number: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime

class FlightOut(FlightCreate):
    id: int
    status: str

    class Config:
        orm_mode = True

@router.post("/", response_model=FlightOut)
def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight

@router.get("/", response_model=list[FlightOut])
def list_flights(db: Session = Depends(get_db)):
    return db.query(Flight).all()

@router.get("/{flight_id}", response_model=FlightOut)
def get_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = db.query(Flight).filter(Flight.id == flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight
