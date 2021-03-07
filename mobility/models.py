from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Enum, DateTime
from sqlalchemy.orm import relationship
import enum
import datetime

from .database import Base

class Gender(str, enum.Enum):
    FEMALE = 'f'
    MALE = 'm'
    DIVERS = 'd'

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(Enum(Gender))
    age = Column(Integer)
    mail = Column(String, unique=True)

class Engine(int, enum.Enum):
    TYPE_A = 0
    TYPE_B = 1
    TYPE_C = 2

class Infotainment(int, enum.Enum):
    NONE = 0
    RADIO = 1
    TV = 2

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    model = Column(String)
    engine = Column(Enum(Engine))
    infotainment_system = Column(Enum(Infotainment))
    interior_design = Column(Integer)
    current_location = Column(Float)


class Demand(Base):
    __tablename__ = "demands"

    id = Column(Integer, primary_key=True)
    pickup_location = Column(Float)
    drop_off_location = Column(Float)
    latest_pickup_time = Column(DateTime)
    latest_drop_offA_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))


