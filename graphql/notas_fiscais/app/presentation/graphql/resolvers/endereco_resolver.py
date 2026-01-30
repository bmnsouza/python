import strawberry
from strawberry.types import Info

from app.core.exception import raise_graphql_error
from app.domain.services.endereco_service import EnderecoService
from app.presentation.graphql.inputs.endereco_input import EnderecoFilterInput, EnderecoOrderInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.mappers.schema_mapper import map_to_schema
from app.presentation.graphql.schemas.endereco_schema import EnderecoFilterSchema
from app.presentation.graphql.types.endereco_type import PaginatedResponseEnderecoType


@strawberry.type
class EnderecoQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        filter: EnderecoFilterInput | None = None,
        order: EnderecoOrderInput | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseEnderecoType:
        try:
            filter_schema = map_to_schema(data=filter, schema=EnderecoFilterSchema)
            final_offset, final_limit, final_accept_ranges = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            service = EnderecoService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filter=filter_schema, order=order)

            result = PaginatedResponseEnderecoType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
