# UserObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**first_name** | **str** | (value may be null) | [optional] 
**last_name** | **str** | (value may be null) | [optional] 
**full_name** | **str** | (value may be null) | [optional] 
**name_initial** | **str** | (value may be null) | [optional] 
**email** | **str** |  | 
**username** | **str** | (value may be null) | [optional] 
**status** | **str** |  | 
**is_active** | **bool** |  | [optional] 
**is_archived** | **bool** |  | [optional] 
**has_avatar** | **bool** |  | [optional] 
**backup_scraper_enabled** | **bool** |  | [optional] 
**unread_notifications_count** | **int** |  | [optional] 
**avatar** | [**AvatarObject**](AvatarObject.md) |  | [optional] 
**account** | [**AccountObject**](AccountObject.md) |  | [optional] 
**membership** | [**UserMembershipObject**](UserMembershipObject.md) |  | [optional] 
**workspaces** | [**List[WorkspaceObject]**](WorkspaceObject.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.user_object import UserObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserObject from a JSON string
user_object_instance = UserObject.from_json(json)
# print the JSON string representation of the object
print(UserObject.to_json())

# convert the object into a dict
user_object_dict = user_object_instance.to_dict()
# create an instance of UserObject from a dict
user_object_from_dict = UserObject.from_dict(user_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


