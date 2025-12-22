import strawberry
from strawberry.types import Info

from app.graphql.schema.input.danfe_input import DanfeFiltersInput
from app.graphql.schema.input.graphql_input import OrderInput
from app.graphql.schema.type.danfe_type import PaginatedResponseDanfeType, SingleResponseDanfeType
from app.graphql.utils.exception_util import raise_graphql_error
from app.graphql.utils.response_util import normalize_pagination_params, set_filters_params, set_order_params
from app.model.danfe_model import DanfeModel
from app.service.danfe_service import DanfeService


@strawberry.type
class DanfeQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        filters: DanfeFiltersInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeType:
        try:
            filters = set_filters_params(filters=filters)
            order = set_order_params(order=order, model=DanfeModel)
            final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseDanfeType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_list_sql(
        self,
        info: Info,
        filters: DanfeFiltersInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeType:
        try:
            filters = set_filters_params(filters=filters)
            order = set_order_params(order=order, model=DanfeModel)
            final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseDanfeType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_by_id(
        self,
        info: Info,
        id_danfe: str
    ) -> SingleResponseDanfeType:
        try:
            session = info.context["session"]
            service = DanfeService(session=session)

            result = await service.get_by_id(id=id_danfe)
        except Exception as e:
            raise_graphql_error(exc=e)

        if not result:
            raise_graphql_error(description="Danfe não encontrado")

        return SingleResponseDanfeType(item=result)
