"""
Contract test suite for the FetchHive Python client.

Covers the SDK test matrix: C1-C5, A1-A2, P1-P3, W1-W3, AG1-AG3, S1-S3, E1-E2.
Uses respx to mock httpx — no real network calls are made.
"""
import json
import os

import httpx
import pytest
import respx

from fetch_hive_sdk import FetchHive

DEFAULT_BASE = "https://api.fetchhive.com/v1"


# ── C: Construction ────────────────────────────────────────────────────────────


def test_c1_missing_api_key_raises(monkeypatch):
    """C1 — missing api_key and no env var raises ValueError."""
    monkeypatch.delenv("FETCH_HIVE_API_KEY", raising=False)
    with pytest.raises(ValueError, match="api_key is required"):
        FetchHive()


def test_c2_env_var_fallback(monkeypatch):
    """C2 — FETCH_HIVE_API_KEY env var is used as fallback."""
    monkeypatch.setenv("FETCH_HIVE_API_KEY", "env-key")
    client = FetchHive()
    assert client._api_key == "env-key"


@respx.mock
def test_c3_custom_base_url_respected():
    """C3 — custom base_url is used for requests."""
    respx.post("https://custom.example.com/api/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="k", base_url="https://custom.example.com/api")
    client.invoke_prompt(deployment="d")
    assert respx.calls.last.request.url.host == "custom.example.com"


@respx.mock
def test_c4_trailing_slash_stripped():
    """C4 — trailing slash on base_url is stripped so URLs don't get double-slashes."""
    respx.post("https://custom.example.com/api/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="k", base_url="https://custom.example.com/api/")
    client.invoke_prompt(deployment="d")
    url = str(respx.calls.last.request.url)
    assert "//" not in url.replace("https://", "")


@respx.mock
def test_c5_default_base_url():
    """C5 — default base_url is https://api.fetchhive.com/v1."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="k")
    client.invoke_prompt(deployment="d")
    assert DEFAULT_BASE in str(respx.calls.last.request.url)


# ── A: Auth headers ────────────────────────────────────────────────────────────


@respx.mock
def test_a1_authorization_header():
    """A1 — Authorization: Bearer <key> header is sent on every request."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="my-secret-key")
    client.invoke_prompt(deployment="d")
    assert respx.calls.last.request.headers["authorization"] == "Bearer my-secret-key"


@respx.mock
def test_a2_content_type_header():
    """A2 — Content-Type: application/json is sent."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="k")
    client.invoke_prompt(deployment="d")
    assert respx.calls.last.request.headers["content-type"] == "application/json"


# ── P: Prompt ──────────────────────────────────────────────────────────────────


@respx.mock
def test_p1_p2_invoke_prompt():
    """P1+P2 — POSTs to /invoke with streaming:false and returns body."""
    mock_body = {"request_id": "req_1", "response": "Hello, Alice!", "model": "gpt-4o"}
    respx.post(f"{DEFAULT_BASE}/invoke").mock(return_value=httpx.Response(200, json=mock_body))

    result = FetchHive(api_key="k").invoke_prompt(deployment="my-prompt", inputs={"name": "Alice"})

    request = respx.calls.last.request
    body = json.loads(request.content)
    assert body["deployment"] == "my-prompt"
    assert body["streaming"] is False
    assert result["response"] == "Hello, Alice!"


@respx.mock
def test_p3_optional_fields_omitted_when_absent():
    """P3 — optional fields not included in body when not provided."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(return_value=httpx.Response(200, json={"response": "ok"}))
    FetchHive(api_key="k").invoke_prompt(deployment="d")

    body = json.loads(respx.calls.last.request.content)
    assert "variant" not in body or body.get("variant") == ""
    assert "inputs" not in body
    assert "user" not in body


@respx.mock
def test_p3_optional_fields_included_when_provided():
    """P3 — optional fields appear in body when provided."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(return_value=httpx.Response(200, json={"response": "ok"}))
    FetchHive(api_key="k").invoke_prompt(deployment="d", variant="v2", inputs={"x": 1}, user="u1")

    body = json.loads(respx.calls.last.request.content)
    assert body["variant"] == "v2"
    assert body["inputs"] == {"x": 1}
    assert body["user"] == "u1"


# ── W: Workflow ────────────────────────────────────────────────────────────────


@respx.mock
def test_w1_w2_invoke_workflow():
    """W1+W2 — POSTs to /workflow/invoke and returns body."""
    mock_body = {"request_id": "r", "run_id": "run_1", "status": "completed", "output": "done"}
    respx.post(f"{DEFAULT_BASE}/workflow/invoke").mock(return_value=httpx.Response(200, json=mock_body))

    result = FetchHive(api_key="k").invoke_workflow(deployment="my-workflow", inputs={"x": 1})

    assert result["status"] == "completed"
    assert str(respx.calls.last.request.url).endswith("/workflow/invoke")


@respx.mock
def test_w3_async_mode_builds_correct_block():
    """W3 — async_mode=True with callback_url builds the correct async block."""
    respx.post(f"{DEFAULT_BASE}/workflow/invoke").mock(
        return_value=httpx.Response(200, json={"status": "queued"})
    )
    FetchHive(api_key="k").invoke_workflow(
        deployment="d",
        async_mode=True,
        callback_url="https://example.com/cb",
    )

    body = json.loads(respx.calls.last.request.content)
    assert body["async"] == {"enabled": True, "callback_url": "https://example.com/cb"}


# ── AG: Agent ──────────────────────────────────────────────────────────────────


@respx.mock
def test_ag1_ag2_invoke_agent():
    """AG1+AG2 — POSTs to /agent/invoke with streaming:false and returns body."""
    mock_body = {"request_id": "r", "response": "Hi there"}
    respx.post(f"{DEFAULT_BASE}/agent/invoke").mock(return_value=httpx.Response(200, json=mock_body))

    result = FetchHive(api_key="k").invoke_agent(agent="my-agent", message="Hi")

    body = json.loads(respx.calls.last.request.content)
    assert body["streaming"] is False
    assert result["response"] == "Hi there"


@respx.mock
def test_ag3_optional_fields_omitted_when_absent():
    """AG3 — optional agent fields not included in body when not provided."""
    respx.post(f"{DEFAULT_BASE}/agent/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    FetchHive(api_key="k").invoke_agent(agent="a", message="m")

    body = json.loads(respx.calls.last.request.content)
    assert not body.get("thread_id")
    assert "user" not in body
    assert "messages" not in body
    assert "image_urls" not in body


@respx.mock
def test_ag3_optional_fields_included_when_provided():
    """AG3 — optional agent fields appear in body when provided."""
    respx.post(f"{DEFAULT_BASE}/agent/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    FetchHive(api_key="k").invoke_agent(
        agent="a",
        message="m",
        thread_id="tid",
        user="u1",
        messages=[{"role": "user", "content": "prev"}],
        image_urls=["https://img.example.com/1.png"],
    )

    body = json.loads(respx.calls.last.request.content)
    assert body["thread_id"] == "tid"
    assert body["user"] == "u1"
    assert len(body["messages"]) == 1
    assert len(body["image_urls"]) == 1


# ── S: Streaming ───────────────────────────────────────────────────────────────

SSE_RESPONSE = b"data: {\"type\":\"response\",\"response\":\"Hello\"}\n\ndata: [DONE]\n\n"


@respx.mock
def test_s1_invoke_prompt_stream():
    """S1 — invoke_prompt_stream sends streaming:true and yields events."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(
        return_value=httpx.Response(200, stream=httpx.ByteStream(SSE_RESPONSE))
    )

    chunks = list(FetchHive(api_key="k").invoke_prompt_stream(deployment="d"))

    body = json.loads(respx.calls.last.request.content)
    assert body["streaming"] is True
    assert len(chunks) == 1
    assert chunks[0]["response"] == "Hello"


@respx.mock
def test_s2_invoke_agent_stream():
    """S2 — invoke_agent_stream sends streaming:true and yields events."""
    respx.post(f"{DEFAULT_BASE}/agent/invoke").mock(
        return_value=httpx.Response(200, stream=httpx.ByteStream(SSE_RESPONSE))
    )

    chunks = list(FetchHive(api_key="k").invoke_agent_stream(agent="a", message="m"))

    body = json.loads(respx.calls.last.request.content)
    assert body["streaming"] is True
    assert len(chunks) == 1
    assert chunks[0]["response"] == "Hello"


@pytest.mark.asyncio
@respx.mock
async def test_s3_async_invoke_prompt_stream():
    """S3 — ainvoke_prompt_stream (async) sends streaming:true and yields events."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(
        return_value=httpx.Response(200, stream=httpx.ByteStream(SSE_RESPONSE))
    )

    chunks = []
    async for chunk in FetchHive(api_key="k").ainvoke_prompt_stream(deployment="d"):
        chunks.append(chunk)

    body = json.loads(respx.calls.last.request.content)
    assert body["streaming"] is True
    assert len(chunks) == 1
    assert chunks[0]["response"] == "Hello"


@pytest.mark.asyncio
@respx.mock
async def test_s3_async_invoke_agent_stream():
    """S3 — ainvoke_agent_stream (async) sends streaming:true and yields events."""
    respx.post(f"{DEFAULT_BASE}/agent/invoke").mock(
        return_value=httpx.Response(200, stream=httpx.ByteStream(SSE_RESPONSE))
    )

    chunks = []
    async for chunk in FetchHive(api_key="k").ainvoke_agent_stream(agent="a", message="m"):
        chunks.append(chunk)

    assert len(chunks) == 1
    assert chunks[0]["response"] == "Hello"


# ── E: Error handling ─────────────────────────────────────────────────────────


@respx.mock
def test_e1_non_2xx_on_non_streaming_raises():
    """E1 — non-2xx response on non-streaming endpoint raises httpx.HTTPStatusError."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(
        return_value=httpx.Response(500, text="Internal Server Error")
    )
    with pytest.raises(httpx.HTTPStatusError):
        FetchHive(api_key="k").invoke_prompt(deployment="d")


@respx.mock
def test_e2_non_2xx_on_streaming_raises():
    """E2 — non-2xx response on streaming endpoint raises before yielding."""
    respx.post(f"{DEFAULT_BASE}/invoke").mock(
        return_value=httpx.Response(401, text="Unauthorized")
    )
    with pytest.raises(httpx.HTTPStatusError):
        list(FetchHive(api_key="k").invoke_prompt_stream(deployment="d"))
