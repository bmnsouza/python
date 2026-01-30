import strawberry
from strawberry.types import Info

from app.application.schemas.danfe_schema import Danfe
from app.application.schemas.validators.danfe_validator import DanfeLastSevenDaysParam, DanfeParamMonthlyParam, DanfeParams
from app.core.exception import raise_graphql_error
from app.presentation.graphql.mappers.pagination_mapper import map_pagination, set_order_params, validate_params
from app.domain.services.danfe_service import DanfeService
from app.presentation.graphql.inputs.danfe_input import DanfeParamLastSevenDaysInput, DanfeParamMonthlyInput, DanfeParamsInput
from app.presentation.graphql.inputs.order_input import OrderInput
from app.presentation.graphql.types.danfe_type import PaginatedResponseDanfeType


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
            filters = validate_params(params=params, schema=DanfeParams)

            order = set_order_params(order=order, schema=Danfe)
            final_offset, final_limit, final_accept_ranges = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseDanfeType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_last_seven_days(
        self,
        info: Info,
        param: DanfeParamLastSevenDaysInput,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeType:
        try:
            validate_params(params=param, schema=DanfeLastSevenDaysParam)

            final_offset, final_limit, final_accept_ranges = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_last_seven_days(offset=final_offset, limit=final_limit, cd_contribuinte=param.cd_contribuinte)

            result = PaginatedResponseDanfeType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_monthly(
        self,
        info: Info,
        params: DanfeParamMonthlyInput,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeType:
        try:
            filters = validate_params(params=params, schema=DanfeParamMonthlyParam)

            final_offset, final_limit, final_accept_ranges = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_monthly(offset=final_offset, limit=final_limit, filters=filters)

            result = PaginatedResponseDanfeType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
