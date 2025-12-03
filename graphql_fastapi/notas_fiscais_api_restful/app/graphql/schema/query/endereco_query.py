import strawberry
from fastapi import HTTPException
from strawberry.types import Info

from app.graphql.schema.type.endereco_type import EnderecoType, PaginatedResponseEnderecoType, SingleResponseEnderecoType
from app.core.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from app.core.exceptions import DatabaseError
from app.service import endereco_service


@strawberry.type
class EnderecoQuery:

    @strawberry.field
    async def get_enderecos(self, info: Info, page: int = DEFAULT_PAGE) -> PaginatedResponseEnderecoType:
        try:
            session = info.context["session"]
            result = await endereco_service.get_enderecos(page=page, session=session)
            data = [EnderecoType.from_orm(e) for e in result["data"]]
            return PaginatedResponseEnderecoType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.field
    async def get_enderecos_por_contribuinte(self, info: Info, cd_contribuinte: str, page: int = DEFAULT_PAGE) -> PaginatedResponseEnderecoType:
        try:
            session = info.context["session"]
            result = await endereco_service.get_enderecos_por_contribuinte(cd_contribuinte=cd_contribuinte, page=page, session=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Endereco não encontrado")
            data = [EnderecoType.from_orm(e) for e in result["data"]]
            return PaginatedResponseEnderecoType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.field
    async def get_endereco(self, info: Info, id_endereco: int) -> SingleResponseEnderecoType:
        try:
            session = info.context["session"]
            result = await endereco_service.get_endereco(id_endereco=id_endereco, session=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Endereco não encontrado")
            data = EnderecoType.from_orm(result['data'])
            return SingleResponseEnderecoType(data=data)
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))
