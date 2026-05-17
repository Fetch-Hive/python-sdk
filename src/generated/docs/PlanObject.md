# PlanObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** | (value may be null) | [optional] 
**amount** | **float** | (value may be null) | [optional] 
**interval** | **str** | (value may be null) | [optional] 
**credit_cap** | **int** | (value may be null) | [optional] 
**concurrency_cap** | **int** | (value may be null) | [optional] 
**plan_type** | **str** | (value may be null) | [optional] 
**is_developer** | **bool** | (value may be null) | [optional] 
**is_growth** | **bool** | (value may be null) | [optional] 
**is_pro** | **bool** | (value may be null) | [optional] 
**is_enterprise** | **bool** | (value may be null) | [optional] 
**is_contact_sales** | **bool** | (value may be null) | [optional] 
**stripe_plan_id** | **str** | (value may be null) | [optional] 
**max_workflow_steps** | **int** | (value may be null) | [optional] 
**max_iteration_limit** | **int** | (value may be null) | [optional] 
**max_log_range_days** | **int** | (value may be null) | [optional] 
**storage_limit_bytes** | **int** | Storage limit in bytes. nil &#x3D; custom/unlimited. (value may be null) | [optional] 
**rate_limit_per_day** | **int** | (value may be null) | [optional] 
**plan_features** | **object** | (value may be null) | [optional] 

## Example

```python
from fetch_hive_sdk.models.plan_object import PlanObject

# TODO update the JSON string below
json = "{}"
# create an instance of PlanObject from a JSON string
plan_object_instance = PlanObject.from_json(json)
# print the JSON string representation of the object
print(PlanObject.to_json())

# convert the object into a dict
plan_object_dict = plan_object_instance.to_dict()
# create an instance of PlanObject from a dict
plan_object_from_dict = PlanObject.from_dict(plan_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


