# service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from ..core.database import async_session
from .models import FlightCreate, Flight
from datetime import datetime

# Core logic: check availability
async def is_flight_available(flight_id: int, requested_seats: int = 1) -> bool:
    async with async_session() as session:
        # Count existing bookings for the flight
        result = await session.execute(
            select(func.count()).select_from(Booking).where(Booking.flight_id == flight_id)
        )
        booked = result.scalar_one_or_none() or 0
        # Retrieve flight capacity
        flight_res = await session.execute(select(Flight).where(Flight.id == flight_id))
        flight = flight_res.scalar_one_or_none()
        if not flight:
            return False
        return (flight.capacity - booked) >= requested_seats

# Placeholder Booking model for query
class Booking:
    flight_id: int
