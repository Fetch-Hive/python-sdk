# PendingToolApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_id** | **UUID** |  | 
**tool_name** | **str** |  | 
**summary** | **str** |  | 
**arguments** | **Dict[str, object]** |  | [optional] 
**expires_at** | **datetime** | (value may be null) | [optional] 
**review_url** | **str** | Dashboard link for this approval. This is not the email token.  | [optional] 

## Example

```python
from fetch_hive_sdk.models.pending_tool_approval import PendingToolApproval

# TODO update the JSON string below
json = "{}"
# create an instance of PendingToolApproval from a JSON string
pending_tool_approval_instance = PendingToolApproval.from_json(json)
# print the JSON string representation of the object
print(PendingToolApproval.to_json())

# convert the object into a dict
pending_tool_approval_dict = pending_tool_approval_instance.to_dict()
# create an instance of PendingToolApproval from a dict
pending_tool_approval_from_dict = PendingToolApproval.from_dict(pending_tool_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


