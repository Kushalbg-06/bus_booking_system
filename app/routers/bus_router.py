from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas
from schemas import buses
from schemas.buses import BusCreate,BusResponse
from typing import List

router=APIRouter(
    prefix="/buses",
    tags=["Buses"]
)

@router.post("/",response_model=BusResponse)
def add_buses(bus:BusCreate,db:Session=Depends(get_db)):
    new_bus=models.Bus(
        bus_number=bus.bus_number,
        origin=bus.origin,
        destination=bus.destination,
        departure_time=bus.departure_time,
        arrival_time=bus.arrival_time,
        total_seats=bus.total_seats,
       is_cancelled=False

    )
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)

    return new_bus