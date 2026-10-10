# DeniedToolCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** |  | 
**approval_id** | **str** |  | [optional] 
**reason** | **str** |  | 

## Example

```python
from fetch_hive_sdk.models.denied_tool_call import DeniedToolCall

# TODO update the JSON string below
json = "{}"
# create an instance of DeniedToolCall from a JSON string
denied_tool_call_instance = DeniedToolCall.from_json(json)
# print the JSON string representation of the object
print(DeniedToolCall.to_json())

# convert the object into a dict
denied_tool_call_dict = denied_tool_call_instance.to_dict()
# create an instance of DeniedToolCall from a dict
denied_tool_call_from_dict = DeniedToolCall.from_dict(denied_tool_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


