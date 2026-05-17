"""
client.py

Idiomatic facade for the Fetch Hive API.

Usage::

    from fetch_hive_sdk import FetchHive

    client = FetchHive(api_key="fhk_...")

    # Non-streaming prompt
    result = client.invoke_prompt(deployment="my-prompt", inputs={"name": "Alice"})
    print(result["response"])

    # Streaming agent
    for chunk in client.invoke_agent_stream(agent="my-agent", message="Hello"):
        if chunk.get("type") == "delta":
            print(chunk.get("content", ""), end="", flush=True)

Async::

    async for chunk in client.ainvoke_agent_stream(agent="my-agent", message="Hello"):
        ...
"""

from __future__ import annotations

import os
from typing import Any, AsyncIterator, Generator, Iterator

import httpx

from .streaming import aiter_sse, iter_sse

DEFAULT_BASE_URL = "https://api.fetchhive.com/v1"


class FetchHive:
    """
    Fetch Hive API client.

    Args:
        api_key: Bearer token from the Fetch Hive dashboard.
                 Defaults to the ``FETCH_HIVE_API_KEY`` environment variable.
        base_url: API base URL. Defaults to ``https://api.fetchhive.com/v1``.
        timeout: Request timeout in seconds (default: 120).
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 120.0,
    ) -> None:
        resolved_key = api_key or os.environ.get("FETCH_HIVE_API_KEY")
        if not resolved_key:
            raise ValueError(
                "api_key is required. Pass it explicitly or set the "
                "FETCH_HIVE_API_KEY environment variable."
            )
        self._api_key = resolved_key
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout

    @property
    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

    def _url(self, path: str) -> str:
        return f"{self._base_url}{path}"

    # ── Prompt ────────────────────────────────────────────────────────────────

    def invoke_prompt(
        self,
        *,
        deployment: str,
        variant: str = "",
        inputs: dict[str, Any] | None = None,
        user: str | None = None,
    ) -> dict[str, Any]:
        """Invoke a prompt deployment and return the full response."""
        body: dict[str, Any] = {"deployment": deployment, "streaming": False}
        if variant:
            body["variant"] = variant
        if inputs is not None:
            body["inputs"] = inputs
        if user is not None:
            body["user"] = user

        with httpx.Client(timeout=self._timeout) as client:
            resp = client.post(self._url("/invoke"), headers=self._headers, json=body)
            resp.raise_for_status()
            return resp.json()

    def invoke_prompt_stream(
        self,
        *,
        deployment: str,
        variant: str = "",
        inputs: dict[str, Any] | None = None,
        user: str | None = None,
    ) -> Generator[dict[str, Any], None, None]:
        """Invoke a prompt deployment and stream SSE events."""
        body: dict[str, Any] = {"deployment": deployment, "streaming": True}
        if variant:
            body["variant"] = variant
        if inputs is not None:
            body["inputs"] = inputs
        if user is not None:
            body["user"] = user

        with httpx.Client(timeout=self._timeout) as client:
            with client.stream("POST", self._url("/invoke"), headers=self._headers, json=body) as resp:
                yield from iter_sse(resp)

    async def ainvoke_prompt_stream(
        self,
        *,
        deployment: str,
        variant: str = "",
        inputs: dict[str, Any] | None = None,
        user: str | None = None,
    ) -> AsyncIterator[dict[str, Any]]:
        """Async: invoke a prompt deployment and stream SSE events."""
        body: dict[str, Any] = {"deployment": deployment, "streaming": True}
        if variant:
            body["variant"] = variant
        if inputs is not None:
            body["inputs"] = inputs
        if user is not None:
            body["user"] = user

        async with httpx.AsyncClient(timeout=self._timeout) as client:
            async with client.stream("POST", self._url("/invoke"), headers=self._headers, json=body) as resp:
                async for chunk in aiter_sse(resp):
                    yield chunk

    # ── Workflow ──────────────────────────────────────────────────────────────

    def invoke_workflow(
        self,
        *,
        deployment: str,
        variant: str = "",
        inputs: dict[str, Any] | None = None,
        async_mode: bool = False,
        callback_url: str | None = None,
        user: str | None = None,
    ) -> dict[str, Any]:
        """Invoke a workflow deployment (sync or async)."""
        body: dict[str, Any] = {"deployment": deployment}
        if variant:
            body["variant"] = variant
        if inputs is not None:
            body["inputs"] = inputs
        if user is not None:
            body["user"] = user
        if async_mode:
            body["async"] = {"enabled": True}
            if callback_url:
                body["async"]["callback_url"] = callback_url

        with httpx.Client(timeout=self._timeout) as client:
            resp = client.post(self._url("/workflow/invoke"), headers=self._headers, json=body)
            resp.raise_for_status()
            return resp.json()

    # ── Agent ─────────────────────────────────────────────────────────────────

    def invoke_agent(
        self,
        *,
        agent: str,
        message: str,
        thread_id: str = "",
        user: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        image_urls: list[str] | None = None,
    ) -> dict[str, Any]:
        """Send a message to an agent and return the full response."""
        body: dict[str, Any] = {"agent": agent, "message": message, "streaming": False}
        if thread_id:
            body["thread_id"] = thread_id
        if user is not None:
            body["user"] = user
        if messages is not None:
            body["messages"] = messages
        if image_urls:
            body["image_urls"] = image_urls

        with httpx.Client(timeout=self._timeout) as client:
            resp = client.post(self._url("/agent/invoke"), headers=self._headers, json=body)
            resp.raise_for_status()
            return resp.json()

    def invoke_agent_stream(
        self,
        *,
        agent: str,
        message: str,
        thread_id: str = "",
        user: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        image_urls: list[str] | None = None,
    ) -> Generator[dict[str, Any], None, None]:
        """Send a message to an agent and stream SSE events."""
        body: dict[str, Any] = {"agent": agent, "message": message, "streaming": True}
        if thread_id:
            body["thread_id"] = thread_id
        if user is not None:
            body["user"] = user
        if messages is not None:
            body["messages"] = messages
        if image_urls:
            body["image_urls"] = image_urls

        with httpx.Client(timeout=self._timeout) as client:
            with client.stream("POST", self._url("/agent/invoke"), headers=self._headers, json=body) as resp:
                yield from iter_sse(resp)

    async def ainvoke_agent_stream(
        self,
        *,
        agent: str,
        message: str,
        thread_id: str = "",
        user: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        image_urls: list[str] | None = None,
    ) -> AsyncIterator[dict[str, Any]]:
        """Async: send a message to an agent and stream SSE events."""
        body: dict[str, Any] = {"agent": agent, "message": message, "streaming": True}
        if thread_id:
            body["thread_id"] = thread_id
        if user is not None:
            body["user"] = user
        if messages is not None:
            body["messages"] = messages
        if image_urls:
            body["image_urls"] = image_urls

        async with httpx.AsyncClient(timeout=self._timeout) as client:
            async with client.stream("POST", self._url("/agent/invoke"), headers=self._headers, json=body) as resp:
                async for chunk in aiter_sse(resp):
                    yield chunk
