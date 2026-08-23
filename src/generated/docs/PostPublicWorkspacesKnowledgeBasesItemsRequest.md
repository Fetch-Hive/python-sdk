# PostPublicWorkspacesKnowledgeBasesItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base_item** | [**PostPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem**](PostPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem.md) |  | 

## Example

```python
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_items_request import PostPublicWorkspacesKnowledgeBasesItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesKnowledgeBasesItemsRequest from a JSON string
post_public_workspaces_knowledge_bases_items_request_instance = PostPublicWorkspacesKnowledgeBasesItemsRequest.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesKnowledgeBasesItemsRequest.to_json())

# convert the object into a dict
post_public_workspaces_knowledge_bases_items_request_dict = post_public_workspaces_knowledge_bases_items_request_instance.to_dict()
# create an instance of PostPublicWorkspacesKnowledgeBasesItemsRequest from a dict
post_public_workspaces_knowledge_bases_items_request_from_dict = PostPublicWorkspacesKnowledgeBasesItemsRequest.from_dict(post_public_workspaces_knowledge_bases_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


