# routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.database import async_session
from .models import FlightCreate, Flight
from .service import is_flight_available

router = APIRouter(prefix="/flights", tags=["flights"])

@router.post("/", response_model=Flight)
async def create_flight(flight: FlightCreate, db: AsyncSession = Depends(async_session)):
    new_flight = Flight(**flight.dict())
    db.add(new_flight)
    await db.commit()
    await db.refresh(new_flight)
    return new_flight

@router.get("/{flight_id}")
async def get_flight(flight_id: int, db: AsyncSession = Depends(async_session)):
    result = await db.execute(select(Flight).where(Flight.id == flight_id))
    flight = result.scalar_one_or_none()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.get("/{flight_id}/availability")
async def check_availability(flight_id: int, seats: int = 1):
    available = await is_flight_available(flight_id, seats)
    return {"available": available}
