""" "Main module for the FastAPI application."""

from fastapi import FastAPI,Depends
from typing import Annotated
from .src.routers import files
from .src.database import engine, Base
from .src.config import Settings,get_settings


app = FastAPI()
Base.metadata.create_all(engine)

@app.get("/HealthCheck")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email
    }

app.include_router(files.router)
