from sqlalchemy import Column, String, Integer, CHAR, ForeignKey, Text, Numeric, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Endereco(Base):
    __tablename__ = "ENDERECO"
    __table_args__ = {"schema": "NOTA_FISCAL"}

    id_endereco = Column(Integer, primary_key=True, autoincrement=True)
    cd_contribuinte = Column(String(20), ForeignKey("NOTA_FISCAL.CONTRIBUINTE.cd_contribuinte"))
    logradouro = Column(String(200))
    municipio = Column(String(100))
    uf = Column(CHAR(2))

    contribuinte = relationship("Contribuinte", back_populates="enderecos")
