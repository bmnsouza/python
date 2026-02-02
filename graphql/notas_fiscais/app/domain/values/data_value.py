from datetime import date
from pydantic import field_validator, model_validator


# ----------------------
# Validador de date
# ----------------------
def _validate_field_date_not_future(value: date | None) -> date | None:
    if value is None:
        return value
    if value < date(1900, 1, 1):
        raise ValueError("A Data deve ser maior ou igual a 1900-01-01")
    if value > date.today():
        raise ValueError("A Data não pode ser futura")
    return value

def field_date_validator_not_future(field_name: str):
    return field_validator(field_name, mode="before")(_validate_field_date_not_future)


# ----------------------
# Validador de year/month
# ----------------------
def _validate_year_not_earlier(year: int) -> None:
    if year < 1900:
        raise ValueError("O ano deve ser maior ou igual a 1900")


def _validate_year_month_not_future(year: int, month: int) -> None:
    today = date.today()
    if (year, month) > (today.year, today.month):
        raise ValueError("O ano e o mês informados não podem ser futuros")


def year_month_validator_not_future(year_field: str, month_field: str):
    def wrapper(cls, model):
        year = getattr(model, year_field, None)
        month = getattr(model, month_field, None)
        if year is not None and month is not None:
            _validate_year_not_earlier(year)
            _validate_year_month_not_future(year, month)
        return model
    return model_validator(mode="after")(wrapper)
