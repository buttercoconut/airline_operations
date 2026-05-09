from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.flight import models, service

router = APIRouter()

@router.post("/", response_model=models.Flight, status_code=status.HTTP_201_CREATED)
async def create_flight(flight: models.FlightCreate, db: Session = Depends(get_db)):
    return service.create_flight(db, flight)

@router.get("/", response_model=list[models.Flight])
async def list_flights(db: Session = Depends(get_db)):
    return service.get_all_flights(db)

@router.get("/{flight_id}", response_model=models.Flight)
async def get_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = service.get_flight_by_id(db, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.get("/availability/{flight_id}")
async def check_availability(flight_id: int, db: Session = Depends(get_db)):
    return service.is_flight_available(db, flight_id)
