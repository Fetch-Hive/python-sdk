# ActiveSubscriptionObjectHostedLlmCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_usd** | **float** |  | 
**total_purchased_usd** | **float** |  | 
**total_used_usd** | **float** |  | 
**enabled** | **bool** |  | 

## Example

```python
from fetch_hive_sdk.models.active_subscription_object_hosted_llm_credits import ActiveSubscriptionObjectHostedLlmCredits

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveSubscriptionObjectHostedLlmCredits from a JSON string
active_subscription_object_hosted_llm_credits_instance = ActiveSubscriptionObjectHostedLlmCredits.from_json(json)
# print the JSON string representation of the object
print(ActiveSubscriptionObjectHostedLlmCredits.to_json())

# convert the object into a dict
active_subscription_object_hosted_llm_credits_dict = active_subscription_object_hosted_llm_credits_instance.to_dict()
# create an instance of ActiveSubscriptionObjectHostedLlmCredits from a dict
active_subscription_object_hosted_llm_credits_from_dict = ActiveSubscriptionObjectHostedLlmCredits.from_dict(active_subscription_object_hosted_llm_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


