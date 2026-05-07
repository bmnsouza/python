from tests.locust.locust_base import BaseGraphQLUser

QUERY_FOLDER = "queries/danfe_query"


class DanfesJsonPythonUser(BaseGraphQLUser):
    query_folder = QUERY_FOLDER


class DanfesJsonBancoUser(BaseGraphQLUser):
    query_folder = QUERY_FOLDER
