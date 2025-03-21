""" Main file for the FastAPI application. """
from fastapi import FastAPI
from .routers import files

app = FastAPI()

@app.get("/HealthCheck")
def health_check():
    """ Health check endpoint. """
    return {"status": "ok"}

app.include_router(files.router)
