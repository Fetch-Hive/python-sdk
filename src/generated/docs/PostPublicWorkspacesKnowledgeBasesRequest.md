# PostPublicWorkspacesKnowledgeBasesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base** | [**PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase**](PostPublicWorkspacesKnowledgeBasesRequestKnowledgeBase.md) |  | 

## Example

```python
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_request import PostPublicWorkspacesKnowledgeBasesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesKnowledgeBasesRequest from a JSON string
post_public_workspaces_knowledge_bases_request_instance = PostPublicWorkspacesKnowledgeBasesRequest.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesKnowledgeBasesRequest.to_json())

# convert the object into a dict
post_public_workspaces_knowledge_bases_request_dict = post_public_workspaces_knowledge_bases_request_instance.to_dict()
# create an instance of PostPublicWorkspacesKnowledgeBasesRequest from a dict
post_public_workspaces_knowledge_bases_request_from_dict = PostPublicWorkspacesKnowledgeBasesRequest.from_dict(post_public_workspaces_knowledge_bases_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


