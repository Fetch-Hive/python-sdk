# AccountObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**date_format** | **str** |  | 
**timezone** | **str** |  | 
**subscribed** | **bool** |  | 
**subscription_status** | **str** | (value may be null) | [optional] 
**onboarded** | **bool** |  | 
**onboarded_at** | **datetime** | (value may be null) | [optional] 
**marketing_attribution** | **str** | (value may be null) | [optional] 
**usage_purpose** | **str** | (value may be null) | [optional] 
**role** | **str** | (value may be null) | [optional] 
**feedback_message** | **str** | (value may be null) | [optional] 
**marked_deletion_at** | **datetime** | (value may be null) | [optional] 
**api_key** | **str** | (value may be null) | [optional] 
**account_steps_completed** | **int** |  | 
**account_step_percentage** | **float** |  | 
**is_app_access_enabled** | **bool** |  | 
**is_app_access_disabled** | **bool** |  | 
**is_trial_plan_enabled** | **bool** |  | 
**is_trial_plan_disabled** | **bool** |  | 
**has_capped_members** | **bool** |  | 
**has_prompts** | **bool** |  | 
**has_members** | **bool** |  | 
**has_submitted_feedback** | **bool** |  | 
**has_discord_username** | **bool** |  | 
**is_marked_for_deletion** | **bool** |  | 
**active_subscription** | [**ActiveSubscriptionObject**](ActiveSubscriptionObject.md) | (value may be null) | [optional] 
**plan_limits** | [**PlanLimitsObject**](PlanLimitsObject.md) |  | [optional] 
**storage** | [**StorageObject**](StorageObject.md) |  | [optional] 
**welcome_bonus** | [**AccountObjectWelcomeBonus**](AccountObjectWelcomeBonus.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.account_object import AccountObject

# TODO update the JSON string below
json = "{}"
# create an instance of AccountObject from a JSON string
account_object_instance = AccountObject.from_json(json)
# print the JSON string representation of the object
print(AccountObject.to_json())

# convert the object into a dict
account_object_dict = account_object_instance.to_dict()
# create an instance of AccountObject from a dict
account_object_from_dict = AccountObject.from_dict(account_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


