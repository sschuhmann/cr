from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    gender: str
    age: int
    mail: str


class UserCreate(UserBase):
    pass


class User(BaseModel):
    id: int


class CarBase(BaseModel):
    model: str
    engine: int
    infotainment_system: int
    interior_design: int
    current_location: float


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int


class DemandBase(BaseModel):
    pickup_location: float
    drop_off_location: float
    latest_pickup_time:  datetime
    latest_drop_off_time: datetime


class DemandCreate(DemandBase):
    user_id: int

class Demand(DemandBase):
    id: int
    user_id: int
    car_id: int