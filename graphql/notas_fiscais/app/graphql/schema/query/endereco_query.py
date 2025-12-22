import strawberry
from strawberry.types import Info

from app.graphql.schema.input.endereco_input import EnderecoFiltersInput
from app.graphql.schema.input.graphql_input import OrderInput
from app.graphql.schema.type.endereco_type import PaginatedResponseEnderecoType, SingleResponseEnderecoType
from app.graphql.utils.exception_util import raise_graphql_error
from app.graphql.utils.response_util import normalize_pagination_params, set_filters_params, set_order_params
from app.model.endereco_model import EnderecoModel
from app.service.endereco_service import EnderecoService


@strawberry.type
class EnderecoQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        filters: EnderecoFiltersInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseEnderecoType:
        try:
            filters = set_filters_params(filters=filters)
            order = set_order_params(order=order, model=EnderecoModel)
            final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = EnderecoService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseEnderecoType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_list_sql(
        self,
        info: Info,
        filters: EnderecoFiltersInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseEnderecoType:
        try:
            filters = set_filters_params(filters=filters)
            order = set_order_params(order=order, model=EnderecoModel)
            final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = EnderecoService(session=session)
            total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=filters, order=order)

            result = PaginatedResponseEnderecoType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_by_id(
        self,
        info: Info,
        id_endereco: str
    ) -> SingleResponseEnderecoType:
        try:
            session = info.context["session"]
            service = EnderecoService(session=session)

            result = await service.get_by_id(id=id_endereco)
        except Exception as e:
            raise_graphql_error(exc=e)

        if not result:
            raise_graphql_error(description="Endereco não encontrado")

        return SingleResponseEnderecoType(item=result)
