# SseChunk

A single event in a Server-Sent Events stream. The `type` field is a runtime discriminator. Known values:   - `reasoning` — a reasoning / thinking chunk (prompt and agent streams)   - `response`  — a text chunk (prompt and agent streams)   - `tool`      — a tool invocation result (agent stream only)   - `usage`     — final token usage event; signals end of meaningful stream content   - `summary`   — auto-summarization event emitted before reasoning when a thread                   history was compressed (agent stream only)   - `error`     — server-side error during streaming  The stream is terminated by `data: [DONE]`, which is handled by the SSE parser and never surfaced as a chunk. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Event type discriminator. | [optional] 
**response** | **str** | Text content of the chunk. Present for &#x60;reasoning&#x60; and &#x60;response&#x60; event types.  | [optional] 
**request_id** | **str** | Unique request identifier. Present on most events; always present on &#x60;usage&#x60;. | [optional] 
**model** | **str** | Model identifier. Present on &#x60;response&#x60; and &#x60;reasoning&#x60; events (prompt stream). | [optional] 
**done** | **bool** | Per-chunk boolean flag on &#x60;response&#x60; and &#x60;reasoning&#x60; events (agent stream). Not a terminal event type — use the &#x60;usage&#x60; event to detect end of stream.  | [optional] 
**tool_id** | **str** | Unique tool invocation identifier. Present for &#x60;tool&#x60; events. | [optional] 
**tool** | **str** | Tool name. Present for &#x60;tool&#x60; events (e.g. \&quot;google_search\&quot;). | [optional] 
**tool_type** | **str** | Internal tool type identifier. Present for &#x60;tool&#x60; events. | [optional] 
**tool_input** | **Dict[str, object]** | Parsed tool input arguments. Present for &#x60;tool&#x60; events. | [optional] 
**observation** | **str** | Serialised JSON tool result. Present for &#x60;tool&#x60; events. | [optional] 
**stop_reason** | **str** | Reason the stream ended. Present on &#x60;usage&#x60; events (e.g. \&quot;completed\&quot;). | [optional] 
**summary_text** | **str** | Compressed summary of the prior conversation. Present for &#x60;summary&#x60; events. | [optional] 
**original_token_count** | **int** | Token count before summarization. Present for &#x60;summary&#x60; events. | [optional] 
**context_limit** | **int** | Model context window size. Present for &#x60;summary&#x60; events. | [optional] 
**provider** | **str** | LLM provider used for summarization. Present for &#x60;summary&#x60; events. | [optional] 
**error** | **str** | Error message. Present for &#x60;error&#x60; events. | [optional] 
**usage** | [**TokenUsage**](TokenUsage.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.sse_chunk import SseChunk

# TODO update the JSON string below
json = "{}"
# create an instance of SseChunk from a JSON string
sse_chunk_instance = SseChunk.from_json(json)
# print the JSON string representation of the object
print(SseChunk.to_json())

# convert the object into a dict
sse_chunk_dict = sse_chunk_instance.to_dict()
# create an instance of SseChunk from a dict
sse_chunk_from_dict = SseChunk.from_dict(sse_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


