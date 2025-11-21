from datetime import datetime
import strawberry
from strawberry.types import Info
from fastapi import HTTPException
from app.graphql.schema.type.danfe_type import DanfeType, SingleResponseType
from app.service import danfe_service
from app.fastapi.schema.danfe_schema import DanfeCreate, DanfeUpdate
from app.core.exceptions import DuplicateEntryError, DatabaseError


@strawberry.type
class DanfeMutation:

    @strawberry.mutation
    async def create_danfe(self, info: Info, cd_contribuinte: str, numero: str, valor_total: float, data_emissao: datetime) -> SingleResponseType:
        try:
            session = info.context["session"]
            danfe = DanfeCreate(cd_contribuinte=cd_contribuinte, numero=numero, valor_total=valor_total, data_emissao=data_emissao)
            result = danfe_service.create_danfe(danfe=danfe, session=session)
            data = DanfeType.from_orm(result['data'])
            return SingleResponseType(data=data)
        except DuplicateEntryError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.mutation
    async def update_danfe(self, info: Info, id_danfe: int, numero: str, valor_total: float, data_emissao: datetime) -> SingleResponseType:
        try:
            session = info.context["session"]
            danfe = DanfeUpdate(numero=numero, valor_total=valor_total, data_emissao=data_emissao)
            result = danfe_service.update_danfe(id_danfe=id_danfe, danfe=danfe, session=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Danfe não encontrado")
            data = DanfeType.from_orm(result['data'])
            return SingleResponseType(data=data)
        except DuplicateEntryError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))


    @strawberry.mutation
    async def delete_danfe(self, info: Info, id_danfe: str) -> SingleResponseType:
        try:
            session = info.context["session"]
            result = await danfe_service.delete_danfe(id_danfe=id_danfe, session=session)
            if not result["data"]:
                raise HTTPException(status_code=404, detail="Danfe não encontrado")
            return {"ok": True, "message": "Danfe excluído com sucesso"}
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail=str(e))
