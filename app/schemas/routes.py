from pydantic import BaseModel
from typing import Optional

class RouteCreate(BaseModel):
    origin:str
    destination:str
    distance:int
    duration:float

class RouteResponse(BaseModel):
    id:int
    origin:str
    destination:str
    distance:int
    duration:float

    model_config = {
        "from_attributes": True
        }