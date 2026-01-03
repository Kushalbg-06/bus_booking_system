from pydantic import BaseModel


class BusCreate(BaseModel):
    bus_number:str
    origin:str
    destination:str
    departure_time:str
    arrival_time:str
    total_seats:int

class BusResponse(BaseModel):
    id:int
    bus_number:str
    origin:str
    destination:str
    departure_time:str
    arrival_time:str
    total_seats:int
    is_cancelled:bool

    model_config ={
        "from_attributes": True
        }
