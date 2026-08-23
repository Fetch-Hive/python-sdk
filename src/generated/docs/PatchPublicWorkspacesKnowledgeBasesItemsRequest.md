# PatchPublicWorkspacesKnowledgeBasesItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base_item** | [**PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem**](PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem.md) |  | 

## Example

```python
from fetch_hive_sdk.models.patch_public_workspaces_knowledge_bases_items_request import PatchPublicWorkspacesKnowledgeBasesItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPublicWorkspacesKnowledgeBasesItemsRequest from a JSON string
patch_public_workspaces_knowledge_bases_items_request_instance = PatchPublicWorkspacesKnowledgeBasesItemsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchPublicWorkspacesKnowledgeBasesItemsRequest.to_json())

# convert the object into a dict
patch_public_workspaces_knowledge_bases_items_request_dict = patch_public_workspaces_knowledge_bases_items_request_instance.to_dict()
# create an instance of PatchPublicWorkspacesKnowledgeBasesItemsRequest from a dict
patch_public_workspaces_knowledge_bases_items_request_from_dict = PatchPublicWorkspacesKnowledgeBasesItemsRequest.from_dict(patch_public_workspaces_knowledge_bases_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


