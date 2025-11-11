from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.connection import Base

if TYPE_CHECKING:
    from app.models.contribuinte_model import ContribuinteModel

class EnderecoModel(Base):
    __tablename__ = "ENDERECO"
    __table_args__ = {"schema": "NOTA_FISCAL"}

    id_endereco: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cd_contribuinte: Mapped[str] = mapped_column(String(20), ForeignKey("NOTA_FISCAL.CONTRIBUINTE.cd_contribuinte"), nullable=False)
    logradouro: Mapped[str] = mapped_column(String(200))
    municipio: Mapped[str] = mapped_column(String(100))
    uf: Mapped[str] = mapped_column(String(2))

    contribuinte: Mapped["ContribuinteModel"] = relationship(
        back_populates="enderecos",
        lazy="joined"        
    )
