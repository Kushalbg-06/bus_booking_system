from fastapi import FastAPI
from . import models
from .database import engine
from .routers import booking_router,bus_router,route_router,seat_router

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def home():
    return {"server running on the port 8000"}

app.include_router(bus_router.router)
app.include_router(route_router.router)
app.include_router(seat_router.router)
