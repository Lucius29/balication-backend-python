from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI(
    title="Balication API",
    description="Backend Sistem Rekomendasi Wisata Bali",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Balication API",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/db-health")
def database_health():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT 1")
            )

            result.scalar()

        return {
            "database": "connected",
            "status": "success"
        }

    except Exception:
        return {
            "database": "disconnected",
            "status": "error"
        }