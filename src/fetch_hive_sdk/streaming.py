"""
streaming.py

Lightweight Server-Sent Events (SSE) parser for streaming Fetch Hive responses.

Provides both synchronous and asynchronous generators.

Sync example::

    import httpx
    from fetch_hive_sdk.streaming import iter_sse

    with httpx.stream("POST", url, headers=headers, json=body) as response:
        for chunk in iter_sse(response):
            if chunk.get("type") == "delta":
                print(chunk.get("content", ""), end="", flush=True)

Async example::

    import httpx
    from fetch_hive_sdk.streaming import aiter_sse

    async with httpx.AsyncClient() as client:
        async with client.stream("POST", url, headers=headers, json=body) as response:
            async for chunk in aiter_sse(response):
                if chunk.get("type") == "delta":
                    print(chunk.get("content", ""), end="", flush=True)
"""

from __future__ import annotations

import json
from typing import Any, AsyncIterator, Generator, Iterator

import httpx


def _parse_line(line: str) -> dict[str, Any] | None:
    """Parse a single SSE data line. Returns None for non-data lines or [DONE]."""
    if not line.startswith("data: "):
        return None
    payload = line[6:]
    if payload.strip() == "[DONE]":
        return None
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        return None


def iter_sse(response: httpx.Response) -> Generator[dict[str, Any], None, None]:
    """
    Synchronous generator that yields parsed SSE events from an httpx streaming
    response.

    Stops at ``data: [DONE]``.
    """
    response.raise_for_status()
    buf = ""
    for chunk in response.iter_text():
        buf += chunk
        while "\n" in buf:
            line, buf = buf.split("\n", 1)
            line = line.rstrip("\r")
            event = _parse_line(line)
            if event is None and line.strip() == "data: [DONE]":
                return
            if event is not None:
                yield event


async def aiter_sse(response: httpx.Response) -> AsyncIterator[dict[str, Any]]:
    """
    Asynchronous generator that yields parsed SSE events from an httpx streaming
    response.

    Stops at ``data: [DONE]``.
    """
    response.raise_for_status()
    buf = ""
    async for chunk in response.aiter_text():
        buf += chunk
        while "\n" in buf:
            line, buf = buf.split("\n", 1)
            line = line.rstrip("\r")
            if line.strip() == "data: [DONE]":
                return
            event = _parse_line(line)
            if event is not None:
                yield event
