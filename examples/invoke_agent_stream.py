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
    if event_type == "response":
        print(chunk.get("response", ""), end="", flush=True)
    elif event_type == "tool":
        print(f"\n[Calling tool: {chunk.get('tool')}]")
    elif event_type == "usage":
        print("\n\n[Done]")
        if chunk.get("usage"):
            print("Usage:", chunk["usage"])
