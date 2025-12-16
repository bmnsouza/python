from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.connection import Base


if TYPE_CHECKING:
    from app.model.danfe_model import DanfeModel
    from app.model.endereco_model import EnderecoModel

class ContribuinteModel(Base):
    __tablename__ = "CONTRIBUINTE"
    __table_args__ = {"schema": "NOTA_FISCAL"}

    cd_contribuinte: Mapped[str] = mapped_column(String(20), primary_key=True)
    cnpj_contribuinte: Mapped[str] = mapped_column(String(14), unique=True, nullable=False)
    nm_fantasia: Mapped[Optional[str]] = mapped_column(String(200), nullable=False)

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
