from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import buses
from typing import List

router=APIRouter(
    prefix="/buses",
    tags=["Buses"]
)

@router.post("/",response_model=buses.BusResponse)
def add_buses(bus:buses.BusCreate,db:Session=Depends(get_db)):
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
@router.get("/",response_model=List[buses.BusResponse])
def get_all_bus(db:Session=Depends(get_db)):
    buses=db.query(models.Bus).all()
    if not buses:
        raise HTTPException(404,detail="buses not found")
    return buses

@router.get("/{id}",response_model=buses.BusResponse)
def get_bus_id(id:int,db:Session=Depends(get_db)):
    bus_id=db.query(models.Bus).filter(models.Bus.id==id).first()
    if not bus_id:
        raise HTTPException(404,detail="bus not found")
    return bus_id

@router.put("/{bus_id}", response_model=buses.BusResponse)
def update_bus(bus_id: int, updated_bus:buses.BusCreate, db: Session = Depends(get_db)):
    bus = db.query(models.Bus).filter(models.Bus.id == bus_id).first()

    if not bus:
        raise HTTPException(404, "Bus not found")

    bus.bus_number = updated_bus.bus_number
    bus.origin = updated_bus.origin
    bus.destination = updated_bus.destination
    bus.departure_time = updated_bus.departure_time
    bus.arrival_time = updated_bus.arrival_time
    bus.total_seats = updated_bus.total_seats

    db.commit()
    db.refresh(bus)
    return bus

@router.delete("/{id}")
def delete_bus(id:int,db:Session=Depends(get_db)):
    bus_id=db.query(models.Bus).filter(models.Bus.id==id).first()
    if not bus_id:
        raise HTTPException(404,detail="bus not found")
    db.delete(bus_id)
    db.commit()

    return {"details":"bus is delete succesfully"}
