# PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequestKnowledgeBaseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**data_content** | **str** |  | [optional] 
**data_query** | **str** |  | [optional] 
**delete_email_data** | **str** |  | [optional] 
**delete_telephone_data** | **str** |  | [optional] 
**chunking_strategy** | **str** |  | [optional] 
**chunk_overlap** | **int** |  | [optional] 
**maximum_chunk_length** | **int** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request_knowledge_base_item import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequestKnowledgeBaseItem

# TODO update the JSON string below
json = "{}"
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequestKnowledgeBaseItem from a JSON string
public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request_knowledge_base_item_instance = PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequestKnowledgeBaseItem.from_json(json)
# print the JSON string representation of the object
print(PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequestKnowledgeBaseItem.to_json())

# convert the object into a dict
public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request_knowledge_base_item_dict = public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request_knowledge_base_item_instance.to_dict()
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequestKnowledgeBaseItem from a dict
public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request_knowledge_base_item_from_dict = PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequestKnowledgeBaseItem.from_dict(public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request_knowledge_base_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


