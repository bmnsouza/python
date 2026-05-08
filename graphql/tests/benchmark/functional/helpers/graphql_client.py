from pathlib import Path

import httpx

BASE_URL = "http://localhost:8080"
URL = "/graphql"


class GraphQLClient:
    def __init__(self):
        print(">>> __init__ <<<")
        self.client = httpx.AsyncClient(
            base_url="http://localhost:8080",
            timeout=5.0,
        )

    async def execute_query(self, query_path: str) -> dict:
        query = Path(query_path).read_text(encoding="utf-8")

        print(">>> query:", query)

        try:
            response = await self.client.post(
                url="http://localhost:8080/graphql",
                json={"query": query},
                headers={"Content-Type": "application/json"},
            )
            return response.json()

        except httpx.ConnectTimeout:
            raise RuntimeError(
                f"Servidor não está respondendo em {BASE_URL + URL}. "
                "Suba a aplicação antes de rodar os testes."
            )
        except Exception as ex:
            raise RuntimeError(ex)
