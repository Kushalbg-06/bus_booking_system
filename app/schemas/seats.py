from pydantic import BaseModel


class SeatResponse(BaseModel):
    id:int
    bus_id:int
    seat_number:int
    is_cancelled:bool
    
    model_config ={
        "from_attributes": True
        }

    