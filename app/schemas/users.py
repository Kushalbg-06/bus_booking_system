from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str
    
    model_config ={
        "from_attributes": True
        }
  
class UserLogin(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    sub: Optional[str] = None