from pydantic import BaseModel
from typing import Optional

class SeatResponse(BaseModel):
    id:int
    bus_id:int
    seat_number:int
    is_cancelled:bool
    
    model_config ={
        "from_attributes": True
        }

    