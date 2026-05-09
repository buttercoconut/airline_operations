from sqlalchemy.ext.asyncio import AsyncSession
from .models import Flight

async def check_flight_availability(db: AsyncSession, flight_id: int, seats_requested: int) -> bool:
    """Check if requested seats are available for a flight.
    For simplicity, we assume all seats are available until a booking
    service records reservations. This function can be extended to
    query a Booking table and calculate remaining seats.
    """
    flight = await db.get(Flight, flight_id)
    if not flight:
        return False
    # Placeholder logic: if seats_requested <= total_seats, return True
    # In real scenario, subtract already booked seats.
    return seats_requested <= flight.total_seats
