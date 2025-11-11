from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.connection import Base

if TYPE_CHECKING:
    from app.models.contribuinte_model import ContribuinteModel

class DanfeModel(Base):
    __tablename__ = "DANFE"
    __table_args__ = {"schema": "NOTA_FISCAL"}

    id_danfe: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cd_contribuinte: Mapped[str] = mapped_column(String(20), ForeignKey("NOTA_FISCAL.CONTRIBUINTE.cd_contribuinte"), nullable=False)
    numero: Mapped[str] = mapped_column(String(15))
    valor_total: Mapped[float] = mapped_column(Float)
    data_emissao: Mapped[datetime] = mapped_column(DateTime, server_default=func.sysdate())

    contribuinte: Mapped["ContribuinteModel"] = relationship(
        back_populates="danfes",
        lazy="joined"
    )
