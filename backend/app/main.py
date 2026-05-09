# main.py
from fastapi import FastAPI
from app.api.flight.routes import router as flight_router

app = FastAPI(title="Airline Operations API")

app.include_router(flight_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Airline Operations API"}
