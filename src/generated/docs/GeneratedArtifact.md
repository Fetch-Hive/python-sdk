# GeneratedArtifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**file_url** | **str** |  | 
**file_name** | **str** |  | [optional] 
**file_type** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**asset_type** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**tool_id** | **str** |  | [optional] 
**tool_name** | **str** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.generated_artifact import GeneratedArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedArtifact from a JSON string
generated_artifact_instance = GeneratedArtifact.from_json(json)
# print the JSON string representation of the object
print(GeneratedArtifact.to_json())

# convert the object into a dict
generated_artifact_dict = generated_artifact_instance.to_dict()
# create an instance of GeneratedArtifact from a dict
generated_artifact_from_dict = GeneratedArtifact.from_dict(generated_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


