# V1KnowledgeBasesPostRequestKnowledgeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**search_type** | **str** |  | [optional] 
**search_score_threshold** | **float** |  | [optional] 
**search_chunk_limit** | **UUID** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.v1_knowledge_bases_post_request_knowledge_base import V1KnowledgeBasesPostRequestKnowledgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of V1KnowledgeBasesPostRequestKnowledgeBase from a JSON string
v1_knowledge_bases_post_request_knowledge_base_instance = V1KnowledgeBasesPostRequestKnowledgeBase.from_json(json)
# print the JSON string representation of the object
print(V1KnowledgeBasesPostRequestKnowledgeBase.to_json())

# convert the object into a dict
v1_knowledge_bases_post_request_knowledge_base_dict = v1_knowledge_bases_post_request_knowledge_base_instance.to_dict()
# create an instance of V1KnowledgeBasesPostRequestKnowledgeBase from a dict
v1_knowledge_bases_post_request_knowledge_base_from_dict = V1KnowledgeBasesPostRequestKnowledgeBase.from_dict(v1_knowledge_bases_post_request_knowledge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


