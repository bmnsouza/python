import strawberry


@strawberry.input
class ContribuinteDanfeMonthlyFilterInput:
    cd_contribuinte: str
    year: int
    month: int
