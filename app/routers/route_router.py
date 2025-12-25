from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import routes
from typing import List

router=APIRouter(
    prefix="/route",
    tags=["Route"]
)
 
@router.post("/",response_model=routes.RouteResponse)
def add_routes(route:routes.RouteCreate,db:Session=Depends(get_db)):
    new_route=models.Route(
        origin=route.origin,
        destination=route.destination,
        distance=route.distance,
        duration=route.duration
    )
    db.add(new_route)
    db.commit()
    db.refresh(new_route)

    return new_route

@router.get("/",response_model=List[routes.RouteResponse])
def get_all_route(db:Session=Depends(get_db)):
    routes=db.query(models.Route).all()
    if not routes:
        raise HTTPException(404,detail="routes not found")
    return routes

@router.delete("/{id}",response_model=routes.RouteResponse)
def  route_delete(id:int,db:Session=Depends(get_db)):
    routes=db.query(models.Route).filter(models.Route.id==id).first()
    if not routes:
        raise HTTPException(detail="the route not found")
    db.delete(routes)
    db.commit()
    db.refresh(routes)
    return "the route is deleted sucessfully"