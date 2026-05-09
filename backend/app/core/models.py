# app/core/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, unique=True, index=True, nullable=False)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    status = Column(String, default="scheduled")
    bookings = relationship("Booking", back_populates="flight")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer, ForeignKey("flights.id"), nullable=False)
    passenger_name = Column(String, nullable=False)
    seat_number = Column(String, nullable=False)
    booking_time = Column(DateTime, nullable=False)
    flight = relationship("Flight", back_populates="bookings")
