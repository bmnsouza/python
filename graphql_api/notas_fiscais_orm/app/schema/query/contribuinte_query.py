import strawberry
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models.contribuinte_model import ContribuinteModel
from app.schema.types.contribuinte_type import ContribuinteType


@strawberry.type
class ContribuinteQuery:
    @strawberry.field
    async def get_contribuintes(self, info, limit: int = 10) -> List[ContribuinteType]:
        """Retorna uma lista de contribuintes com endereços e danfes."""
        session = info.context["session"]
        result = await session.execute(
            select(ContribuinteModel)
            .options(
                selectinload(ContribuinteModel.enderecos),
                selectinload(ContribuinteModel.danfes)
            )
            .limit(limit)
        )
        contribuintes = result.scalars().unique().all()
        return [ContribuinteType.from_orm(c) for c in contribuintes]

    @strawberry.field
    async def get_contribuinte_por_cnpj(self, info, cnpj: str) -> Optional[ContribuinteType]:
        """Busca um contribuinte pelo CNPJ."""
        session = info.context["session"]
        result = await session.execute(
            select(ContribuinteModel)
            .options(
                selectinload(ContribuinteModel.enderecos),
                selectinload(ContribuinteModel.danfes)
            )
            .where(ContribuinteModel.cnpj_contribuinte == cnpj)
        )
        contrib = result.scalars().first()
        return ContribuinteType.from_orm(contrib) if contrib else None
