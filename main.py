""" Main file for the FastAPI application. """
from fastapi import FastAPI
from .routers import files

app = FastAPI()


app.include_router(files.router)

@app.get("/HealthCheck")
async def health_check():
    """ Health check endpoint. """
    return {"status": "ok"}
