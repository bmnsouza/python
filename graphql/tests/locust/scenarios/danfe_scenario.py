from tests.locust.locust_base import BaseGraphQLUser

QUERY_FOLDER = "queries/danfe_query"


class DanfesJsonBancoUser(BaseGraphQLUser):
    query_folder = QUERY_FOLDER


class DanfesJsonPythonUser(BaseGraphQLUser):
    query_folder = QUERY_FOLDER
