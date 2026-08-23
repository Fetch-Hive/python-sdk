# PublicModelsGet200ResponseInner


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
from fetch_hive_sdk.models.public_models_get200_response_inner import PublicModelsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicModelsGet200ResponseInner from a JSON string
public_models_get200_response_inner_instance = PublicModelsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PublicModelsGet200ResponseInner.to_json())

# convert the object into a dict
public_models_get200_response_inner_dict = public_models_get200_response_inner_instance.to_dict()
# create an instance of PublicModelsGet200ResponseInner from a dict
public_models_get200_response_inner_from_dict = PublicModelsGet200ResponseInner.from_dict(public_models_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


