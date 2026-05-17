"""
fetch_hive_sdk — Official Python SDK for the Fetch Hive API.

Quick start::

    from fetch_hive_sdk import FetchHive

    client = FetchHive(api_key="fhk_...")

    # Non-streaming
    result = client.invoke_agent(agent="my-agent", message="Hello")
    print(result["response"])

    # Streaming
    for chunk in client.invoke_agent_stream(agent="my-agent", message="Hello"):
        if chunk.get("type") == "delta":
            print(chunk.get("content", ""), end="", flush=True)
"""

from .client import FetchHive
from .streaming import aiter_sse, iter_sse

__all__ = ["FetchHive", "iter_sse", "aiter_sse"]
