from sqlalchemy import Column, String, Integer, CHAR, ForeignKey, Text, Numeric, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Contribuinte(Base):
    __tablename__ = "CONTRIBUINTE"
    __table_args__ = {"schema": "NOTA_FISCAL"}

    cd_contribuinte = Column(String(20), primary_key=True)
    nm_fantasia = Column(String(200))
    cnpj_contribuinte = Column(String(14))

    endereco = relationship("Endereco", back_populates="contribuinte", cascade="all, delete-orphan")
    danfe = relationship("Danfe", back_populates="contribuinte", cascade="all, delete-orphan")
