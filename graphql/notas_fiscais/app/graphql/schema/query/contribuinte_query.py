import strawberry
from strawberry.types import Info

from app.graphql.schema.input.contribuinte_input import ContribuinteFiltersInput
from app.graphql.schema.input.graphql_input import OrderInput
from app.graphql.schema.type.contribuinte_type import PaginatedResponseContribuinteType, SingleResponseContribuinteType
from app.graphql.utils.exception_util import raise_graphql_error
from app.graphql.utils.response_util import set_pagination_params, set_filters_params, set_order_params
from app.model.contribuinte_model import ContribuinteModel
from app.service.contribuinte_service import ContribuinteService


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        filters: ContribuinteFiltersInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseContribuinteType:
        try:
            filters = set_filters_params(filters=filters)
            order = set_order_params(order=order, model=ContribuinteModel)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = ContribuinteService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseContribuinteType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_list_sql(
        self,
        info: Info,
        filters: ContribuinteFiltersInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseContribuinteType:
        try:
            filters = set_filters_params(filters=filters)
            order = set_order_params(order=order, model=ContribuinteModel)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = ContribuinteService(session=session)
            total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseContribuinteType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_by_cd(
        self,
        info: Info,
        cd_contribuinte: str
    ) -> SingleResponseContribuinteType:
        try:
            session = info.context["session"]
            service = ContribuinteService(session=session)

            result = await service.get_by_cd(cd=cd_contribuinte)
        except Exception as e:
            raise_graphql_error(exc=e)

        if not result:
            raise_graphql_error(description="Contribuinte não encontrado")

        return SingleResponseContribuinteType(item=result)
