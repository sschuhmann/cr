from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_mail(db, user.mail)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail = "User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user



@app.post("/cars/", response_model=schemas.Car)
def create_user(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = crud.get_
    if db_car:
        raise HTTPException(status_code=400, detail="License already registered")
    return crud.create_car(db=db, car=car)


@app.get("/demand", response_model=schemas.Demand)
def place_demand(demand: schemas.DemandCreate, db: Session = Depends(get_db)):
    db_demand = crud.get_active_demand_user(db, demand.user_id)
    if db_demand:
        raise HTTPException(status_code=400, detail="The user already has an open demand")

    db_demand = crud.create_demand(db, demand)

    #ToDo Trigger schedular

    return db_demand

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)