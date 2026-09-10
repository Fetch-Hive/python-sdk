# PendingDelegation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**kind** | **str** |  | 
**target** | **Dict[str, object]** |  | [optional] 
**expected_by** | **datetime** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.pending_delegation import PendingDelegation

# TODO update the JSON string below
json = "{}"
# create an instance of PendingDelegation from a JSON string
pending_delegation_instance = PendingDelegation.from_json(json)
# print the JSON string representation of the object
print(PendingDelegation.to_json())

# convert the object into a dict
pending_delegation_dict = pending_delegation_instance.to_dict()
# create an instance of PendingDelegation from a dict
pending_delegation_from_dict = PendingDelegation.from_dict(pending_delegation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


