import strawberry
from strawberry.types import Info
from fastapi import HTTPException
from app.graphql.schema.type.contribuinte_type import ContribuinteType, SingleResponseType
from app.service import contribuinte_service
from app.fastapi.schema.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate
from app.core.exceptions import DuplicateEntryError, DatabaseError


@strawberry.type
class ContribuinteMutation:

    @strawberry.mutation
    async def create_contribuinte(self, info: Info, cd_contribuinte: str, cnpj_contribuinte: str, nm_fantasia: str) -> SingleResponseType:
        try:
            session = info.context["session"]
            contribuinte = ContribuinteCreate(cd_contribuinte=cd_contribuinte, cnpj_contribuinte=cnpj_contribuinte, nm_fantasia=nm_fantasia)
            result = contribuinte_service.create_contribuinte(contribuinte=contribuinte, db=session)
            data = ContribuinteType.from_orm(result['data'])
            return SingleResponseType(data=data)
        except DuplicateEntryError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.mutation
    async def update_contribuinte(self, info: Info, cd_contribuinte: str, cnpj_contribuinte: str, nm_fantasia: str) -> SingleResponseType:
        try:
            session = info.context["session"]
            contribuinte = ContribuinteUpdate(cnpj_contribuinte=cnpj_contribuinte, nm_fantasia=nm_fantasia)
            result = contribuinte_service.update_contribuinte(cd_contribuinte=cd_contribuinte, contribuinte=contribuinte, db=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
            data = ContribuinteType.from_orm(result['data'])
            return SingleResponseType(data=data)
        except DuplicateEntryError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.mutation
    async def delete_contribuinte(self, info: Info, cd_contribuinte: str) -> SingleResponseType:
        try:
            session = info.context["session"]
            result = await contribuinte_service.delete_contribuinte(cd_contribuinte=cd_contribuinte, db=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
            return {"ok": True, "message": "Contribuinte excluído com sucesso"}
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))
