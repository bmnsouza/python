def assert_graphql_response(payload: dict):
    assert "data" in payload
    assert payload["data"] is not None
