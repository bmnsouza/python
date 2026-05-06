from pathlib import Path

from locust import HttpUser, task, between


QUERY_ROOT = Path(__file__).parent / "queries"


def load_query(relative_path: str) -> str:
    return (QUERY_ROOT / relative_path).read_text(encoding="utf-8")


class BaseGraphQLUser(HttpUser):
    host = "http://localhost:8080"
    wait_time = between(0.1, 0.3)
    abstract = True

    query_path = None
    request_name = None
    gql_query = None

    def on_start(self):
        if not self.query_path:
            raise ValueError("query_path não definido")

        self.gql_query = load_query(self.query_path)

    @task
    def execute_graphql(self):
        with self.client.post(
            "/graphql",
            json={"query": self.gql_query},
            headers={"Content-Type": "application/json"},
            name=self.request_name or self.query_path,
            catch_response=True,
        ) as response:

            if response.status_code != 200:
                response.failure(f"HTTP {response.status_code}")
