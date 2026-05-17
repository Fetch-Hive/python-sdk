# PlanLimitsObject

Per-plan caps (nil means unlimited). Read from account.effective_plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_workflow_steps** | **int** | (value may be null) | [optional] 
**max_iteration_limit** | **int** | (value may be null) | [optional] 
**max_log_range_days** | **int** | (value may be null) | [optional] 
**workspace_limit** | **int** | Max active workspaces. nil &#x3D; unlimited. (value may be null) | [optional] 
**workspace_count** | **int** | Current count of active workspaces on the account. | [optional] 
**workspace_limit_reached** | **bool** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.plan_limits_object import PlanLimitsObject

# TODO update the JSON string below
json = "{}"
# create an instance of PlanLimitsObject from a JSON string
plan_limits_object_instance = PlanLimitsObject.from_json(json)
# print the JSON string representation of the object
print(PlanLimitsObject.to_json())

# convert the object into a dict
plan_limits_object_dict = plan_limits_object_instance.to_dict()
# create an instance of PlanLimitsObject from a dict
plan_limits_object_from_dict = PlanLimitsObject.from_dict(plan_limits_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


