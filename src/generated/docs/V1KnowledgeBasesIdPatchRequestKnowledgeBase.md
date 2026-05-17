# V1KnowledgeBasesIdPatchRequestKnowledgeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**search_type** | **str** |  | [optional] 
**search_score_threshold** | **float** |  | [optional] 
**search_chunk_limit** | **int** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.v1_knowledge_bases_id_patch_request_knowledge_base import V1KnowledgeBasesIdPatchRequestKnowledgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of V1KnowledgeBasesIdPatchRequestKnowledgeBase from a JSON string
v1_knowledge_bases_id_patch_request_knowledge_base_instance = V1KnowledgeBasesIdPatchRequestKnowledgeBase.from_json(json)
# print the JSON string representation of the object
print(V1KnowledgeBasesIdPatchRequestKnowledgeBase.to_json())

# convert the object into a dict
v1_knowledge_bases_id_patch_request_knowledge_base_dict = v1_knowledge_bases_id_patch_request_knowledge_base_instance.to_dict()
# create an instance of V1KnowledgeBasesIdPatchRequestKnowledgeBase from a dict
v1_knowledge_bases_id_patch_request_knowledge_base_from_dict = V1KnowledgeBasesIdPatchRequestKnowledgeBase.from_dict(v1_knowledge_bases_id_patch_request_knowledge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


