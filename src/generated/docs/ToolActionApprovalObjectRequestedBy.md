# ToolActionApprovalObjectRequestedBy

(value may be null)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | (value may be null) | [optional] 
**name** | **str** | (value may be null) | [optional] 
**workflow_name** | **str** | (value may be null) | [optional] 
**agent_name** | **str** | (value may be null) | [optional] 

## Example

```python
from fetch_hive_sdk.models.tool_action_approval_object_requested_by import ToolActionApprovalObjectRequestedBy

# TODO update the JSON string below
json = "{}"
# create an instance of ToolActionApprovalObjectRequestedBy from a JSON string
tool_action_approval_object_requested_by_instance = ToolActionApprovalObjectRequestedBy.from_json(json)
# print the JSON string representation of the object
print(ToolActionApprovalObjectRequestedBy.to_json())

# convert the object into a dict
tool_action_approval_object_requested_by_dict = tool_action_approval_object_requested_by_instance.to_dict()
# create an instance of ToolActionApprovalObjectRequestedBy from a dict
tool_action_approval_object_requested_by_from_dict = ToolActionApprovalObjectRequestedBy.from_dict(tool_action_approval_object_requested_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


