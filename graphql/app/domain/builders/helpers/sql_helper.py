from sqlalchemy import text


class SqlHelper:

    @staticmethod
    def paginate(query: str, order_by: str) -> str:
        return text(f"""
        SELECT *
        FROM (
            SELECT r.*,
                ROW_NUMBER() OVER (ORDER BY {order_by}) rn
            FROM (
                {query}
            ) r
            ORDER BY {order_by}
        )
        WHERE rn > :offset
        AND rn <= :offset + :limit
        """)
