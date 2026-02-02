
def build_order_by(order: dict[str, str]) -> str:
    if not order:
        return ""

    clauses = []

    for field, direction in order.items():
        if direction is None:
            continue

        sql_direction = "ASC"
        if str(direction).upper() == "DESC":
            sql_direction = "DESC"

        clauses.append(f"{field} {sql_direction}")

    if not clauses:
        return ""

    return " ORDER BY " + ", ".join(clauses)
