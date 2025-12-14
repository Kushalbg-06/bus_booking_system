from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import users
from typing import List

router=APIRouter(
   prefix="/users",
   tags=["User"] 
)
@router.post("/",response_model=users.UserResponse)
def add_users(user:users.UserCreate,db:Session=Depends(get_db)):
    new_user=models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/",response_model=List[users.UserResponse])
def get_all_user(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    if not users:
        raise HTTPException(404,detail="users not found")
    return users

@router.get("/{id}",response_model=users.UserResponse)
def get_by_id(int:id,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(404,detail="user not found")
    return user