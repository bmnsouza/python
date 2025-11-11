from typing import TYPE_CHECKING, List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.database.connection import Base

if TYPE_CHECKING:
    from app.models.endereco_model import EnderecoModel
    from app.models.danfe_model import DanfeModel


class ContribuinteModel(Base):
    __tablename__ = "CONTRIBUINTE"
    __table_args__ = {"schema": "NOTA_FISCAL"}

    cd_contribuinte: Mapped[str] = mapped_column(String(20), primary_key=True)
    nm_fantasia: Mapped[Optional[str]] = mapped_column(String(200), nullable=False)
    cnpj_contribuinte: Mapped[str] = mapped_column(String(14), unique=True, nullable=False)

    danfes: Mapped[List["DanfeModel"]] = relationship(
        back_populates="contribuinte", 
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    enderecos: Mapped[List["EnderecoModel"]] = relationship(
        back_populates="contribuinte", 
        cascade="all, delete-orphan",
        lazy="selectin"
    )
