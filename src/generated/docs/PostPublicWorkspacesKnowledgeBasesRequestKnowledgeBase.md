# PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase


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
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_request_knowledge_base import PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase from a JSON string
post_public_workspaces_knowledge_bases_request_knowledge_base_instance = PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase.to_json())

# convert the object into a dict
post_public_workspaces_knowledge_bases_request_knowledge_base_dict = post_public_workspaces_knowledge_bases_request_knowledge_base_instance.to_dict()
# create an instance of PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase from a dict
post_public_workspaces_knowledge_bases_request_knowledge_base_from_dict = PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase.from_dict(post_public_workspaces_knowledge_bases_request_knowledge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


