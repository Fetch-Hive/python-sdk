# fetch-hive-sdk

Official Python SDK for [Fetch Hive](https://fetchhive.com) — invoke AI prompts, workflows, and agents from your application.

[![PyPI version](https://badge.fury.io/py/fetch-hive-sdk.svg)](https://pypi.org/project/fetch-hive-sdk/)

## Installation

```bash
pip install fetch-hive-sdk
```

## Quick start

```python
from fetch_hive_sdk import FetchHive

client = FetchHive(api_key="fhk_...")
# or: client = FetchHive()  # reads FETCH_HIVE_API_KEY env var
```

Get your API key from the [Fetch Hive dashboard](https://app.fetchhive.com).

## Invoke a prompt

```python
result = client.invoke_prompt(
    deployment="my-prompt",
    inputs={"name": "Alice", "topic": "machine learning"},
)
print(result["response"])
```

## Invoke a prompt (streaming)

```python
for chunk in client.invoke_prompt_stream(
    deployment="my-prompt",
    inputs={"name": "Alice"},
):
    if chunk.get("type") == "delta":
        print(chunk.get("content", ""), end="", flush=True)
```

## Invoke a workflow

```python
run = client.invoke_workflow(
    deployment="my-workflow",
    inputs={"customer_id": "42"},
)
print(run["status"], run.get("output"))
```

## Async workflow

```python
run = client.invoke_workflow(
    deployment="my-workflow",
    inputs={"customer_id": "42"},
    async_mode=True,
    callback_url="https://example.com/webhook",
)
print("Queued:", run["run_id"])
```

## Invoke an agent (streaming)

```python
for chunk in client.invoke_agent_stream(
    agent="my-agent",
    message="What is the weather in London?",
    thread_id="session-abc123",  # optional — persist conversation history
):
    if chunk.get("type") == "delta":
        print(chunk.get("content", ""), end="", flush=True)
    elif chunk.get("type") == "tool_start":
        print(f"\n[Calling tool: {chunk.get('tool_name')}]")
```

## Async streaming

```python
import asyncio

async def main():
    async for chunk in client.ainvoke_agent_stream(
        agent="my-agent",
        message="Hello",
    ):
        if chunk.get("type") == "delta":
            print(chunk.get("content", ""), end="", flush=True)

asyncio.run(main())
```

## Multimodal (image) inputs

```python
result = client.invoke_agent(
    agent="vision-agent",
    message="Describe this image",
    image_urls=["https://example.com/photo.jpg"],
)
```

## Authentication

Pass the API key to the constructor or set the `FETCH_HIVE_API_KEY` environment variable:

```bash
export FETCH_HIVE_API_KEY=fhk_...
```

## Version

0.1.0

## License

MIT — see [LICENSE](LICENSE).
