import strawberry
from strawberry.types import Info

from app.core.exception.exception_graphql import raise_graphql_error
from app.core.response.response_graphql import set_pagination_params, set_filters_params, set_order_params, validate_params
from app.fastapi.schema.danfe_schema import DanfeListItem
from app.graphql.schema.input.danfe_input import DanfeParamsInput, DanfeParamInput
from app.graphql.schema.input.graphql_input import OrderInput
from app.graphql.schema.type.danfe_type import PaginatedResponseDanfeType, SingleResponseDanfeType
from app.model.danfe_model import DanfeModel
from app.service.danfe_service import DanfeService
from app.validator.danfe_validator import DanfeParam, DanfeParams


@strawberry.type
class DanfeQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        params: DanfeParamsInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeType:
        try:
            validate_params(params=params, schema=DanfeParams)

            params = set_filters_params(params=params)
            order = set_order_params(order=order, model=DanfeModel)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=params, order=order)

            result = PaginatedResponseDanfeType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_list_sql(
        self,
        info: Info,
        params: DanfeParamsInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeType:
        try:
            validate_params(params=params, schema=DanfeParams)

            params = set_filters_params(params=params)
            order = set_order_params(order=order, schema=DanfeListItem)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=params, order=order)

            result = PaginatedResponseDanfeType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_by_id(
        self,
        info: Info,
        param: DanfeParamInput
    ) -> SingleResponseDanfeType:
        try:
            validate_params(params=param, schema=DanfeParam)

            session = info.context["session"]
            service = DanfeService(session=session)
            item = await service.get_by_id(id=param.id_danfe)

            result = SingleResponseDanfeType(item=item)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
