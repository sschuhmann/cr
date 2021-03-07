from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_mail(db: Session, mail: str):
    return db.query(models.User).filter(models.User.mail == mail).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, gender=user.gender, age=user.age, mail=user.mail)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Car).offset(skip).limit(limit).all()

def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(model=car.model, engine=car.engine, infotainment_system=car.infotainment_system,
                        interior_deign=car.interior_design, curret_location=car.current_location)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)

    print(db_car.license)
    return db_car

def get_active_demand_user(db: Session, user_id: int):
    return db.query(models.Demand).filter(models.Demand.user_id == user_id).filter(models.Demand.active == True).first()

def create_demand(db: Session, demand: schemas.DemandCreate):
    db_demand = models.Demand(pickup_location=demand.pickup_location, drop_off_location=demand.drop_off_location,
                              latest_pickup_time=demand.latest_pickup_time,
                              latest_drop_off_time=demand.latest_drop_off_time,
                              user_id=demand.user_id)
    db.add(db_demand)
    db.commit()
    db.refresh(db_demand)
    return db_demand

def get_available_cars(db: Session):
    return db.query(models.Car).join(models.Demand, isouter=True).all()