import strawberry
from strawberry.relay import Connection
from strawberry.types import Info

from app.core.exceptions import CustomException
from app.domain.services.contribuinte_service import ContribuinteService
from app.presentation.decorators.relay_connection_decorator import relay_connection
from app.presentation.inputs.contribuinte_input import ContribuinteInput, ContribuintesInput
from app.presentation.types.contribuinte_type import ContribuinteType
from app.presentation.utils.cursor_util import Cursor


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def contribuinte(self, info: Info, *, filtro: ContribuinteInput) -> ContribuinteType | None:
        try:
            service = ContribuinteService(session=info.context["session"])
            result = await service.get_contribuinte(filtro=filtro.to_pydantic())
            return result
        except Exception as e:
            raise CustomException(str(e))

    @strawberry.field
    @relay_connection
    async def contribuintes(
        self,
        info: Info,
        *,
        filtro: ContribuintesInput,
        first: int | None = None,
        after: str | None = None,
    ) -> Connection[ContribuinteType]:
        try:
            service = ContribuinteService(session=info.context["session"])
            return await service.get_contribuintes(
                filtro=filtro.to_pydantic(),
                offset=Cursor.decode(after),
                limit=first,
            )
        except Exception as e:
            raise CustomException(str(e))
