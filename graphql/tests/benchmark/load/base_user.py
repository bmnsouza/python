from pathlib import Path

from locust import HttpUser, task

from tests.benchmark.load.reporting.request_metrics import collect_request_metrics


class BaseGraphQLUser(HttpUser):
    abstract = True

    host = "http://localhost:8080"

    query_folder: str = ""
    query_name: str = ""
    query_text: str = ""

    def on_start(self):
        self.query_name = self._build_query_name()
        self.query_text = self.get_query_file().read_text(encoding="utf-8")

    def _build_query_name(self) -> str:
        class_name = self.__class__.__name__.replace("User", "")
        return "".join(["_" + char.lower() if char.isupper() else char for char in class_name]).lstrip("_")

    def get_query_file(self) -> Path:
        return Path("tests") / "resources" / "graphql" / self.query_folder / f"{self.query_name}.graphql"

    @task
    def run_query(self):
        with self.client.post(
            "/graphql",
            json={"query": self.query_text},
            headers={"Content-Type": "application/json"},
            name=self.query_name,
            catch_response=True,
        ) as response:
            try:
                payload = response.json()
            except Exception as exc:
                response.failure(f"Resposta inválida (não é JSON): {exc}")
                return

            if "errors" in payload:
                response.failure(str(payload["errors"]))
                return

            try:
                collect_request_metrics(
                    resolver_name=self.query_name,
                    payload=payload,
                )
            except Exception as exc:
                response.failure(f"Erro ao coletar métricas: {exc}")
                return

            response.success()
