"""
Unit tests for the FetchHive Python client.
Uses respx to mock httpx — no real network calls.
"""
import pytest
import respx
import httpx

from fetch_hive_sdk import FetchHive


@pytest.fixture
def client():
    return FetchHive(api_key="test-key")


def test_constructor_requires_api_key():
    import os
    original = os.environ.pop("FETCH_HIVE_API_KEY", None)
    try:
        with pytest.raises(ValueError, match="api_key is required"):
            FetchHive()
    finally:
        if original is not None:
            os.environ["FETCH_HIVE_API_KEY"] = original


def test_constructor_reads_env_var(monkeypatch):
    monkeypatch.setenv("FETCH_HIVE_API_KEY", "env-key")
    c = FetchHive()
    assert c._api_key == "env-key"


@respx.mock
def test_invoke_prompt(client):
    mock_body = {"request_id": "req_1", "response": "Hello, Alice!", "model": "gpt-4o"}
    respx.post("https://api.fetchhive.com/v1/invoke").mock(
        return_value=httpx.Response(200, json=mock_body)
    )

    result = client.invoke_prompt(deployment="my-prompt", inputs={"name": "Alice"})

    assert result["response"] == "Hello, Alice!"
    request = respx.calls.last.request
    import json
    body = json.loads(request.content)
    assert body["deployment"] == "my-prompt"
    assert body["streaming"] is False


@respx.mock
def test_invoke_agent(client):
    mock_body = {"request_id": "req_2", "response": "Hi there"}
    respx.post("https://api.fetchhive.com/v1/agent/invoke").mock(
        return_value=httpx.Response(200, json=mock_body)
    )

    result = client.invoke_agent(agent="my-agent", message="Hi")

    assert result["response"] == "Hi there"
    request = respx.calls.last.request
    import json
    body = json.loads(request.content)
    assert body["agent"] == "my-agent"
    assert body["streaming"] is False


@respx.mock
def test_invoke_workflow(client):
    mock_body = {"request_id": "req_3", "run_id": "run_abc", "status": "completed", "output": "done"}
    respx.post("https://api.fetchhive.com/v1/workflow/invoke").mock(
        return_value=httpx.Response(200, json=mock_body)
    )

    result = client.invoke_workflow(deployment="my-workflow", inputs={"x": 1})

    assert result["status"] == "completed"
