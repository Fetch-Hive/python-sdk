# V1GlobalEmbeddingsPostRequestEmbedding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text to embed | 
**model** | **str** | OpenAI embedding model to use (defaults to text-embedding-3-small) | [optional] 

## Example

```python
from fetch_hive_sdk.models.v1_global_embeddings_post_request_embedding import V1GlobalEmbeddingsPostRequestEmbedding

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalEmbeddingsPostRequestEmbedding from a JSON string
v1_global_embeddings_post_request_embedding_instance = V1GlobalEmbeddingsPostRequestEmbedding.from_json(json)
# print the JSON string representation of the object
print(V1GlobalEmbeddingsPostRequestEmbedding.to_json())

# convert the object into a dict
v1_global_embeddings_post_request_embedding_dict = v1_global_embeddings_post_request_embedding_instance.to_dict()
# create an instance of V1GlobalEmbeddingsPostRequestEmbedding from a dict
v1_global_embeddings_post_request_embedding_from_dict = V1GlobalEmbeddingsPostRequestEmbedding.from_dict(v1_global_embeddings_post_request_embedding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


