import strawberry
from fastapi import HTTPException
from strawberry.types import Info
from app.graphql.schema.type.danfe_type import DanfeType, PaginatedResponseType, SingleResponseType
from app.graphql.schema.input.danfe_input import DanfeFiltroInput
from app.fastapi.schema.danfe_schema import DanfeFiltro
from app.core.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from app.service import danfe_service
from app.core.exceptions import DatabaseError


@strawberry.type
class DanfeQuery:

    @strawberry.field
    async def get_danfes(self, info: Info, page: int = DEFAULT_PAGE) -> PaginatedResponseType:
        try:
            session = info.context["session"]
            result = await danfe_service.get_danfes(page=page, db=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Danfe não encontrado")            
            data = [DanfeType.from_orm(d) for d in result["data"]]
            return PaginatedResponseType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.field
    async def get_danfes_filtradas(self, info: Info, filtro: DanfeFiltroInput, page: int = DEFAULT_PAGE) -> PaginatedResponseType:
        try:
            danfe = DanfeFiltro(
                cd_contribuinte=filtro.cd_contribuinte,
                numero=filtro.numero,
                valor_minimo=filtro.valor_minimo,
                valor_maximo=filtro.valor_maximo,
                data_inicial=filtro.data_inicial,
                data_final=filtro.data_final
            )

            session = info.context["session"]
            result = await danfe_service.get_danfes_filtradas(danfe=danfe, page=page, db=session)

            if not result["data"]:
                raise HTTPException(status_code=404, detail="Danfe não encontrado")
            data = [DanfeType.from_orm(d) for d in result["data"]]
            return PaginatedResponseType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.field
    async def get_danfe(self, info: Info, id_danfe: int) -> SingleResponseType:
        try:
            session = info.context["session"]
            result = await danfe_service.get_danfe(id_danfe=id_danfe, db=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Danfe não encontrado")
            data = DanfeType.from_orm(result['data'])
            return SingleResponseType(data=data)
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))
