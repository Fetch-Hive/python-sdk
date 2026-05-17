"""
Example: Invoke an agent with streaming.

Run:
    FETCH_HIVE_API_KEY=fhk_... python examples/invoke_agent_stream.py
"""
from fetch_hive_sdk import FetchHive

client = FetchHive()

print("Streaming agent response:\n")

for chunk in client.invoke_agent_stream(
    agent="my-agent",
    message="Tell me a short story",
):
    event_type = chunk.get("type")
    if event_type == "delta":
        print(chunk.get("content", ""), end="", flush=True)
    elif event_type == "tool_start":
        print(f"\n[Calling tool: {chunk.get('tool_name')}]")
    elif event_type == "done":
        print("\n\n[Done]")
        if chunk.get("usage"):
            print("Usage:", chunk["usage"])
