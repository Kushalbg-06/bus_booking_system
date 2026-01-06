from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import seats
from typing import List

router=APIRouter(
    prefix="/seat",
    tags=["Seats"]
)
@router.get("{id}",response_model=List[seats.SeatResponse])
def get_seats(id:int,db:Session=Depends(get_db)):
    seats=db.query(models.Seats).all()
    if not seats:
        raise HTTPException(404,detail="seats not found")
    return seats
