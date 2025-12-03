import strawberry
# from fastapi import HTTPException
# from strawberry.types import Info

# from app.core.exceptions import DatabaseError
# from app.core.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
# from app.graphql.schema.type.contribuinte_type import ContribuinteType, ContribuinteDenfeEnderecoType, PaginatedResponseType, SingleResponseType
# from app.service import contribuinte_service


@strawberry.type
class ContribuinteQuery:
    pass

    # @strawberry.field
    # async def get_contribuintes(self, info: Info, page: int = DEFAULT_PAGE) -> PaginatedResponseType:
    #     try:
    #         session = info.context["session"]
    #         result = await contribuinte_service.get_contribuintes(page=page, session=session)
    #         data = [ContribuinteType.from_orm(c) for c in result["data"]]
    #         return PaginatedResponseType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)
    #     except DatabaseError as e:
    #         raise HTTPException(status_code=500, detail=str(e))


    # @strawberry.field
    # async def get_contribuintes_danfe_endereco(self, info: Info, filtro_nome: str, page: int = DEFAULT_PAGE) -> PaginatedResponseType:
    #     try:
    #         session = info.context["session"]
    #         result = await contribuinte_service.get_contribuintes_danfe_endereco(filtro_nome=filtro_nome, page=page, session=session)
    #         data = [ContribuinteDenfeEnderecoType(**row) for row in result["data"]]
    #         return PaginatedResponseType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)
    #     except DatabaseError as e:
    #         raise HTTPException(status_code=500, detail=str(e))


    # @strawberry.field
    # async def get_contribuinte_por_cd(self, info: Info, cd_contribuinte: str) -> SingleResponseType:
    #     try:
    #         session = info.context["session"]
    #         result = await contribuinte_service.get_contribuinte_por_cd(cd_contribuinte=cd_contribuinte, session=session)
    #         if not result["data"]:
    #             raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    #         data = ContribuinteType.from_orm(result['data'])
    #         return SingleResponseType(data=data)
    #     except DatabaseError as e:
    #         raise HTTPException(status_code=500, detail=str(e))


    # @strawberry.field
    # async def get_contribuinte_por_cnpj(self, info: Info, cnpj_contribuinte: str) -> SingleResponseType:
    #     try:
    #         session = info.context["session"]
    #         result = await contribuinte_service.get_contribuinte_por_cnpj(cnpj_contribuinte=cnpj_contribuinte, session=session)
    #         if not result["data"]:
    #             raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    #         data = ContribuinteType.from_orm(result['data'])
    #         return SingleResponseType(data=data)
    #     except DatabaseError as e:
    #         raise HTTPException(status_code=500, detail=str(e))
