import pytest

from tests.benchmark.functional.helpers.assertions import assert_graphql_response
from tests.benchmark.functional.helpers.graphql_client import GraphQLClient


# @pytest.mark.skip(reason="Executar apenas manualmente")
@pytest.mark.asyncio
async def test_danfes_json_banco():
    print(">>> test_danfes_json_banco <<<")

    client = GraphQLClient()

    try:
        payload = await client.execute_query("tests/benchmark/queries/danfe/danfes_json_banco.graphql")

        assert_graphql_response(payload)

        resolver_data = payload["data"]["danfesJsonBanco"]

        assert resolver_data is not None
        assert "edges" in resolver_data
    finally:
        await client.close()


@pytest.mark.skip(reason="Executar apenas manualmente")
# @pytest.mark.asyncio
async def test_danfes_json_python():
    client = GraphQLClient()

    try:
        payload = await client.execute_query("tests/benchmark/queries/danfe/danfes_json_python.graphql")

        assert_graphql_response(payload)

        resolver_data = payload["data"]["danfesJsonPython"]

        assert resolver_data is not None
        assert "edges" in resolver_data
    finally:
        await client.close()
