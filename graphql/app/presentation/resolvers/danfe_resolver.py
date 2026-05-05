import strawberry
from strawberry.relay import Connection
from strawberry.types import Info

from app.core.exceptions import CustomException
from app.domain.services.danfe_service import DanfeService
from app.presentation.decorators.relay_connection_decorator import relay_connection
from app.presentation.inputs.danfe_input import DanfesInput
from app.presentation.types.danfe_type import DanfeType
from app.presentation.utils.cursor_util import Cursor


@strawberry.type
class DanfeQuery:

    @strawberry.field
    @relay_connection
    async def danfes_json_python(
        self,
        info: Info,
        *,
        filtro: DanfesInput,
        first: int | None = None,
        after: str | None = None,
    ) -> Connection[DanfeType]:
        try:
            service = DanfeService(session=info.context["session"])
            return await service.get_danfes_json_python(
                filtro=filtro.to_pydantic(),
                offset=Cursor.decode(after),
                limit=first,
            )
        except Exception as e:
            raise CustomException(str(e))

    @strawberry.field
    @relay_connection
    async def danfes_json_banco(
        self,
        info: Info,
        *,
        filtro: DanfesInput,
        first: int | None = None,
        after: str | None = None,
    ) -> Connection[DanfeType]:
        try:
            service = DanfeService(session=info.context["session"])
            return await service.get_danfes_json_banco(
                filtro=filtro.to_pydantic(),
                offset=Cursor.decode(after),
                limit=first,
            )
        except Exception as e:
            raise CustomException(str(e))
