# app/main.py
from fastapi import FastAPI
from app.api.flight.routes import router as flight_router
from app.api.booking.routes import router as booking_router

app = FastAPI(title="Airline Operations API")

app.include_router(flight_router, prefix="/flights", tags=["flights"])
app.include_router(booking_router, prefix="/bookings", tags=["bookings"])

@app.get("/")
async def root():
    return {"message": "Welcome to Airline Operations API"}
