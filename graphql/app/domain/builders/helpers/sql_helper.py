from sqlalchemy import text


class SqlHelper:

    @staticmethod
    def pagination() -> text:
        return "OFFSET :offset ROWS FETCH NEXT :limit ROWS ONLY"
