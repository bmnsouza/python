from pathlib import Path

import httpx

BASE_URL = "http://localhost:8080"
URL = "graphql"


class GraphQLClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=BASE_URL,
            timeout=5.0,
        )

    async def close(self):
        await self.client.aclose()

    async def execute_query(self, query_path: str) -> dict:
        query = Path(query_path).read_text(encoding="utf-8")

        try:
            response = await self.client.post(
                url=URL,
                json={"query": query},
            )

            response.raise_for_status()

            return response.json()

        except httpx.ConnectTimeout as ex:
            raise RuntimeError(
                f"Servidor não está respondendo em {BASE_URL}/{URL}. " "Suba a aplicação antes de rodar os testes."
            ) from ex

        except httpx.HTTPError as ex:
            raise RuntimeError(f"Erro HTTP ao chamar GraphQL: {ex}") from ex
