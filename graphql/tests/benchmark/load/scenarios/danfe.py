from tests.benchmark.load.base_user import BaseGraphQLUser

QUERY_FOLDER = "danfe"


class DanfesJsonBancoUser(BaseGraphQLUser):
    query_folder = QUERY_FOLDER


class DanfesJsonPythonUser(BaseGraphQLUser):
    query_folder = QUERY_FOLDER
