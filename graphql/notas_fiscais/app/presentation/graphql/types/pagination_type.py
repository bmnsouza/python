import strawberry

@strawberry.type
class PaginationType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
