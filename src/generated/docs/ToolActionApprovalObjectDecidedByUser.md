# ToolActionApprovalObjectDecidedByUser

Admin approval only. The public approval omits this field. (value may be null)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**email** | **str** | (value may be null) | [optional] 
**full_name** | **str** | (value may be null) | [optional] 
**username** | **str** | (value may be null) | [optional] 
**name_initial** | **str** | (value may be null) | [optional] 

## Example

```python
from fetch_hive_sdk.models.tool_action_approval_object_decided_by_user import ToolActionApprovalObjectDecidedByUser

# TODO update the JSON string below
json = "{}"
# create an instance of ToolActionApprovalObjectDecidedByUser from a JSON string
tool_action_approval_object_decided_by_user_instance = ToolActionApprovalObjectDecidedByUser.from_json(json)
# print the JSON string representation of the object
print(ToolActionApprovalObjectDecidedByUser.to_json())

# convert the object into a dict
tool_action_approval_object_decided_by_user_dict = tool_action_approval_object_decided_by_user_instance.to_dict()
# create an instance of ToolActionApprovalObjectDecidedByUser from a dict
tool_action_approval_object_decided_by_user_from_dict = ToolActionApprovalObjectDecidedByUser.from_dict(tool_action_approval_object_decided_by_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


