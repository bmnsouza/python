from sqlalchemy.orm import Session
from app.models.contribuinte_model import Contribuinte
from app.schemas.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate

def get_contribuinte(db: Session, cd_contribuinte: str):
    return db.query(Contribuinte).filter(Contribuinte.cd_contribuinte == cd_contribuinte).first()

def get_contribuintes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Contribuinte).offset(skip).limit(limit).all()

def create_contribuinte(db: Session, contribuinte: ContribuinteCreate):
    db_contribuinte = contribuinte.Contribuinte(**contribuinte.dict())
    db.add(db_contribuinte)
    db.commit()
    db.refresh(db_contribuinte)
    return db_contribuinte

def update_contribuinte(db: Session, cd_contribuinte: str, updates: ContribuinteUpdate):
    db_contribuinte = get_contribuinte(db, cd_contribuinte)
    if not db_contribuinte:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_contribuinte, key, value)
    db.commit()
    db.refresh(db_contribuinte)
    return db_contribuinte

def delete_contribuinte(db: Session, cd_contribuinte: str):
    db_contribuinte = get_contribuinte(db, cd_contribuinte)
    if db_contribuinte:
        db.delete(db_contribuinte)
        db.commit()
    return db_contribuinte
