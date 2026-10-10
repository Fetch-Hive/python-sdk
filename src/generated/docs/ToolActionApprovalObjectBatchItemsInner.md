# ToolActionApprovalObjectBatchItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**summary** | **str** |  | 

## Example

```python
from fetch_hive_sdk.models.tool_action_approval_object_batch_items_inner import ToolActionApprovalObjectBatchItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ToolActionApprovalObjectBatchItemsInner from a JSON string
tool_action_approval_object_batch_items_inner_instance = ToolActionApprovalObjectBatchItemsInner.from_json(json)
# print the JSON string representation of the object
print(ToolActionApprovalObjectBatchItemsInner.to_json())

# convert the object into a dict
tool_action_approval_object_batch_items_inner_dict = tool_action_approval_object_batch_items_inner_instance.to_dict()
# create an instance of ToolActionApprovalObjectBatchItemsInner from a dict
tool_action_approval_object_batch_items_inner_from_dict = ToolActionApprovalObjectBatchItemsInner.from_dict(tool_action_approval_object_batch_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


