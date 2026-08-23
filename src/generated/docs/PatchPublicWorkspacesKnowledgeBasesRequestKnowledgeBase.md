# PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase


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
from fetch_hive_sdk.models.patch_public_workspaces_knowledge_bases_request_knowledge_base import PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase from a JSON string
patch_public_workspaces_knowledge_bases_request_knowledge_base_instance = PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase.from_json(json)
# print the JSON string representation of the object
print(PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase.to_json())

# convert the object into a dict
patch_public_workspaces_knowledge_bases_request_knowledge_base_dict = patch_public_workspaces_knowledge_bases_request_knowledge_base_instance.to_dict()
# create an instance of PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase from a dict
patch_public_workspaces_knowledge_bases_request_knowledge_base_from_dict = PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase.from_dict(patch_public_workspaces_knowledge_bases_request_knowledge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


