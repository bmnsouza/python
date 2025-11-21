import strawberry
from strawberry.types import Info
from fastapi import HTTPException
from app.graphql.schema.type.endereco_type import EnderecoType, SingleResponseType
from app.service import endereco_service
from app.fastapi.schema.endereco_schema import EnderecoCreate, EnderecoUpdate
from app.core.exceptions import DuplicateEntryError, DatabaseError


@strawberry.type
class EnderecoMutation:

    @strawberry.mutation
    async def create_endereco(self, info: Info, cd_contribuinte: str, logradouro: str, municipio: str, uf: str) -> SingleResponseType:
        try:
            session = info.context["session"]
            endereco = EnderecoCreate(cd_contribuinte=cd_contribuinte, logradouro=logradouro, municipio=municipio, uf=uf)
            result = endereco_service.create_endereco(endereco=endereco, db=session)
            data = EnderecoType.from_orm(result['data'])
            return SingleResponseType(data=data)
        except DuplicateEntryError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.mutation
    async def update_endereco(self, info: Info, id_endereco: int, logradouro: str, municipio: str, uf: str) -> SingleResponseType:
        try:
            session = info.context["session"]
            endereco = EnderecoUpdate(logradouro=logradouro, municipio=municipio, uf=uf)
            result = endereco_service.update_endereco(id_endereco=id_endereco, endereco=endereco, db=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Endereço não encontrado")
            data = EnderecoType.from_orm(result['data'])
            return SingleResponseType(data=data)
        except DuplicateEntryError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.mutation
    async def delete_endereco(self, info: Info, id_endereco: str) -> SingleResponseType:
        try:
            session = info.context["session"]
            result = await endereco_service.delete_endereco(id_endereco=id_endereco, db=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Endereço não encontrado")
            return {"ok": True, "message": "Endereço excluído com sucesso"}
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))
