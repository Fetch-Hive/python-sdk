# SseChunk

A single event in a Server-Sent Events stream. The type field is a runtime discriminator. Known values: delta, done, tool_start, tool_end, error. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Event type discriminator. | [optional] 
**content** | **str** | Text delta content (present for type \&quot;delta\&quot;). | [optional] 
**request_id** | **str** | Present on the final \&quot;done\&quot; event. | [optional] 
**model** | **str** | Present on the final \&quot;done\&quot; event. | [optional] 
**tool_name** | **str** | Tool name (present for \&quot;tool_start\&quot; / \&quot;tool_end\&quot;). | [optional] 
**tool_input** | **str** | Serialised JSON tool input (present for \&quot;tool_start\&quot;). | [optional] 
**observation** | **str** | Serialised JSON tool result (present for \&quot;tool_end\&quot;). | [optional] 
**error** | **str** | Error message (present for \&quot;error\&quot; events). | [optional] 
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


