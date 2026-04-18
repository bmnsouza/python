from sqlalchemy import text


class SqlHelper:

    @staticmethod
    def paginate(query: str, order_by: str) -> text:
        return text(f"""
        SELECT *
        FROM (
            {query}
        )
        ORDER BY {order_by}
        OFFSET :offset ROWS FETCH NEXT :limit ROWS ONLY
        """)
