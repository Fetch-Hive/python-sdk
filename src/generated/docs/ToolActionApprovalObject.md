# ToolActionApprovalObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**status** | **str** |  | 
**decision** | **str** | (value may be null) | [optional] 
**summary** | **str** |  | 
**provider_type** | **str** | (value may be null) | [optional] 
**action_slug** | **str** | (value may be null) | [optional] 
**action_label** | **str** | (value may be null) | [optional] 
**confirmation** | **str** | (value may be null) | [optional] 
**approvals_required** | **int** | (value may be null) | [optional] 
**approval_votes** | [**List[ToolActionApprovalObjectApprovalVotesInner]**](ToolActionApprovalObjectApprovalVotesInner.md) | (value may be null) | [optional] 
**provider_login** | **str** | (value may be null) | [optional] 
**gateway_name** | **str** | (value may be null) | [optional] 
**token_name** | **str** | (value may be null) | [optional] 
**arguments** | **object** | (value may be null) | [optional] 
**result** | **object** | (value may be null) | [optional] 
**error** | **str** | (value may be null) | [optional] 
**risk_level** | **str** | (value may be null) | [optional] 
**requested_by_kind** | **str** | (value may be null) | [optional] 
**requested_by** | [**ToolActionApprovalObjectRequestedBy**](ToolActionApprovalObjectRequestedBy.md) |  | [optional] 
**prompt_workflow_run_id** | **UUID** | (value may be null) | [optional] 
**agent_run_id** | **UUID** | (value may be null) | [optional] 
**ephemeral_execution_id** | **str** | (value may be null) | [optional] 
**copilot_session_id** | **str** | (value may be null) | [optional] 
**integration_connection_count** | **int** | (value may be null) | [optional] 
**created_at** | **datetime** | (value may be null) | [optional] 
**expires_at** | **datetime** | (value may be null) | [optional] 
**decided_at** | **datetime** | (value may be null) | [optional] 
**decided_by** | **str** | (value may be null) | [optional] 
**decided_via** | **str** | (value may be null) | [optional] 
**decided_by_api_key_name** | **str** | (value may be null) | [optional] 
**decided_by_user** | [**ToolActionApprovalObjectDecidedByUser**](ToolActionApprovalObjectDecidedByUser.md) |  | [optional] 
**auto_allowed_by** | **str** | (value may be null) | [optional] 
**auto_allowed_source_id** | **UUID** | (value may be null) | [optional] 
**auto_allowed_source_name** | **str** | (value may be null) | [optional] 
**workspace_id** | **UUID** | (value may be null) | [optional] 
**original_arguments** | **object** | (value may be null) | [optional] 
**arguments_edited_at** | **datetime** | (value may be null) | [optional] 
**arguments_edited_by** | [**ToolActionApprovalObjectArgumentsEditedBy**](ToolActionApprovalObjectArgumentsEditedBy.md) |  | [optional] 
**changed_fields** | **List[str]** | (value may be null) | [optional] 
**resolved_policy_id** | **UUID** | (value may be null) | [optional] 
**resolved_policy_user** | [**ToolActionApprovalObjectArgumentsEditedBy**](ToolActionApprovalObjectArgumentsEditedBy.md) |  | [optional] 
**locked_rule_effect** | **str** | (value may be null) | [optional] 
**audience_role** | **str** | (value may be null) | [optional] 
**integration_authorization_id** | **UUID** | (value may be null) | [optional] 
**batch_key** | **str** | (value may be null) | [optional] 
**batch_pending_count** | **int** | (value may be null) | [optional] 
**batch_items** | [**List[ToolActionApprovalObjectBatchItemsInner]**](ToolActionApprovalObjectBatchItemsInner.md) | (value may be null) | [optional] 
**capabilities** | [**ToolActionApprovalObjectCapabilities**](ToolActionApprovalObjectCapabilities.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.tool_action_approval_object import ToolActionApprovalObject

# TODO update the JSON string below
json = "{}"
# create an instance of ToolActionApprovalObject from a JSON string
tool_action_approval_object_instance = ToolActionApprovalObject.from_json(json)
# print the JSON string representation of the object
print(ToolActionApprovalObject.to_json())

# convert the object into a dict
tool_action_approval_object_dict = tool_action_approval_object_instance.to_dict()
# create an instance of ToolActionApprovalObject from a dict
tool_action_approval_object_from_dict = ToolActionApprovalObject.from_dict(tool_action_approval_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


