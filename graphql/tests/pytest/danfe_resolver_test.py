from pathlib import Path

import httpx
import pytest

from tests.benchmark_core import measure_all
from tests.pytest.benchmark_pytest import assert_benchmark

BASE_PATH_QUERY = "tests/queries/danfe_query/"
BASE_URL = "http://localhost:8080"
URL = "/graphql"


def load_query(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


# @pytest.mark.asyncio
@pytest.mark.skip(reason="Desativado para ambiente produtivo")
async def test_danfes_json_banco():
    query = load_query(BASE_PATH_QUERY + "danfes_json_banco.graphql")

    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post(url=URL, json={"query": query}, headers={"Content-Type": "application/json"})
        data = response.json()

    metrics = measure_all(lambda: data)
    assert_benchmark(metrics)


# @pytest.mark.asyncio
@pytest.mark.skip(reason="Desativado para ambiente produtivo")
async def test_danfes_json_python():
    query = load_query(BASE_PATH_QUERY + "danfes_json_python.graphql")

    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post(url=URL, json={"query": query}, headers={"Content-Type": "application/json"})
        data = response.json()

    metrics = measure_all(lambda: data)

    metrics = measure_all(lambda: data)
    assert_benchmark(metrics)
