from typing import Optional
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
import strawberry
from fastapi import HTTPException
from app.graphql.schemas.types.endereco_type import EnderecoType
from app.models.endereco_model import EnderecoModel
from app.logger import app_logger


@strawberry.type
class EnderecoMutation:
    @strawberry.mutation
    async def criar_endereco(
        self,
        info,
        cd_contribuinte: str,
        logradouro: str,
        municipio: str,
        uf: str,
    ) -> EnderecoType:
        """Cria um novo endereço vinculado a um contribuinte."""
        session = info.context["session"]
        try:
            novo = EnderecoModel(
                cd_contribuinte=cd_contribuinte,
                logradouro=logradouro,
                municipio=municipio,
                uf=uf,
            )
            session.add(novo)
            await session.commit()
            await session.refresh(novo)
            return EnderecoType.from_orm(novo)
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao criar endereço %s", logradouro)
            raise HTTPException(status_code=500, detail="Erro interno ao criar endereço") from e

    @strawberry.mutation
    async def atualizar_endereco(
        self,
        info,
        id_endereco: int,
        logradouro: Optional[str] = None,
        municipio: Optional[str] = None,
        uf: Optional[str] = None,
    ) -> str:
        """Atualiza informações de um endereço."""
        session = info.context["session"]
        try:
            result = await session.execute(
                select(EnderecoModel).where(EnderecoModel.id_endereco == id_endereco)
            )
            endereco = result.scalars().first()
            if not endereco:
                return f"Endereço {id_endereco} não encontrado."

            if logradouro:
                endereco.logradouro = logradouro
            if municipio:
                endereco.municipio = municipio
            if uf:
                endereco.uf = uf

            await session.commit()
            return f"Endereço {id_endereco} atualizado com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao atualizar endereço %s", id_endereco)
            raise HTTPException(status_code=500, detail="Erro interno ao atualizar endereço") from e

    @strawberry.mutation
    async def excluir_endereco(self, info, id_endereco: int) -> str:
        """Exclui um endereço pelo ID."""
        session = info.context["session"]
        try:
            result = await session.execute(
                select(EnderecoModel).where(EnderecoModel.id_endereco == id_endereco)
            )
            endereco = result.scalars().first()
            if not endereco:
                return f"Endereço {id_endereco} não encontrado."

            await session.delete(endereco)
            await session.commit()
            return f"Endereço {id_endereco} excluído com sucesso."
        except SQLAlchemyError as e:
            await session.rollback()
            app_logger.exception("Erro ao excluir endereço %s", id_endereco)
            raise HTTPException(status_code=500, detail="Erro interno ao excluir endereço") from e
