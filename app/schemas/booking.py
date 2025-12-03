from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookingResponse(BaseModel):
    id:int
    user_id:int
    bus_id:int
    seat_id:int
    booking_time:datetime
    seat_status:str

    model_config ={
        "from_attributes": True
        }
