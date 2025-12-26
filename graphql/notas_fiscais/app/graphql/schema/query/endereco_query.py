import strawberry
from strawberry.types import Info

from app.core.exception.exception_graphql import raise_graphql_error
from app.core.response.response_graphql import set_pagination_params, set_filters_params, set_order_params, validate_params
from app.fastapi.schema.endereco_schema import EnderecoListItem
from app.graphql.schema.input.endereco_input import EnderecoParamsInput, EnderecoParamInput
from app.graphql.schema.input.graphql_input import OrderInput
from app.graphql.schema.type.endereco_type import PaginatedResponseEnderecoType, SingleResponseEnderecoType
from app.model.endereco_model import EnderecoModel
from app.service.endereco_service import EnderecoService
from app.validator.endereco_validator import EnderecoParam, EnderecoParams


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
            validate_params(params=params, schema=EnderecoParams)

            params = set_filters_params(params=params)
            order = set_order_params(order=order, model=EnderecoModel)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = EnderecoService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=params, order=order)

            result = PaginatedResponseEnderecoType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_list_sql(
        self,
        info: Info,
        params: EnderecoParamsInput | None = None,
        order: list[OrderInput] | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseEnderecoType:
        try:
            validate_params(params=params, schema=EnderecoParams)

            params = set_filters_params(params=params)
            order = set_order_params(order=order, schema=EnderecoListItem)
            final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

            session = info.context["session"]
            service = EnderecoService(session=session)
            total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=params, order=order)

            result = PaginatedResponseEnderecoType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_by_id(
        self,
        info: Info,
        param: EnderecoParamInput
    ) -> SingleResponseEnderecoType:
        try:
            validate_params(params=param, schema=EnderecoParam)

            session = info.context["session"]
            service = EnderecoService(session=session)
            item = await service.get_by_id(id=param.id_endereco)

            result = SingleResponseEnderecoType(item=item)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
