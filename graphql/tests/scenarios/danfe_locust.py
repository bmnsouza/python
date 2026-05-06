from tests.locust_base import BaseGraphQLUser


class DanfesJsonPythonUser(BaseGraphQLUser):
    weight = 1
    query_path = "danfe_resolver/danfes_json_python.graphql"
    request_name = "danfes_json_python"


class DanfesJsonBancoUser(BaseGraphQLUser):
    weight = 1
    query_path = "danfe_resolver/danfes_json_banco.graphql"
    request_name = "danfes_json_banco"
