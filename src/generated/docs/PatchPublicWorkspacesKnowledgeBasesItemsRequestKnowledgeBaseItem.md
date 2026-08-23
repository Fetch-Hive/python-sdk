# PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem


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
from fetch_hive_sdk.models.patch_public_workspaces_knowledge_bases_items_request_knowledge_base_item import PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem from a JSON string
patch_public_workspaces_knowledge_bases_items_request_knowledge_base_item_instance = PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem.from_json(json)
# print the JSON string representation of the object
print(PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem.to_json())

# convert the object into a dict
patch_public_workspaces_knowledge_bases_items_request_knowledge_base_item_dict = patch_public_workspaces_knowledge_bases_items_request_knowledge_base_item_instance.to_dict()
# create an instance of PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem from a dict
patch_public_workspaces_knowledge_bases_items_request_knowledge_base_item_from_dict = PatchPublicWorkspacesKnowledgeBasesItemsRequestKnowledgeBaseItem.from_dict(patch_public_workspaces_knowledge_bases_items_request_knowledge_base_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


