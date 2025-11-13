from typing import List, Optional
import strawberry
from sqlalchemy import select
from app.models.danfe_model import DanfeModel
from app.graphql.schemas.types.danfe_type import DanfeType
from datetime import datetime


@strawberry.input
class FiltroDanfeInput:
    numero: Optional[str] = None
    valor_minimo: Optional[float] = None
    valor_maximo: Optional[float] = None
    data_inicial: Optional[datetime] = None
    data_final: Optional[datetime] = None
    cd_contribuinte: Optional[str] = None


@strawberry.type
class PaginacaoDanfe:
    total_registros: int
    proximo_cursor: Optional[int]
    danfes: List[DanfeType]


@strawberry.type
class DanfeQuery:
    @strawberry.field
    async def get_danfes(self, info, limit: int = 50) -> List[DanfeType]:
        """Lista todas as DANFEs (limitadas)."""
        session = info.context["session"]
        result = await session.execute(
            select(DanfeModel)
            .order_by(DanfeModel.data_emissao.desc())
            .limit(limit)
        )
        danfes = result.scalars().all()
        return [DanfeType.from_orm(d) for d in danfes]

    @strawberry.field
    async def get_danfes_filtradas(
        self,
        info,
        filtro: Optional[FiltroDanfeInput] = None,
        cursor: Optional[int] = None,
        limite: int = 50
    ) -> PaginacaoDanfe:
        """Retorna DANFEs filtradas e paginadas."""
        session = info.context["session"]
        stmt = select(DanfeModel)

        if filtro:
            if filtro.numero:
                stmt = stmt.where(DanfeModel.numero == filtro.numero)
            if filtro.valor_minimo is not None:
                stmt = stmt.where(DanfeModel.valor_total >= filtro.valor_minimo)
            if filtro.valor_maximo is not None:
                stmt = stmt.where(DanfeModel.valor_total <= filtro.valor_maximo)
            if filtro.data_inicial:
                stmt = stmt.where(DanfeModel.data_emissao >= filtro.data_inicial)
            if filtro.data_final:
                stmt = stmt.where(DanfeModel.data_emissao <= filtro.data_final)
            if filtro.cd_contribuinte:
                stmt = stmt.where(DanfeModel.cd_contribuinte == filtro.cd_contribuinte)

        if cursor:
            stmt = stmt.where(DanfeModel.id_danfe > cursor)

        stmt = stmt.order_by(DanfeModel.id_danfe).limit(limite)
        result = await session.execute(stmt)
        danfes = result.scalars().all()

        total_result = await session.execute(select(DanfeModel))
        total_registros = len(total_result.scalars().all())
        proximo_cursor = danfes[-1].id_danfe if danfes else None

        return PaginacaoDanfe(
            total_registros=total_registros,
            proximo_cursor=proximo_cursor,
            danfes=[DanfeType.from_orm(d) for d in danfes],
        )
