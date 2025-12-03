from sqlalchemy import Column,Integer,Float,ForeignKey,DateTime,String,Boolean
from datetime import datetime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)

class Bus(Base):
    __tablename__="buses"
    id=Column(Integer,primary_key=True,index=True)
    bus_number=Column(String)
    origin=Column(String)
    destination=Column(String)
    departure_time=Column(String)
    arrival_time=Column(String)
    total_seats=Column(Integer)
    is_cancelled=Column(Boolean,default=False)

class Seats(Base):
    __tablename__="seats"
    id=Column(Integer,primary_key=True,index=True)
    bus_id=Column(Integer,ForeignKey("buses.id"))
    seat_number=Column(Integer)
    is_booked=Column(Boolean,default=False)

class Booking(Base):
    __tablename__="bookings"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    bus_id=Column(Integer,ForeignKey("buses.id"))
    seat_id=Column(Integer,ForeignKey("seats.id"))
    booking_time=Column(DateTime,default=datetime.utcnow)
    seat_status=Column(String,default="Available")

class Route(Base):
    __tablename__="routes"
    id=Column(Integer,primary_key=True,index=True)
    origin=Column(String)
    destination=Column(String)
    distance=Column(Integer)
    duration=Column(Float)