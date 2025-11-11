import strawberry
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, func
from app.models.danfe_model import DanfeModel
from app.schema.types.danfe_type import DanfeType


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
                data_emissao=func.sysdate(),
            )
            session.add(nova)
            await session.commit()
            await session.refresh(nova)
            return DanfeType.from_orm(nova)
        except SQLAlchemyError as e:
            await session.rollback()
            raise Exception(f"Erro ao criar DANFE: {e}")

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
            raise Exception(f"Erro ao atualizar Danfe: {e}")

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
                return f"Danfe {id_danfe} não encontrada."

            await session.delete(danfe)
            await session.commit()
            return f"Danfe {id_danfe} excluída com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            raise Exception(f"Erro ao excluir DANFE: {e}")
