from pydantic import BaseModel, Field

from app.domain.values.contribuinte_value import CdContribuinte
from app.domain.values.data_value import year_month_validator_not_future
# from app.domain.values.data_value import year_month_not_future, year_month_validator_not_future


class ContribuinteDanfeMonthlyFilterInputValidator(BaseModel):
    cd_contribuinte: CdContribuinte
    year: int = Field(..., ge=1900)
    month: int = Field(..., ge=1, le=12)

    _validate_year_month = year_month_validator_not_future("year", "month")
