from typing import List
import strawberry
from sqlalchemy import select
from app.models.endereco_model import EnderecoModel
from app.graphql.schemas.types.endereco_type import EnderecoType


@strawberry.type
class EnderecoQuery:
    @strawberry.field
    async def get_enderecos(self, info, limit: int = 50) -> List[EnderecoType]:
        """Retorna todos os endereços."""
        session = info.context["session"]
        result = await session.execute(select(EnderecoModel).limit(limit))
        enderecos = result.scalars().all()
        return [EnderecoType.from_orm(e) for e in enderecos]

    @strawberry.field
    async def get_enderecos_por_contribuinte(self, info, cd_contribuinte: str) -> List[EnderecoType]:
        """Busca todos os endereços de um contribuinte específico."""
        session = info.context["session"]
        result = await session.execute(
            select(EnderecoModel).where(EnderecoModel.cd_contribuinte == cd_contribuinte)
        )
        enderecos = result.scalars().all()
        return [EnderecoType.from_orm(e) for e in enderecos]
