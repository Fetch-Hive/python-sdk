"""
Example: Invoke a prompt deployment.

Run:
    FETCH_HIVE_API_KEY=fhk_... python examples/invoke_prompt.py
"""
from fetch_hive_sdk import FetchHive

client = FetchHive()

result = client.invoke_prompt(
    deployment="my-prompt",
    inputs={"name": "Alice", "topic": "machine learning"},
    metadata={},
)

print("Response:", result.get("response"))
print("Model:", result.get("model"))
print("Usage:", result.get("usage"))
