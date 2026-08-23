# GetPublicModels200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**provider** | **str** |  | 
**provider_name** | **str** |  | 
**context_limit** | **int** |  | 
**model_type** | **str** |  | 
**is_image_generation** | **bool** |  | 
**is_vision** | **bool** |  | 
**is_reasoning** | **bool** |  | 
**is_tool_calling** | **bool** |  | 
**is_json_schema** | **bool** |  | 

## Example

```python
from fetch_hive_sdk.models.get_public_models200_response_inner import GetPublicModels200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicModels200ResponseInner from a JSON string
get_public_models200_response_inner_instance = GetPublicModels200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetPublicModels200ResponseInner.to_json())

# convert the object into a dict
get_public_models200_response_inner_dict = get_public_models200_response_inner_instance.to_dict()
# create an instance of GetPublicModels200ResponseInner from a dict
get_public_models200_response_inner_from_dict = GetPublicModels200ResponseInner.from_dict(get_public_models200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


