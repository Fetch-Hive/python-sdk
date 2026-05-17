# V1KnowledgeBasesIdSearchPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | **str** |  | 
**search_type** | **str** |  | 
**search_chunk_limit** | **int** |  | 
**search_score_threshold** | **float** |  | 

## Example

```python
from fetch_hive_sdk.models.v1_knowledge_bases_id_search_post_request import V1KnowledgeBasesIdSearchPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1KnowledgeBasesIdSearchPostRequest from a JSON string
v1_knowledge_bases_id_search_post_request_instance = V1KnowledgeBasesIdSearchPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1KnowledgeBasesIdSearchPostRequest.to_json())

# convert the object into a dict
v1_knowledge_bases_id_search_post_request_dict = v1_knowledge_bases_id_search_post_request_instance.to_dict()
# create an instance of V1KnowledgeBasesIdSearchPostRequest from a dict
v1_knowledge_bases_id_search_post_request_from_dict = V1KnowledgeBasesIdSearchPostRequest.from_dict(v1_knowledge_bases_id_search_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


