from typing import Any, Dict

from sqlalchemy.orm import DeclarativeMeta

from fastapi import HTTPException

from graphql import GraphQLError

import strawberry
from strawberry.types import Info

from app.graphql.schema.input.contribuinte_input import ContribuinteFiltersInput, OrderInput
from app.graphql.schema.type.contribuinte_type import ContribuinteType, PaginatedResponseType, SingleResponseType
from app.model.contribuinte_model import ContribuinteModel
from app.service.contribuinte_service import ContribuinteService
from app.utils.exception_util import raise_http_exception
from app.utils.response_util import normalize_pagination_params


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def get_list(self, info: Info, filters: ContribuinteFiltersInput | None = None, order: list[OrderInput] | None = None, offset: int | None = None, limit: int | None = None, ) -> PaginatedResponseType:
        try:
            # Validação equivalente ao Query(ge=...)
            if offset is not None and offset < 0:
                raise GraphQLError("offset deve ser >= 0")

            if limit is not None and limit < 1:
                raise GraphQLError("limit deve ser >= 1")

            final_offset, final_limit, _ = normalize_pagination_params(
                offset=offset,
                limit=limit
            )

            session = info.context["session"]
            service = ContribuinteService(session=session)

            filters = filters_input_to_dict(filters)
            order = order_by_input_to_list(order, ContribuinteModel)

            total, items = await service.get_list(
                filters=filters,
                order=order,
                offset=final_offset,
                limit=final_limit
            )

            return PaginatedResponseType(
                offset=final_offset,
                limit=final_limit,
                total=total,
                data=[ContribuinteType.from_orm(c) for c in items]
            )
        except Exception as e:
            raise_http_exception(exc=e)


    @strawberry.field
    async def get_by_cd(self, info: Info, cd_contribuinte: str) -> SingleResponseType:
        try:
            session = info.context["session"]
            service = ContribuinteService(session=session)

            result = await service.get_by_cd(cd=cd_contribuinte)
        except Exception as e:
            raise_http_exception(exc=e)

        if not result:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

        return SingleResponseType(data=result)


def filters_input_to_dict(filters: ContribuinteFiltersInput | None) -> Dict[str, Any]:
    if not filters:
        return {}

    return {k: v for k, v in vars(filters).items() if v is not None}

def order_by_input_to_list(order: list[OrderInput] | None, model: DeclarativeMeta) -> list[tuple[str, str]]:
    if not order:
        return []

    seen = set()
    result = []

    for item in order:
        field = item.field
        direction = item.direction.value  # "asc" | "des"

        if not hasattr(model, field):
            continue

        if field not in seen:
            seen.add(field)
            result.append((field, direction))

    return result
