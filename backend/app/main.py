from fastapi import FastAPI
from app.api.flight.routes import router as flight_router

app = FastAPI(title="Airline Operations - Flight Service")

app.include_router(flight_router, prefix="/flights", tags=["flights"])

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}
