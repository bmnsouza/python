import strawberry
from strawberry.relay import Connection
from strawberry.types import Info

from app.core.exceptions import CustomException
from app.domain.services.endereco_service import EnderecoService
from app.presentation.decorators.relay_connection_decorator import relay_connection
from app.presentation.inputs.endereco_input import EnderecoInput, EnderecosInput
from app.presentation.types.endereco_type import EnderecoType
from app.presentation.utils.cursor_util import Cursor


@strawberry.type
class EnderecoQuery:

    @strawberry.field
    async def endereco(self, info: Info, *, filtro: EnderecoInput) -> EnderecoType | None:
        try:
            service = EnderecoService(session=info.context["session"])
            result = await service.get_endereco(filtro=filtro.to_pydantic())
            return result
        except Exception as e:
            raise CustomException(str(e))

    @strawberry.field
    @relay_connection
    async def enderecos(
        self,
        info: Info,
        *,
        filtro: EnderecosInput,
        first: int | None = None,
        after: str | None = None,
    ) -> Connection[EnderecoType]:
        try:
            service = EnderecoService(session=info.context["session"])
            return await service.get_enderecos(
                filtro=filtro.to_pydantic(),
                offset=Cursor.decode(after),
                limit=first,
            )
        except Exception as e:
            raise CustomException(str(e))
