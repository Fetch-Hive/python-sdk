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
    metadata={},
)
print(result["response"])
```

## Invoke a prompt (streaming)

```python
for chunk in client.invoke_prompt_stream(
    deployment="my-prompt",
    inputs={"name": "Alice"},
):
    if chunk.get("type") == "response":
        print(chunk.get("response", ""), end="", flush=True)
    elif chunk.get("type") == "usage":
        print("\nUsage:", chunk["usage"])
```

## Invoke a workflow

```python
run = client.invoke_workflow(
    deployment="my-workflow",
    inputs={"customer_id": "42"},
    metadata={},
)
print(run["status"], run.get("output"))
```

## Invoke a workflow (async)

```python
run = client.invoke_workflow(
    deployment="my-workflow",
    inputs={"customer_id": "42"},
    async_mode=True,
    callback_url="https://example.com/webhook",
)
print("Queued:", run["run_id"])
```

## Invoke an agent

```python
reply = client.invoke_agent(
    agent="my-agent",
    message="What is the weather in London?",
    metadata={},
)
print(reply["response"])
```

## Metadata

Pass optional `metadata` on prompt, workflow, or agent invokes to attach flat audit fields for log display and filtering. Metadata values must be strings, numbers, booleans, or `None`.

## Invoke an agent (streaming)

```python
for chunk in client.invoke_agent_stream(
    agent="my-agent",
    message="What is the weather in London?",
    thread_id="session-abc123",  # optional — persist conversation history
):
    if chunk.get("type") == "response":
        print(chunk.get("response", ""), end="", flush=True)
    elif chunk.get("type") == "tool":
        print(f"\n[Calling tool: {chunk.get('tool')}]")
    elif chunk.get("type") == "usage":
        print("\nUsage:", chunk["usage"])
```

## Multimodal (image) inputs

```python
result = client.invoke_agent(
    agent="vision-agent",
    message="Describe this image",
    image_urls=["https://example.com/photo.jpg"],
)
print(result["response"])
```

## Async streaming

```python
import asyncio

async def main():
    async for chunk in client.ainvoke_agent_stream(
        agent="my-agent",
        message="Hello",
        thread_id="session-abc123",
    ):
        if chunk.get("type") == "response":
            print(chunk.get("response", ""), end="", flush=True)
        elif chunk.get("type") == "tool":
            print(f"\n[Calling tool: {chunk.get('tool')}]")
        elif chunk.get("type") == "usage":
            print("\nUsage:", chunk["usage"])

asyncio.run(main())
```

## Authentication

Pass the API key to the constructor or set the environment variable:

```bash
export FETCH_HIVE_API_KEY=fhk_...
```

```python
client = FetchHive()  # picks up FETCH_HIVE_API_KEY automatically
```

## Configuration

| Option | Default | Description |
|---|---|---|
| `api_key` | `FETCH_HIVE_API_KEY` env var | Bearer token from the Fetch Hive dashboard |
| `base_url` | `https://api.fetchhive.com/v1` | Override the API base URL |
| `timeout` | `120` | Request timeout in seconds |

## Links

- [Fetch Hive dashboard](https://app.fetchhive.com)
- [API documentation](https://docs.fetchhive.com)
- [GitHub](https://github.com/Fetch-Hive/python-sdk)

## Version

0.2.7

## License

MIT — see [LICENSE](LICENSE).
