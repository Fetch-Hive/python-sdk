# PostPublicWorkspacesKnowledgeBasesSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | **str** |  | 
**search_type** | **str** |  | 
**search_chunk_limit** | **int** |  | 
**search_score_threshold** | **float** |  | 

## Example

```python
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_search_request import PostPublicWorkspacesKnowledgeBasesSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesKnowledgeBasesSearchRequest from a JSON string
post_public_workspaces_knowledge_bases_search_request_instance = PostPublicWorkspacesKnowledgeBasesSearchRequest.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesKnowledgeBasesSearchRequest.to_json())

# convert the object into a dict
post_public_workspaces_knowledge_bases_search_request_dict = post_public_workspaces_knowledge_bases_search_request_instance.to_dict()
# create an instance of PostPublicWorkspacesKnowledgeBasesSearchRequest from a dict
post_public_workspaces_knowledge_bases_search_request_from_dict = PostPublicWorkspacesKnowledgeBasesSearchRequest.from_dict(post_public_workspaces_knowledge_bases_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


