from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,hashing
from . import token
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(
    prefix="/user",
    tags=["Users"]
)