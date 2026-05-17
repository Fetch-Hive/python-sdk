# V1GlobalEmbeddingsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | [**V1GlobalEmbeddingsPostRequestEmbedding**](V1GlobalEmbeddingsPostRequestEmbedding.md) |  | 

## Example

```python
from fetch_hive_sdk.models.v1_global_embeddings_post_request import V1GlobalEmbeddingsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalEmbeddingsPostRequest from a JSON string
v1_global_embeddings_post_request_instance = V1GlobalEmbeddingsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalEmbeddingsPostRequest.to_json())

# convert the object into a dict
v1_global_embeddings_post_request_dict = v1_global_embeddings_post_request_instance.to_dict()
# create an instance of V1GlobalEmbeddingsPostRequest from a dict
v1_global_embeddings_post_request_from_dict = V1GlobalEmbeddingsPostRequest.from_dict(v1_global_embeddings_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


