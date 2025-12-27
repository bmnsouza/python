import strawberry
from strawberry.types import Info

from app.core.exception.graphql_exception import raise_graphql_error
from app.core.response.graphql_response import set_pagination_params, set_order_params, validate_params
from app.graphql.input.contribuinte_input import ContribuinteParamInput, ContribuinteParamsInput
from app.graphql.input.graphql_input import OrderInput
from app.graphql.type.contribuinte_type import PaginatedResponseContribuinteSqlType, PaginatedResponseContribuinteType, SingleResponseContribuinteType
from app.schema.contribuinte_schema import ContribuinteItem
from app.service.contribuinte_service import ContribuinteService
from app.validator.contribuinte_validator import ContribuinteParam, ContribuinteParams


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
            validate_params(params=params, schema=ContribuinteParams)

            order = set_order_params(order=order, schema=ContribuinteItem)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = ContribuinteService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=params, order=order)

            result = PaginatedResponseContribuinteType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_list_sql(
        self,
        info: Info,
        params: ContribuinteParamsInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseContribuinteSqlType:
        try:
            validate_params(params=params, schema=ContribuinteParams)

            order = set_order_params(order=order, schema=ContribuinteItem)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = ContribuinteService(session=session)
            total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=params, order=order)

            result = PaginatedResponseContribuinteSqlType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_by_cd(
        self,
        info: Info,
        param: ContribuinteParamInput
    ) -> SingleResponseContribuinteType:
        try:
            validate_params(params=param, schema=ContribuinteParam)

            session = info.context["session"]
            service = ContribuinteService(session=session)
            item = await service.get_by_cd(cd=param.cd_contribuinte)

            result = SingleResponseContribuinteType(item=item)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
