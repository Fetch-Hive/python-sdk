# ActiveSubscriptionObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**total_credits_used** | **float** |  | 
**credit_cap** | **float** |  | 
**topup_credit_balance** | **int** | Persistent top-up tasks that never expire or reset at billing cycle. | [optional] 
**total_available_credits** | **int** | Plan remaining + top-up balance. | [optional] 
**credits_used_percentage** | **float** |  | 
**trial_days_remaining** | **int** | (value may be null) | [optional] 
**next_rebill_at** | **datetime** | (value may be null) | [optional] 
**pending_cancelled_at** | **datetime** | (value may be null) | [optional] 
**trial_end_at** | **datetime** | (value may be null) | [optional] 
**status** | **str** |  | 
**subscription_type** | **str** |  | 
**has_active_trial** | **bool** |  | 
**has_pending_cancellation** | **bool** |  | 
**has_downgrade_scheduled** | **bool** |  | 
**downgrade_scheduled_at** | **datetime** | (value may be null) | [optional] 
**plan** | [**PlanObject**](PlanObject.md) |  | [optional] 
**downgrade_plan** | [**PlanObject**](PlanObject.md) | (value may be null) | [optional] 
**hosted_llm_credits** | [**ActiveSubscriptionObjectHostedLlmCredits**](ActiveSubscriptionObjectHostedLlmCredits.md) |  | 

## Example

```python
from fetch_hive_sdk.models.active_subscription_object import ActiveSubscriptionObject

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveSubscriptionObject from a JSON string
active_subscription_object_instance = ActiveSubscriptionObject.from_json(json)
# print the JSON string representation of the object
print(ActiveSubscriptionObject.to_json())

# convert the object into a dict
active_subscription_object_dict = active_subscription_object_instance.to_dict()
# create an instance of ActiveSubscriptionObject from a dict
active_subscription_object_from_dict = ActiveSubscriptionObject.from_dict(active_subscription_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


