from fastapi import FastAPI
from .api.flight.routes import router as flight_router

app = FastAPI(title="Airline Operations API")

app.include_router(flight_router)

# Optional: add startup event to create tables
from .core.database import engine
from .api.flight.models import Base

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
