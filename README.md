# fetch-hive-sdk

Official Python SDK for [Fetch Hive](https://fetchhive.com).

> This repository is **bot-managed**. Source is generated and assembled by
> [Fetch-Hive/sdk-generator](https://github.com/Fetch-Hive/sdk-generator).
> Do not open pull requests here — open them in the generator repo.

## Installation

```bash
pip install fetch-hive-sdk
```

## Quick start

```python
from fetch_hive_sdk import FetchHive

client = FetchHive(api_key="fhk_...")
# or: client = FetchHive()  # reads FETCH_HIVE_API_KEY env var

# Invoke a prompt
result = client.invoke_prompt(deployment="my-prompt")
print(result["response"])

# Stream an agent response
for chunk in client.invoke_agent_stream(agent="my-agent", message="Hello"):
    if chunk.get("type") == "delta":
        print(chunk.get("content", ""), end="", flush=True)
```

See the [sdk-generator README](https://github.com/Fetch-Hive/sdk-generator) for full documentation.

## License

MIT
