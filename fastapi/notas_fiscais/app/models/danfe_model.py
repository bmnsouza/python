from sqlalchemy import Column, String, Integer, CHAR, ForeignKey, Text, Numeric, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Danfe(Base):
    __tablename__ = "DANFE"
    __table_args__ = {"schema": "NOTA_FISCAL"}

    id_danfe = Column(Integer, primary_key=True, autoincrement=True)
    cd_contribuinte = Column(String(20), ForeignKey("NOTA_FISCAL.CONTRIBUINTE.cd_contribuinte"))
    numero = Column(String(15))
    valor_total = Column(Numeric(12,2))
    data_emissao = Column(DateTime)

    contribuinte = relationship("Contribuinte", back_populates="danfes")
