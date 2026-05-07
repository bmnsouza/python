from pathlib import Path

from locust import HttpUser, task

from tests.locust.benchmark_locust import benchmark_request


class BaseGraphQLUser(HttpUser):
    abstract = True

    def get_query_file(self) -> Path:
        class_name = self.__class__.__name__.replace("User", "")
        file_name = "".join(["_" + c.lower() if c.isupper() else c for c in class_name]).lstrip("_") + ".graphql"

        return Path("tests/queries") / file_name

    def get_request_name(self) -> str:
        # Usa o nome do arquivo sem extensão como identificador
        return self.get_query_file().stem

    @task
    def run_query(self):
        query_file = self.get_query_file()
        query_text = query_file.read_text(encoding="utf-8")

        response = self.client.post(
            "/graphql",
            json={"query": query_text},
            headers={"Content-Type": "application/json"},
        )

        benchmark_request(self.get_request_name(), response.json())
