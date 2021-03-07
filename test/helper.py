from mobility.database import SessionLocal, engine
import mobility.models as models

def clear_database_records():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    db.query(models.User).delete()
    db.query(models.Car).delete()
    db.query(models.Demand).delete()
    db.commit()