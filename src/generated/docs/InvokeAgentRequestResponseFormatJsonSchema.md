# InvokeAgentRequestResponseFormatJsonSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**strict** | **bool** |  | [optional] 
**var_schema** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_agent_request_response_format_json_schema import InvokeAgentRequestResponseFormatJsonSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeAgentRequestResponseFormatJsonSchema from a JSON string
invoke_agent_request_response_format_json_schema_instance = InvokeAgentRequestResponseFormatJsonSchema.from_json(json)
# print the JSON string representation of the object
print(InvokeAgentRequestResponseFormatJsonSchema.to_json())

# convert the object into a dict
invoke_agent_request_response_format_json_schema_dict = invoke_agent_request_response_format_json_schema_instance.to_dict()
# create an instance of InvokeAgentRequestResponseFormatJsonSchema from a dict
invoke_agent_request_response_format_json_schema_from_dict = InvokeAgentRequestResponseFormatJsonSchema.from_dict(invoke_agent_request_response_format_json_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


