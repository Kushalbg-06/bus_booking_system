from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas
from typing import List

router=APIRouter(
   prefix="/booking",
   tags=["Booking"] 
)
@router.post("/", response_model=BookingResponse)
def book_seat(data: BookingCreate, db: Session = Depends(get_db), current = Depends(get_current_user)):
    if current["is_admin"]:
        raise HTTPException(403, "Admins cannot book")
    user = current["user"]
    seat = db.query(models.Seat).filter(models.Seat.id == data.seat_id, models.Seat.bus_id == data.bus_id).first()
    if not seat:
        raise HTTPException(404, "Seat not found")
    if seat.is_booked:
        raise HTTPException(400, "Seat already booked")
    booking = models.Booking(user_id=user.id, bus_id=data.bus_id, seat_id=data.seat_id)
    seat.is_booked = True
    db.add(booking); db.commit(); db.refresh(booking)
    return booking
