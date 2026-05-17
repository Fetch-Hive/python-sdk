# AvatarObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumb** | **str** | (value may be null) | [optional] 
**medium** | **str** | (value may be null) | [optional] 
**large** | **str** | (value may be null) | [optional] 

## Example

```python
from fetch_hive_sdk.models.avatar_object import AvatarObject

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarObject from a JSON string
avatar_object_instance = AvatarObject.from_json(json)
# print the JSON string representation of the object
print(AvatarObject.to_json())

# convert the object into a dict
avatar_object_dict = avatar_object_instance.to_dict()
# create an instance of AvatarObject from a dict
avatar_object_from_dict = AvatarObject.from_dict(avatar_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


