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
        if chunk.get("type") == "response":
            print(chunk.get("response", ""), end="", flush=True)
        elif chunk.get("type") == "tool":
            print(f"\n[Calling tool: {chunk.get('tool')}]")
        elif chunk.get("type") == "usage":
            print("\nUsage:", chunk["usage"])

Async::

    async for chunk in client.ainvoke_agent_stream(agent="my-agent", message="Hello"):
        ...
"""

from __future__ import annotations

import os
from typing import Any, AsyncIterator, Generator, Iterator

import httpx

from .streaming import aiter_sse, iter_sse

Metadata = dict[str, str | int | float | bool | None]

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
        metadata: Metadata | None = None,
    ) -> dict[str, Any]:
        """Invoke a prompt deployment and return the full response."""
        body: dict[str, Any] = {"deployment": deployment, "streaming": False}
        if variant:
            body["variant"] = variant
        if inputs is not None:
            body["inputs"] = inputs
        if user is not None:
            body["user"] = user
        if metadata is not None:
            body["metadata"] = metadata

        with httpx.Client(timeout=self._timeout) as client:
            resp = client.post(self._url("/prompt/invoke"), headers=self._headers, json=body)
            resp.raise_for_status()
            return resp.json()

    def invoke_prompt_stream(
        self,
        *,
        deployment: str,
        variant: str = "",
        inputs: dict[str, Any] | None = None,
        user: str | None = None,
        metadata: Metadata | None = None,
    ) -> Generator[dict[str, Any], None, None]:
        """Invoke a prompt deployment and stream SSE events."""
        body: dict[str, Any] = {"deployment": deployment, "streaming": True}
        if variant:
            body["variant"] = variant
        if inputs is not None:
            body["inputs"] = inputs
        if user is not None:
            body["user"] = user
        if metadata is not None:
            body["metadata"] = metadata

        with httpx.Client(timeout=self._timeout) as client:
            with client.stream("POST", self._url("/prompt/invoke"), headers=self._headers, json=body) as resp:
                yield from iter_sse(resp)

    async def ainvoke_prompt_stream(
        self,
        *,
        deployment: str,
        variant: str = "",
        inputs: dict[str, Any] | None = None,
        user: str | None = None,
        metadata: Metadata | None = None,
    ) -> AsyncIterator[dict[str, Any]]:
        """Async: invoke a prompt deployment and stream SSE events."""
        body: dict[str, Any] = {"deployment": deployment, "streaming": True}
        if variant:
            body["variant"] = variant
        if inputs is not None:
            body["inputs"] = inputs
        if user is not None:
            body["user"] = user
        if metadata is not None:
            body["metadata"] = metadata

        async with httpx.AsyncClient(timeout=self._timeout) as client:
            async with client.stream("POST", self._url("/prompt/invoke"), headers=self._headers, json=body) as resp:
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
        metadata: Metadata | None = None,
    ) -> dict[str, Any]:
        """Invoke a workflow deployment (sync or async)."""
        body: dict[str, Any] = {"deployment": deployment}
        if variant:
            body["variant"] = variant
        if inputs is not None:
            body["inputs"] = inputs
        if user is not None:
            body["user"] = user
        if metadata is not None:
            body["metadata"] = metadata
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
        metadata: Metadata | None = None,
        messages: list[dict[str, Any]] | None = None,
        image_urls: list[str] | None = None,
        attachments: list[str | dict[str, Any]] | None = None,
        known_artifact_refs: list[str] | None = None,
        artifact_refs: list[str] | None = None,
    ) -> dict[str, Any]:
        """Send a message to an agent and return the full response."""
        body: dict[str, Any] = {"agent": agent, "message": message, "streaming": False}
        if thread_id:
            body["thread_id"] = thread_id
        if user is not None:
            body["user"] = user
        if metadata is not None:
            body["metadata"] = metadata
        if messages is not None:
            body["messages"] = messages
        if attachments or image_urls:
            body["attachments"] = attachments or image_urls
        if known_artifact_refs:
            body["known_artifact_refs"] = known_artifact_refs
        if artifact_refs:
            body["artifact_refs"] = artifact_refs

        with httpx.Client(timeout=self._timeout) as client:
            resp = client.post(self._url("/agent/invoke"), headers=self._headers, json=body)
            resp.raise_for_status()
            return resp.json()

    # ── Hive Agent ────────────────────────────────────────────────────────────

    def invoke_hive_agent(
        self,
        *,
        hive_agent: str,
        objective: str,
        callback_url: str,
        sources: dict[str, Any] | None = None,
        metadata: Metadata | None = None,
    ) -> dict[str, Any]:
        """Start a Hive Agent run asynchronously. Requires a callback URL."""
        if not callback_url:
            raise ValueError("callback_url is required for Hive Agent invocation")
        body: dict[str, Any] = {
            "hive_agent": hive_agent,
            "objective": objective,
            "async": {"enabled": True, "callback_url": callback_url},
        }
        if sources is not None:
            body["sources"] = sources
        if metadata is not None:
            body["metadata"] = metadata
        return self._request("POST", "/hive-agent/invoke", body)

    # ── Public resources ──────────────────────────────────────────────────────

    def get_request(self, id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/requests/{id}")

    def list_knowledge_bases(self, workspace_id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/workspaces/{workspace_id}/knowledge_bases")

    def get_knowledge_base(self, workspace_id: str, id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/workspaces/{workspace_id}/knowledge_bases/{id}")

    def create_knowledge_base(self, workspace_id: str, knowledge_base: dict[str, Any]) -> dict[str, Any]:
        return self._request("POST", f"/public/workspaces/{workspace_id}/knowledge_bases", {"knowledge_base": knowledge_base})

    def update_knowledge_base(self, workspace_id: str, id: str, knowledge_base: dict[str, Any]) -> dict[str, Any]:
        return self._request("PATCH", f"/public/workspaces/{workspace_id}/knowledge_bases/{id}", {"knowledge_base": knowledge_base})

    def delete_knowledge_base(self, workspace_id: str, id: str) -> dict[str, Any]:
        return self._request("DELETE", f"/public/workspaces/{workspace_id}/knowledge_bases/{id}")

    def search_knowledge_base(self, workspace_id: str, id: str, **params: Any) -> dict[str, Any]:
        return self._request("POST", f"/public/workspaces/{workspace_id}/knowledge_bases/{id}/search", params)

    def list_knowledge_base_items(self, workspace_id: str, knowledge_base_id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items")

    def get_knowledge_base_item(self, workspace_id: str, knowledge_base_id: str, id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id}")

    def create_knowledge_base_item(self, workspace_id: str, knowledge_base_id: str, knowledge_base_item: dict[str, Any]) -> dict[str, Any]:
        return self._request(
            "POST",
            f"/public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items",
            {"knowledge_base_item": knowledge_base_item},
        )

    def update_knowledge_base_item(self, workspace_id: str, knowledge_base_id: str, id: str, knowledge_base_item: dict[str, Any]) -> dict[str, Any]:
        return self._request(
            "PATCH",
            f"/public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id}",
            {"knowledge_base_item": knowledge_base_item},
        )

    def delete_knowledge_base_item(self, workspace_id: str, knowledge_base_id: str, id: str) -> dict[str, Any]:
        return self._request("DELETE", f"/public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id}")

    def regenerate_knowledge_base_item(self, workspace_id: str, knowledge_base_id: str, id: str) -> dict[str, Any]:
        return self._request("POST", f"/public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id}/regenerate", {})

    def list_agents(self, workspace_id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/workspaces/{workspace_id}/agents")

    def get_agent(self, workspace_id: str, id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/workspaces/{workspace_id}/agents/{id}")

    def create_agent(self, workspace_id: str, agent: dict[str, Any]) -> dict[str, Any]:
        return self._request("POST", f"/public/workspaces/{workspace_id}/agents", {"agent": agent})

    def update_agent(self, workspace_id: str, id: str, agent: dict[str, Any]) -> dict[str, Any]:
        return self._request("PATCH", f"/public/workspaces/{workspace_id}/agents/{id}", {"agent": agent})

    def delete_agent(self, workspace_id: str, id: str) -> dict[str, Any]:
        return self._request("DELETE", f"/public/workspaces/{workspace_id}/agents/{id}")

    def get_agent_chat(self, workspace_id: str, agent_id: str, chat_id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/workspaces/{workspace_id}/agents/{agent_id}/chats/{chat_id}")

    def create_agent_chat(self, workspace_id: str, agent_id: str, chat: dict[str, Any]) -> dict[str, Any]:
        return self._request("POST", f"/public/workspaces/{workspace_id}/agents/{agent_id}/chats", {"chat": chat})

    def update_agent_chat(self, workspace_id: str, agent_id: str, chat_id: str, chat: dict[str, Any]) -> dict[str, Any]:
        return self._request("PATCH", f"/public/workspaces/{workspace_id}/agents/{agent_id}/chats/{chat_id}", {"chat": chat})

    def delete_agent_chat(self, workspace_id: str, agent_id: str, chat_id: str) -> dict[str, Any]:
        return self._request("DELETE", f"/public/workspaces/{workspace_id}/agents/{agent_id}/chats/{chat_id}")

    def clear_agent_chat_messages(self, workspace_id: str, agent_id: str, chat_id: str) -> dict[str, Any]:
        return self._request("PATCH", f"/public/workspaces/{workspace_id}/agents/{agent_id}/chats/{chat_id}/clear_messages", {})

    def list_agent_chat_messages(self, workspace_id: str, agent_id: str, chat_id: str) -> dict[str, Any]:
        return self._request("GET", f"/public/workspaces/{workspace_id}/agents/{agent_id}/chats/{chat_id}/messages")

    def _request(self, method: str, path: str, json_body: dict[str, Any] | None = None) -> dict[str, Any]:
        kwargs: dict[str, Any] = {"headers": self._headers}
        if json_body is not None:
            kwargs["json"] = json_body
        with httpx.Client(timeout=self._timeout) as client:
            resp = client.request(method, self._url(path), **kwargs)
            resp.raise_for_status()
            if not resp.content:
                return {}
            return resp.json()

    def invoke_agent_stream(
        self,
        *,
        agent: str,
        message: str,
        thread_id: str = "",
        user: str | None = None,
        metadata: Metadata | None = None,
        messages: list[dict[str, Any]] | None = None,
        image_urls: list[str] | None = None,
        attachments: list[str | dict[str, Any]] | None = None,
        known_artifact_refs: list[str] | None = None,
        artifact_refs: list[str] | None = None,
    ) -> Generator[dict[str, Any], None, None]:
        """Send a message to an agent and stream SSE events."""
        body: dict[str, Any] = {"agent": agent, "message": message, "streaming": True}
        if thread_id:
            body["thread_id"] = thread_id
        if user is not None:
            body["user"] = user
        if metadata is not None:
            body["metadata"] = metadata
        if messages is not None:
            body["messages"] = messages
        if attachments or image_urls:
            body["attachments"] = attachments or image_urls
        if known_artifact_refs:
            body["known_artifact_refs"] = known_artifact_refs
        if artifact_refs:
            body["artifact_refs"] = artifact_refs

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
        metadata: Metadata | None = None,
        messages: list[dict[str, Any]] | None = None,
        image_urls: list[str] | None = None,
        attachments: list[str | dict[str, Any]] | None = None,
        known_artifact_refs: list[str] | None = None,
        artifact_refs: list[str] | None = None,
    ) -> AsyncIterator[dict[str, Any]]:
        """Async: send a message to an agent and stream SSE events."""
        body: dict[str, Any] = {"agent": agent, "message": message, "streaming": True}
        if thread_id:
            body["thread_id"] = thread_id
        if user is not None:
            body["user"] = user
        if metadata is not None:
            body["metadata"] = metadata
        if messages is not None:
            body["messages"] = messages
        if attachments or image_urls:
            body["attachments"] = attachments or image_urls
        if known_artifact_refs:
            body["known_artifact_refs"] = known_artifact_refs
        if artifact_refs:
            body["artifact_refs"] = artifact_refs

        async with httpx.AsyncClient(timeout=self._timeout) as client:
            async with client.stream("POST", self._url("/agent/invoke"), headers=self._headers, json=body) as resp:
                async for chunk in aiter_sse(resp):
                    yield chunk
