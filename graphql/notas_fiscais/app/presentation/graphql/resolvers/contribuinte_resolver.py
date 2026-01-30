import strawberry
from strawberry.types import Info

from app.application.schemas.contribuinte_schema import Contribuinte
from app.application.schemas.validators.contribuinte_validator import ContribuinteParams
from app.core.exception import raise_graphql_error
from app.core.response import set_pagination_params, set_order_params, validate_params
from app.domain.services.contribuinte_service import ContribuinteService
from app.presentation.graphql.inputs.contribuinte_input import ContribuinteParamsInput
from app.presentation.graphql.inputs.order_input import OrderInput
from app.presentation.graphql.types.contribuinte_type import PaginatedResponseContribuinteType


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        params: ContribuinteParamsInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseContribuinteType:
        try:
            filters = validate_params(params=params, schema=ContribuinteParams)

            order = set_order_params(order=order, schema=Contribuinte)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = ContribuinteService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseContribuinteType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
