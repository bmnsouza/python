from sqlalchemy.orm import Session
from app.models.danfe_model import Danfe
from app.schemas.danfe_schema import DanfeCreate, DanfeUpdate

def get_danfe(db: Session, id_danfe: int):
    return db.query(Danfe).filter(Danfe.id_danfe == id_danfe).first()

def get_danfes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Danfe).offset(skip).limit(limit).all()

def create_danfe(db: Session, danfe: DanfeCreate):
    db_danfe = Danfe(**danfe.model_dump())
    db.add(db_danfe)
    db.commit()
    db.refresh(db_danfe)
    return db_danfe

def update_danfe(db: Session, id_danfe: int, updates: DanfeUpdate):
    db_danfe = get_danfe(db, id_danfe)
    if not db_danfe:
        return None
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_danfe, key, value)
    db.commit()
    db.refresh(db_danfe)
    return db_danfe

def delete_danfe(db: Session, id_danfe: int):
    db_danfe = get_danfe(db, id_danfe)
    if db_danfe:
        db.delete(db_danfe)
        db.commit()
    return db_danfe
