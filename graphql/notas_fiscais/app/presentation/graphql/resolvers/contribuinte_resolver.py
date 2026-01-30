import strawberry
from strawberry.types import Info

from app.presentation.graphql.schemas.contribuinte_schema import ContribuinteFilterSchema
from app.core.exception import raise_graphql_error
from app.domain.services.contribuinte_service import ContribuinteService
from app.presentation.graphql.inputs.contribuinte_input import ContribuinteOrderInput, ContribuinteFilterInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.mappers.schema_mapper import map_to_schema
from app.presentation.graphql.types.contribuinte_type import PaginatedResponseContribuinteType


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        filter: ContribuinteFilterInput | None = None,
        order: ContribuinteOrderInput | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseContribuinteType:
        try:
            filter_schema = map_to_schema(data=filter, schema=ContribuinteFilterSchema)
            final_offset, final_limit, final_accept_ranges = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            service = ContribuinteService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filter=filter_schema, order=order)

            result = PaginatedResponseContribuinteType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges, items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
