from pydantic import BaseModel
from datetime import datetime
from  mobility.models import Gender, Infotainment, Engine

class UserBase(BaseModel):
    name: str
    gender: Gender
    age: int
    mail: str

    class Config:
        orm_mode=True


class UserCreate(UserBase):
    pass


class User(BaseModel):
    id: int


class CarBase(BaseModel):
    model: str
    engine: Engine
    infotainment_system: Infotainment
    interior_design: int
    current_location: float

    class Config:
        orm_mode=True


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int


class DemandBase(BaseModel):
    pickup_location: float
    drop_off_location: float
    latest_pickup_time:  datetime
    latest_drop_off_time: datetime

    class Config:
        orm_mode=True


class DemandCreate(DemandBase):
    user_id: int

class Demand(DemandBase):
    id: int
    user_id: int
    car_id: int