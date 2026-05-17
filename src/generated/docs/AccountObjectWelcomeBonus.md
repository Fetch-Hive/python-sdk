# AccountObjectWelcomeBonus

One-time hosted LLM credit bonus. $2 for Developer (free) plan, $5 for any paid plan. Granted on first subscription activation. (value may be null)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_usd** | **float** | (value may be null) | [optional] 
**granted** | **bool** |  | 
**granted_at** | **datetime** | (value may be null) | [optional] 

## Example

```python
from fetch_hive_sdk.models.account_object_welcome_bonus import AccountObjectWelcomeBonus

# TODO update the JSON string below
json = "{}"
# create an instance of AccountObjectWelcomeBonus from a JSON string
account_object_welcome_bonus_instance = AccountObjectWelcomeBonus.from_json(json)
# print the JSON string representation of the object
print(AccountObjectWelcomeBonus.to_json())

# convert the object into a dict
account_object_welcome_bonus_dict = account_object_welcome_bonus_instance.to_dict()
# create an instance of AccountObjectWelcomeBonus from a dict
account_object_welcome_bonus_from_dict = AccountObjectWelcomeBonus.from_dict(account_object_welcome_bonus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


