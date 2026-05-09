from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..core.database import get_db
from .models import Flight, FlightCreate, FlightOut, FlightCheckAvailability
from .service import check_flight_availability

router = APIRouter(prefix="/flights", tags=["flights"])

@router.post("/", response_model=FlightOut, status_code=status.HTTP_201_CREATED)
async def create_flight(flight: FlightCreate, db: AsyncSession = Depends(get_db)):
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    await db.commit()
    await db.refresh(db_flight)
    return db_flight

@router.get("/{flight_id}", response_model=FlightOut)
async def get_flight(flight_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Flight).where(Flight.id == flight_id))
    flight = result.scalar_one_or_none()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.post("/availability", response_model=dict)
async def check_availability(payload: FlightCheckAvailability, db: AsyncSession = Depends(get_db)):
    available = await check_flight_availability(db, payload.flight_id, payload.seats_requested)
    return {"available": available}
