from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas
from typing import List

router=APIRouter(
   prefix="/booking",
   tags=["Booking"] 
)
@router.post("/", response_model=schemas.BookingResponse)
def book_seat(data: schemas.BookingCreate, db: Session = Depends(get_db), current = Depends(get_current_user)):
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
 
@router.get("/my", response_model=List[schemas.BookingResponse])
def my_bookings(db: Session = Depends(get_db), current = Depends(get_current_user)):
    if current["is_admin"]:
        raise HTTPException(403, "Admins have no user bookings")
    user = current["user"]
    return db.query(models.Booking).filter(models.Booking.user_id == user.id).all()

@router.delete("/cancel/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db), current = Depends(get_current_user)):
    if current["is_admin"]:
        raise HTTPException(403, "Admins cannot cancel user bookings")
    user = current["user"]
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id, models.Booking.user_id == user.id).first()
    if not booking:
        raise HTTPException(404, "Booking not found")
    seat = db.query(models.Seat).filter(models.Seat.id == booking.seat_id).first()
    if seat:
        seat.is_booked = False
    booking.status = "Cancelled"
    db.commit()
    return {"message": "Cancelled"}