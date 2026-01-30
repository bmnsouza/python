from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infraestructure.database.connection import Base


if TYPE_CHECKING:
    from app.infraestructure.database.models.contribuinte_model import ContribuinteModel

class DanfeModel(Base):
    __tablename__ = "DANFE"
    __table_args__ = {"schema": "NOTA_FISCAL"}

    id_danfe: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cd_contribuinte: Mapped[str] = mapped_column(String(20), ForeignKey("NOTA_FISCAL.CONTRIBUINTE.cd_contribuinte"), nullable=False)
    numero: Mapped[str] = mapped_column(String(15), nullable=False)
    valor_total: Mapped[Decimal] = mapped_column(Numeric(12,2), nullable=False)
    data_emissao: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)

    contribuinte: Mapped["ContribuinteModel"] = relationship(
        back_populates="danfes",
        lazy="joined"
    )
