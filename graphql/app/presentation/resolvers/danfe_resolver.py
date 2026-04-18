import strawberry
from strawberry.relay import Connection
from strawberry.types import Info

from app.core.exceptions import CustomException
from app.domain.services.danfe_service import DanfeService

from ..decorators.relay_connection_decorator import relay_connection
from ..inputs.danfe_input import DanfeInput, DanfesInput
from ..types.danfe_type import DanfeType
from ..utils.cursor_util import Cursor


@strawberry.type
class DanfeQuery:

    @strawberry.field
    async def danfe(self, info: Info, *, filtro: DanfeInput) -> DanfeType | None:
        try:
            service = DanfeService(session=info.context["session"])
            result = await service.get_danfe(filtro=filtro.to_pydantic())
            return result
        except Exception as e:
            raise CustomException(str(e))

    @strawberry.field
    @relay_connection
    async def danfes(
        self,
        info: Info,
        *,
        filtro: DanfesInput,
        first: int | None = None,
        after: str | None = None,
    ) -> Connection[DanfeType]:
        try:
            service = DanfeService(session=info.context["session"])
            return await service.get_danfes(
                filtro=filtro.to_pydantic(),
                offset=Cursor.decode(after),
                limit=first,
            )
        except Exception as e:
            raise CustomException(str(e))
