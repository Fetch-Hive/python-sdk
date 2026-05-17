# UserMembershipObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**role** | **str** |  | 
**is_owner** | **bool** |  | 
**is_admin** | **bool** |  | 
**is_member** | **bool** |  | 

## Example

```python
from fetch_hive_sdk.models.user_membership_object import UserMembershipObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserMembershipObject from a JSON string
user_membership_object_instance = UserMembershipObject.from_json(json)
# print the JSON string representation of the object
print(UserMembershipObject.to_json())

# convert the object into a dict
user_membership_object_dict = user_membership_object_instance.to_dict()
# create an instance of UserMembershipObject from a dict
user_membership_object_from_dict = UserMembershipObject.from_dict(user_membership_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


