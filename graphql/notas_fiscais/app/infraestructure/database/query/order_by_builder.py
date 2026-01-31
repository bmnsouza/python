from typing import Optional

from app.presentation.graphql.inputs.order_input import OrderDirection


def build_order_by(order: Optional[object]) -> str:
    if not order:
        return ""

    clauses = []

    for field, direction in vars(order).items():
        if direction is None:
            continue

        sql_direction = "ASC" if direction == OrderDirection.ASC else "DESC"
        clauses.append(f"{field} {sql_direction}")

    if not clauses:
        return ""

    return " ORDER BY " + ", ".join(clauses)
