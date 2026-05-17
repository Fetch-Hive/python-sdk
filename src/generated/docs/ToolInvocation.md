# ToolInvocation

A single tool call made by the agent during execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | Name of the tool that was called. | [optional] 
**tool_input** | **str** | Arguments passed to the tool. Contains serialised JSON; parse client-side as needed.  | [optional] 
**observation** | **str** | The tool&#39;s return value. Contains serialised JSON; parse client-side as needed.  | [optional] 

## Example

```python
from fetch_hive_sdk.models.tool_invocation import ToolInvocation

# TODO update the JSON string below
json = "{}"
# create an instance of ToolInvocation from a JSON string
tool_invocation_instance = ToolInvocation.from_json(json)
# print the JSON string representation of the object
print(ToolInvocation.to_json())

# convert the object into a dict
tool_invocation_dict = tool_invocation_instance.to_dict()
# create an instance of ToolInvocation from a dict
tool_invocation_from_dict = ToolInvocation.from_dict(tool_invocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


