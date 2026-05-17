# V1GlobalEmbeddingsPost200ResponseUsage

OpenAI  usage for this request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **UUID** |  | [optional] 
**total_tokens** | **UUID** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.v1_global_embeddings_post200_response_usage import V1GlobalEmbeddingsPost200ResponseUsage

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalEmbeddingsPost200ResponseUsage from a JSON string
v1_global_embeddings_post200_response_usage_instance = V1GlobalEmbeddingsPost200ResponseUsage.from_json(json)
# print the JSON string representation of the object
print(V1GlobalEmbeddingsPost200ResponseUsage.to_json())

# convert the object into a dict
v1_global_embeddings_post200_response_usage_dict = v1_global_embeddings_post200_response_usage_instance.to_dict()
# create an instance of V1GlobalEmbeddingsPost200ResponseUsage from a dict
v1_global_embeddings_post200_response_usage_from_dict = V1GlobalEmbeddingsPost200ResponseUsage.from_dict(v1_global_embeddings_post200_response_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


