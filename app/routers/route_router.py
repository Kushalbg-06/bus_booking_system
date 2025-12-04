from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas
from typing import List

router=APIRouter(
    prefix="/route",
    tags=["Route"]
)