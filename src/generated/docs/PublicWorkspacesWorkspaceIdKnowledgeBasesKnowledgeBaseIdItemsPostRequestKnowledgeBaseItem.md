# PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequestKnowledgeBaseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 
**response_type** | **str** |  | [optional] 
**data_content** | **str** |  | [optional] 
**data_query** | **str** | (value may be null) | [optional] 
**delete_email_data** | **str** |  | [optional] 
**delete_telephone_data** | **str** |  | [optional] 
**chunking_strategy** | **str** |  | [optional] 
**chunk_overlap** | **int** |  | [optional] 
**maximum_chunk_length** | **int** |  | [optional] 
**asset_id** | **UUID** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request_knowledge_base_item import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequestKnowledgeBaseItem

# TODO update the JSON string below
json = "{}"
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequestKnowledgeBaseItem from a JSON string
public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request_knowledge_base_item_instance = PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequestKnowledgeBaseItem.from_json(json)
# print the JSON string representation of the object
print(PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequestKnowledgeBaseItem.to_json())

# convert the object into a dict
public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request_knowledge_base_item_dict = public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request_knowledge_base_item_instance.to_dict()
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequestKnowledgeBaseItem from a dict
public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request_knowledge_base_item_from_dict = PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequestKnowledgeBaseItem.from_dict(public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request_knowledge_base_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


