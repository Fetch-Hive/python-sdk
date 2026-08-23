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
    respx.post("https://custom.example.com/api/prompt/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="k", base_url="https://custom.example.com/api")
    client.invoke_prompt(deployment="d")
    assert respx.calls.last.request.url.host == "custom.example.com"


@respx.mock
def test_c4_trailing_slash_stripped():
    """C4 — trailing slash on base_url is stripped so URLs don't get double-slashes."""
    respx.post("https://custom.example.com/api/prompt/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="k", base_url="https://custom.example.com/api/")
    client.invoke_prompt(deployment="d")
    url = str(respx.calls.last.request.url)
    assert "//" not in url.replace("https://", "")


@respx.mock
def test_c5_default_base_url():
    """C5 — default base_url is https://api.fetchhive.com/v1."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="k")
    client.invoke_prompt(deployment="d")
    assert DEFAULT_BASE in str(respx.calls.last.request.url)


# ── A: Auth headers ────────────────────────────────────────────────────────────


@respx.mock
def test_a1_authorization_header():
    """A1 — Authorization: Bearer <key> header is sent on every request."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="my-secret-key")
    client.invoke_prompt(deployment="d")
    assert respx.calls.last.request.headers["authorization"] == "Bearer my-secret-key"


@respx.mock
def test_a2_content_type_header():
    """A2 — Content-Type: application/json is sent."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )
    client = FetchHive(api_key="k")
    client.invoke_prompt(deployment="d")
    assert respx.calls.last.request.headers["content-type"] == "application/json"


# ── P: Prompt ──────────────────────────────────────────────────────────────────


@respx.mock
def test_p1_p2_invoke_prompt():
    """P1+P2 — POSTs to /prompt/invoke with streaming:false and returns body."""
    mock_body = {"request_id": "req_1", "response": "Hello, Alice!", "model": "gpt-4o"}
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(return_value=httpx.Response(200, json=mock_body))

    result = FetchHive(api_key="k").invoke_prompt(deployment="my-prompt", inputs={"name": "Alice"})

    request = respx.calls.last.request
    body = json.loads(request.content)
    assert body["deployment"] == "my-prompt"
    assert body["streaming"] is False
    assert result["response"] == "Hello, Alice!"


@respx.mock
def test_p3_optional_fields_omitted_when_absent():
    """P3 — optional fields not included in body when not provided."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(return_value=httpx.Response(200, json={"response": "ok"}))
    FetchHive(api_key="k").invoke_prompt(deployment="d")

    body = json.loads(respx.calls.last.request.content)
    assert "variant" not in body or body.get("variant") == ""
    assert "inputs" not in body
    assert "user" not in body


@respx.mock
def test_p3_optional_fields_included_when_provided():
    """P3 — optional fields appear in body when provided."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(return_value=httpx.Response(200, json={"response": "ok"}))
    FetchHive(api_key="k").invoke_prompt(
        deployment="d",
        variant="v2",
        inputs={"x": 1},
        user="u1",
        metadata={"customer_id": "cus_123", "trial": False, "invoice_count": 12, "region": None},
    )

    body = json.loads(respx.calls.last.request.content)
    assert body["variant"] == "v2"
    assert body["inputs"] == {"x": 1}
    assert body["user"] == "u1"
    assert body["metadata"] == {
        "customer_id": "cus_123",
        "trial": False,
        "invoice_count": 12,
        "region": None,
    }


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


@respx.mock
def test_w4_metadata_passes_through():
    """W4 — metadata appears in workflow invoke body."""
    respx.post(f"{DEFAULT_BASE}/workflow/invoke").mock(
        return_value=httpx.Response(200, json={"status": "completed"})
    )
    FetchHive(api_key="k").invoke_workflow(
        deployment="d",
        metadata={"customer_id": "cus_123", "invoice_count": 12},
    )

    body = json.loads(respx.calls.last.request.content)
    assert body["metadata"] == {"customer_id": "cus_123", "invoice_count": 12}


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
    assert "attachments" not in body


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
        metadata={"customer_id": "cus_123", "trial": False},
        messages=[{"role": "user", "content": "prev"}],
        attachments=["https://img.example.com/1.png"],
        known_artifact_refs=["11111111-1111-4111-8111-111111111111"],
        artifact_refs=["11111111-1111-4111-8111-111111111111"],
    )

    body = json.loads(respx.calls.last.request.content)
    assert body["thread_id"] == "tid"
    assert body["user"] == "u1"
    assert body["metadata"] == {"customer_id": "cus_123", "trial": False}
    assert len(body["messages"]) == 1
    assert len(body["attachments"]) == 1
    assert body["artifact_refs"] == body["known_artifact_refs"]


# ── HA: Hive Agent ─────────────────────────────────────────────────────────────


@respx.mock
def test_ha1_ha2_invoke_hive_agent():
    """HA1+HA2 — invoke_hive_agent POSTs to /hive-agent/invoke and returns parsed JSON."""
    respx.post(f"{DEFAULT_BASE}/hive-agent/invoke").mock(
        return_value=httpx.Response(
            202,
            json={"run_id": "run_1", "request_id": "req_1", "status": "pending", "webhook_secret": "whsec_x"},
        )
    )
    result = FetchHive(api_key="k").invoke_hive_agent(
        hive_agent="agt_1",
        objective="Research competitors",
        callback_url="https://example.com/cb",
    )
    assert str(respx.calls.last.request.url).endswith("/hive-agent/invoke")
    assert result["run_id"] == "run_1"
    assert result["webhook_secret"] == "whsec_x"


@respx.mock
def test_ha3_async_block_and_missing_callback():
    """HA3 — body always includes async.enabled true; missing callback_url raises."""
    respx.post(f"{DEFAULT_BASE}/hive-agent/invoke").mock(
        return_value=httpx.Response(202, json={"status": "pending"})
    )
    FetchHive(api_key="k").invoke_hive_agent(
        hive_agent="agt_1",
        objective="Research competitors",
        callback_url="https://example.com/cb",
    )
    body = json.loads(respx.calls.last.request.content)
    assert body["async"] == {"enabled": True, "callback_url": "https://example.com/cb"}

    with pytest.raises(ValueError, match="callback_url is required"):
        FetchHive(api_key="k").invoke_hive_agent(
            hive_agent="agt_1",
            objective="Research competitors",
            callback_url="",
        )


@respx.mock
def test_ha4_optional_sources_and_metadata():
    """HA4 — optional sources and metadata included only when provided."""
    respx.post(f"{DEFAULT_BASE}/hive-agent/invoke").mock(
        return_value=httpx.Response(202, json={"status": "pending"})
    )
    client = FetchHive(api_key="k")
    client.invoke_hive_agent(
        hive_agent="agt_1",
        objective="Research competitors",
        callback_url="https://example.com/cb",
    )
    first = json.loads(respx.calls[0].request.content)
    assert "sources" not in first
    assert "metadata" not in first

    client.invoke_hive_agent(
        hive_agent="agt_1",
        objective="Research competitors",
        callback_url="https://example.com/cb",
        sources={"website_urls": ["https://example.com"]},
        metadata={"customer_id": "cus_123"},
    )
    second = json.loads(respx.calls[1].request.content)
    assert second["sources"] == {"website_urls": ["https://example.com"]}
    assert second["metadata"] == {"customer_id": "cus_123"}


@respx.mock
def test_kb1_knowledge_base_helpers():
    """KB1 — knowledge base helpers hit expected paths."""
    respx.get(f"{DEFAULT_BASE}/public/workspaces/ws_1/knowledge_bases").mock(
        return_value=httpx.Response(200, json={"knowledge_bases": []})
    )
    respx.post(f"{DEFAULT_BASE}/public/workspaces/ws_1/knowledge_bases").mock(
        return_value=httpx.Response(200, json={"knowledge_base": {"id": "kb_1"}})
    )
    client = FetchHive(api_key="k")
    client.list_knowledge_bases("ws_1")
    client.create_knowledge_base("ws_1", {"name": "KB"})
    assert respx.calls[0].request.method == "GET"
    assert respx.calls[1].request.method == "POST"


@respx.mock
def test_kbi1_knowledge_base_item_helpers():
    """KBI1 — knowledge base item helpers hit expected paths."""
    respx.get(f"{DEFAULT_BASE}/public/workspaces/ws_1/knowledge_bases/kb_1/items").mock(
        return_value=httpx.Response(200, json={"knowledge_base_items": []})
    )
    respx.post(f"{DEFAULT_BASE}/public/workspaces/ws_1/knowledge_bases/kb_1/items/item_1/regenerate").mock(
        return_value=httpx.Response(200, json={"request_id": "req_1"})
    )
    client = FetchHive(api_key="k")
    client.list_knowledge_base_items("ws_1", "kb_1")
    client.regenerate_knowledge_base_item("ws_1", "kb_1", "item_1")
    assert "/items" in str(respx.calls[0].request.url)
    assert str(respx.calls[1].request.url).endswith("/regenerate")


@respx.mock
def test_pa1_public_agent_helpers():
    """PA1 — public agent helpers hit expected paths."""
    respx.get(f"{DEFAULT_BASE}/public/workspaces/ws_1/agents").mock(
        return_value=httpx.Response(200, json={"agents": []})
    )
    FetchHive(api_key="k").list_agents("ws_1")
    assert str(respx.calls.last.request.url).endswith("/agents")


@respx.mock
def test_pac1_agent_chat_helpers():
    """PAC1 — agent chat helpers hit expected paths."""
    respx.post(f"{DEFAULT_BASE}/public/workspaces/ws_1/agents/agt_1/chats").mock(
        return_value=httpx.Response(200, json={"chat": {"id": "c1"}})
    )
    respx.patch(f"{DEFAULT_BASE}/public/workspaces/ws_1/agents/agt_1/chats/cht_1/clear_messages").mock(
        return_value=httpx.Response(200, json={"message": "cleared"})
    )
    client = FetchHive(api_key="k")
    client.create_agent_chat("ws_1", "agt_1", {"name": "Chat"})
    client.clear_agent_chat_messages("ws_1", "agt_1", "cht_1")
    assert respx.calls[0].request.method == "POST"
    assert respx.calls[1].request.method == "PATCH"


@respx.mock
def test_r1_get_request():
    """R1 — get_request GETs /public/requests/:id."""
    respx.get(f"{DEFAULT_BASE}/public/requests/req_1").mock(
        return_value=httpx.Response(200, json={"request": {"id": "req_1"}})
    )
    result = FetchHive(api_key="k").get_request("req_1")
    assert respx.calls.last.request.method == "GET"
    assert result["request"]["id"] == "req_1"


# ── S: Streaming ───────────────────────────────────────────────────────────────

SSE_RESPONSE = b"data: {\"type\":\"response\",\"response\":\"Hello\"}\n\ndata: [DONE]\n\n"


@respx.mock
def test_s1_invoke_prompt_stream():
    """S1 — invoke_prompt_stream sends streaming:true and yields events."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(
        return_value=httpx.Response(200, stream=httpx.ByteStream(SSE_RESPONSE))
    )

    chunks = list(
        FetchHive(api_key="k").invoke_prompt_stream(
            deployment="d",
            metadata={"plan": "enterprise"},
        )
    )

    body = json.loads(respx.calls.last.request.content)
    assert body["streaming"] is True
    assert body["metadata"] == {"plan": "enterprise"}
    assert len(chunks) == 1
    assert chunks[0]["response"] == "Hello"


@respx.mock
def test_s2_invoke_agent_stream():
    """S2 — invoke_agent_stream sends streaming:true and yields events."""
    respx.post(f"{DEFAULT_BASE}/agent/invoke").mock(
        return_value=httpx.Response(200, stream=httpx.ByteStream(SSE_RESPONSE))
    )

    chunks = list(
        FetchHive(api_key="k").invoke_agent_stream(
            agent="a",
            message="m",
            metadata={"plan": "enterprise"},
        )
    )

    body = json.loads(respx.calls.last.request.content)
    assert body["streaming"] is True
    assert body["metadata"] == {"plan": "enterprise"}
    assert len(chunks) == 1
    assert chunks[0]["response"] == "Hello"


@pytest.mark.asyncio
@respx.mock
async def test_s3_async_invoke_prompt_stream():
    """S3 — ainvoke_prompt_stream (async) sends streaming:true and yields events."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(
        return_value=httpx.Response(200, stream=httpx.ByteStream(SSE_RESPONSE))
    )

    chunks = []
    async for chunk in FetchHive(api_key="k").ainvoke_prompt_stream(
        deployment="d",
        metadata={"plan": "enterprise"},
    ):
        chunks.append(chunk)

    body = json.loads(respx.calls.last.request.content)
    assert body["streaming"] is True
    assert body["metadata"] == {"plan": "enterprise"}
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
    async for chunk in FetchHive(api_key="k").ainvoke_agent_stream(
        agent="a",
        message="m",
        metadata={"plan": "enterprise"},
    ):
        chunks.append(chunk)

    body = json.loads(respx.calls.last.request.content)
    assert body["metadata"] == {"plan": "enterprise"}
    assert len(chunks) == 1
    assert chunks[0]["response"] == "Hello"


# ── E: Error handling ─────────────────────────────────────────────────────────


@respx.mock
def test_e1_non_2xx_on_non_streaming_raises():
    """E1 — non-2xx response on non-streaming endpoint raises httpx.HTTPStatusError."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(
        return_value=httpx.Response(500, text="Internal Server Error")
    )
    with pytest.raises(httpx.HTTPStatusError):
        FetchHive(api_key="k").invoke_prompt(deployment="d")


@respx.mock
def test_e2_non_2xx_on_streaming_raises():
    """E2 — non-2xx response on streaming endpoint raises before yielding."""
    respx.post(f"{DEFAULT_BASE}/prompt/invoke").mock(
        return_value=httpx.Response(401, text="Unauthorized")
    )
    with pytest.raises(httpx.HTTPStatusError):
        list(FetchHive(api_key="k").invoke_prompt_stream(deployment="d"))
