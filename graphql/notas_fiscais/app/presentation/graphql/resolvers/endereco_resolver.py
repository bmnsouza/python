import strawberry
from strawberry.types import Info

from app.application.schemas.endereco_schema import Endereco
from app.application.schemas.validators.endereco_validator import EnderecoParams
from app.core.exception import raise_graphql_error
from app.core.response import set_pagination_params, set_order_params, validate_params
from app.domain.services.endereco_service import EnderecoService
from app.presentation.graphql.inputs.endereco_input import EnderecoParamsInput
from app.presentation.graphql.inputs.order_input import OrderInput
from app.presentation.graphql.types.endereco_type import PaginatedResponseEnderecoType


@strawberry.type
class EnderecoQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        params: EnderecoParamsInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseEnderecoType:
        try:
            filters = validate_params(params=params, schema=EnderecoParams)

            order = set_order_params(order=order, schema=Endereco)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = EnderecoService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseEnderecoType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
