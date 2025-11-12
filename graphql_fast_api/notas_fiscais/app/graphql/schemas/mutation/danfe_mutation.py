from typing import Optional
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
import strawberry
from fastapi import HTTPException
from app.graphql.schemas.types.danfe_type import DanfeType
from app.models.danfe_model import DanfeModel
from app.logger import app_logger


@strawberry.type
class DanfeMutation:
    @strawberry.mutation
    async def criar_danfe(
        self,
        info,
        cd_contribuinte: str,
        numero: str,
        valor_total: float,
    ) -> DanfeType:
        """Cria uma nova DANFE vinculada a um contribuinte."""
        session = info.context["session"]
        try:
            nova = DanfeModel(
                cd_contribuinte=cd_contribuinte,
                numero=numero,
                valor_total=valor_total,
            )
            session.add(nova)
            await session.commit()
            await session.refresh(nova)
            return DanfeType.from_orm(nova)
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao criar Danfe %s", numero)
            raise HTTPException(status_code=500, detail="Erro interno ao criar Danfe") from e

    @strawberry.mutation
    async def atualizar_danfe(
        self,
        info,
        id_danfe: int,
        numero: Optional[str] = None,
        valor_total: Optional[float] = None,
    ) -> str:
        """Atualiza informações de um Danfe."""
        session = info.context["session"]
        try:
            result = await session.execute(
                select(DanfeModel).where(DanfeModel.id_danfe == id_danfe)
            )
            endereco = result.scalars().first()
            if not endereco:
                return f"Danfe {id_danfe} não encontrado."

            if numero:
                endereco.numero = numero
            if valor_total:
                endereco.valor_total = valor_total

            await session.commit()
            return f"Danfe {id_danfe} atualizado com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao atualizar Danfe %s", id_danfe)
            raise HTTPException(status_code=500, detail="Erro interno ao atualizar Danfe") from e

    @strawberry.mutation
    async def excluir_danfe(self, info, id_danfe: int) -> str:
        """Exclui uma DANFE pelo ID."""
        session = info.context["session"]
        try:
            result = await session.execute(
                select(DanfeModel).where(DanfeModel.id_danfe == id_danfe)
            )
            danfe = result.scalars().first()
            if not danfe:
                return f"Danfe {id_danfe} não encontrado."

            await session.delete(danfe)
            await session.commit()
            return f"Danfe {id_danfe} excluído com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao excluir Danfe %s", id_danfe)
            raise HTTPException(status_code=500, detail="Erro interno ao excluir Danfe") from e
