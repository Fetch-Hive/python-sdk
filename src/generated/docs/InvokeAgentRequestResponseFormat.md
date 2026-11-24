# InvokeAgentRequestResponseFormat

Per-call output format. Omit it, or send `{ \"type\": \"text\" }`, for text. `{ \"type\": \"json_schema\", \"json_schema\": { \"name\", \"schema\", \"strict\" } }` returns JSON that matches the schema. The schema root must be an object and the document must be at most 100000 bytes. The schema applies to the final answer; tool calls still run. A model that does not support JSON Schema returns `422 json_schema_unsupported`. An invalid schema returns `422 json_schema_invalid`. If the answer still does not match after one repair, the call returns `422 json_schema_output_invalid`. `is_json_schema_response_format` plus `json_schema` is the older shape. `response_format` wins when both are present. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**json_schema** | [**InvokeAgentRequestResponseFormatJsonSchema**](InvokeAgentRequestResponseFormatJsonSchema.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_agent_request_response_format import InvokeAgentRequestResponseFormat

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeAgentRequestResponseFormat from a JSON string
invoke_agent_request_response_format_instance = InvokeAgentRequestResponseFormat.from_json(json)
# print the JSON string representation of the object
print(InvokeAgentRequestResponseFormat.to_json())

# convert the object into a dict
invoke_agent_request_response_format_dict = invoke_agent_request_response_format_instance.to_dict()
# create an instance of InvokeAgentRequestResponseFormat from a dict
invoke_agent_request_response_format_from_dict = InvokeAgentRequestResponseFormat.from_dict(invoke_agent_request_response_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


