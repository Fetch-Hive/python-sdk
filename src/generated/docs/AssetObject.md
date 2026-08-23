# AssetObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**object_key** | **str** |  | [optional] 
**file_name** | **str** |  | 
**file_url** | **str** |  | 
**file_url_expires_at** | **datetime** |  | 
**file_type** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**asset_type** | **str** |  | 
**workspace_id** | **UUID** | (value may be null) | [optional] 
**uploaded_at** | **datetime** |  | 
**error_message** | **str** | (value may be null) | [optional] 
**transcription** | [**AssetObjectTranscription**](AssetObjectTranscription.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.asset_object import AssetObject

# TODO update the JSON string below
json = "{}"
# create an instance of AssetObject from a JSON string
asset_object_instance = AssetObject.from_json(json)
# print the JSON string representation of the object
print(AssetObject.to_json())

# convert the object into a dict
asset_object_dict = asset_object_instance.to_dict()
# create an instance of AssetObject from a dict
asset_object_from_dict = AssetObject.from_dict(asset_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


