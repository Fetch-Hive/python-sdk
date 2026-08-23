# AssetObjectTranscription

(value may be null)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**error_code** | **str** | (value may be null) | [optional] 
**error_message** | **str** | (value may be null) | [optional] 
**completed_at** | **datetime** | (value may be null) | [optional] 

## Example

```python
from fetch_hive_sdk.models.asset_object_transcription import AssetObjectTranscription

# TODO update the JSON string below
json = "{}"
# create an instance of AssetObjectTranscription from a JSON string
asset_object_transcription_instance = AssetObjectTranscription.from_json(json)
# print the JSON string representation of the object
print(AssetObjectTranscription.to_json())

# convert the object into a dict
asset_object_transcription_dict = asset_object_transcription_instance.to_dict()
# create an instance of AssetObjectTranscription from a dict
asset_object_transcription_from_dict = AssetObjectTranscription.from_dict(asset_object_transcription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


