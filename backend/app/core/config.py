import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/airline_db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Additional config can be added here
