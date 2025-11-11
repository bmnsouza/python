import strawberry
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from app.models.contribuinte_model import ContribuinteModel
from app.schema.types.contribuinte_type import ContribuinteType


@strawberry.type
class ContribuinteMutation:
    @strawberry.mutation
    async def criar_contribuinte(
        self,
        info,
        cd_contribuinte: str,
        cnpj_contribuinte: str,
        nm_fantasia: Optional[str] = None,
    ) -> ContribuinteType:
        """Cria um novo contribuinte."""
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
            raise Exception(f"Erro ao criar contribuinte: {e}")

    @strawberry.mutation
    async def atualizar_contribuinte(
        self,
        info,
        cd_contribuinte: str,
        nm_fantasia: str,
    ) -> str:
        """Atualiza o nome fantasia de um contribuinte."""
        session = info.context["session"]
        try:
            result = await session.execute(
                select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd_contribuinte)
            )
            contrib = result.scalars().first()
            if not contrib:
                return f"Contribuinte {cd_contribuinte} não encontrado."

            contrib.nm_fantasia = nm_fantasia
            await session.commit()
            return f"Contribuinte {cd_contribuinte} atualizado com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            raise Exception(f"Erro ao atualizar contribuinte: {e}")

    @strawberry.mutation
    async def excluir_contribuinte(self, info, cd_contribuinte: str) -> str:
        """Exclui um contribuinte pelo código."""
        session = info.context["session"]
        try:
            result = await session.execute(
                select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd_contribuinte)
            )
            contrib = result.scalars().first()
            if not contrib:
                return f"Contribuinte {cd_contribuinte} não encontrado."

            await session.delete(contrib)
            await session.commit()
            return f"Contribuinte {cd_contribuinte} excluído com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            raise Exception(f"Erro ao excluir contribuinte: {e}")
