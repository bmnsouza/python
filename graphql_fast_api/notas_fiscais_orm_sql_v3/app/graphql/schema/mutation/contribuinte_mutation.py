from typing import Optional
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
import strawberry
from strawberry.types import Info
from fastapi import HTTPException
from app.graphql.schema.type.contribuinte_type import ContribuinteType
from app.model.contribuinte_model import ContribuinteModel
from app.logger import app_logger


@strawberry.type
class ContribuinteMutation:
    @strawberry.mutation
    async def create_contribuinte(self, info: Info, cd_contribuinte: str, cnpj_contribuinte: str, nm_fantasia: Optional[str] = None) -> ContribuinteType:
        session = info.context["session"]
        try:
            novo = ContribuinteModel(
                cd_contribuinte=cd_contribuinte,
                cnpj_contribuinte=cnpj_contribuinte,
                nm_fantasia=nm_fantasia,
            )
            session.add(novo)
            await session.commit()
            await session.refresh(novo)
            return ContribuinteType.from_orm(novo)
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao criar contribuinte %s", cd_contribuinte)
            raise HTTPException(status_code=500, detail="Erro interno ao criar contribuinte") from e

    @strawberry.mutation
    async def update_contribuinte(self, info: Info, cd_contribuinte: str, nm_fantasia: str) -> str:
        session = info.context["session"]
        try:
            result = await session.execute(select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd_contribuinte))
            contrib = result.scalars().first()
            if not contrib:
                return f"Contribuinte {cd_contribuinte} não encontrado."

            contrib.nm_fantasia = nm_fantasia
            await session.commit()
            return f"Contribuinte {cd_contribuinte} atualizado com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao atualizar contribuinte %s", cd_contribuinte)
            raise HTTPException(status_code=500, detail="Erro interno ao atualizar contribuinte") from e

    @strawberry.mutation
    async def delete_contribuinte(self, info: Info, cd_contribuinte: str) -> str:
        """Exclui um contribuinte pelo código."""
        session = info.context["session"]
        try:
            result = await session.execute(select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd_contribuinte))
            contrib = result.scalars().first()
            if not contrib:
                return f"Contribuinte {cd_contribuinte} não encontrado."

            await session.delete(contrib)
            await session.commit()
            return f"Contribuinte {cd_contribuinte} excluído com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao excluir contribuinte %s", cd_contribuinte)
            raise HTTPException(status_code=500, detail="Erro interno ao excluir contribuinte") from e
