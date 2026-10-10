# ToolActionApprovalObjectCapabilities

(value may be null)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_always_allow** | **bool** |  | [optional] 
**can_run_decision** | **bool** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.tool_action_approval_object_capabilities import ToolActionApprovalObjectCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ToolActionApprovalObjectCapabilities from a JSON string
tool_action_approval_object_capabilities_instance = ToolActionApprovalObjectCapabilities.from_json(json)
# print the JSON string representation of the object
print(ToolActionApprovalObjectCapabilities.to_json())

# convert the object into a dict
tool_action_approval_object_capabilities_dict = tool_action_approval_object_capabilities_instance.to_dict()
# create an instance of ToolActionApprovalObjectCapabilities from a dict
tool_action_approval_object_capabilities_from_dict = ToolActionApprovalObjectCapabilities.from_dict(tool_action_approval_object_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


