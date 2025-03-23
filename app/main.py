""" "Main module for the FastAPI application."""

from fastapi import FastAPI
from .src.routers import files
from .src.database import engine, Base

app = FastAPI()
Base.metadata.create_all(engine)

@app.get("/HealthCheck")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


app.include_router(files.router)
