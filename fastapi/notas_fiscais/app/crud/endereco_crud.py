from sqlalchemy.orm import Session
from app.models.endereco_model import Endereco
from app.schemas.endereco_schema import EnderecoCreate, EnderecoUpdate

def get_endereco(db: Session, id_endereco: int):
    return db.query(Endereco).filter(Endereco.id_endereco == id_endereco).first()

def get_enderecos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Endereco).offset(skip).limit(limit).all()

def create_endereco(db: Session, endereco: EnderecoCreate):
    db_endereco = Endereco(**endereco.model_dump())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

def update_endereco(db: Session, id_endereco: int, updates: EnderecoUpdate):
    db_endereco = get_endereco(db, id_endereco)
    if not db_endereco:
        return None
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_endereco, key, value)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

def delete_endereco(db: Session, id_endereco: int):
    db_endereco = get_endereco(db, id_endereco)
    if db_endereco:
        db.delete(db_endereco)
        db.commit()
    return db_endereco
