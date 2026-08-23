# GetPublicWorkspacesKnowledgeBasesItems200ResponseKnowledgeBaseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**knowledge_base_id** | **UUID** |  | 
**item_type** | **str** |  | 
**run_status** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from fetch_hive_sdk.models.get_public_workspaces_knowledge_bases_items200_response_knowledge_base_items_inner import GetPublicWorkspacesKnowledgeBasesItems200ResponseKnowledgeBaseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicWorkspacesKnowledgeBasesItems200ResponseKnowledgeBaseItemsInner from a JSON string
get_public_workspaces_knowledge_bases_items200_response_knowledge_base_items_inner_instance = GetPublicWorkspacesKnowledgeBasesItems200ResponseKnowledgeBaseItemsInner.from_json(json)
# print the JSON string representation of the object
print(GetPublicWorkspacesKnowledgeBasesItems200ResponseKnowledgeBaseItemsInner.to_json())

# convert the object into a dict
get_public_workspaces_knowledge_bases_items200_response_knowledge_base_items_inner_dict = get_public_workspaces_knowledge_bases_items200_response_knowledge_base_items_inner_instance.to_dict()
# create an instance of GetPublicWorkspacesKnowledgeBasesItems200ResponseKnowledgeBaseItemsInner from a dict
get_public_workspaces_knowledge_bases_items200_response_knowledge_base_items_inner_from_dict = GetPublicWorkspacesKnowledgeBasesItems200ResponseKnowledgeBaseItemsInner.from_dict(get_public_workspaces_knowledge_bases_items200_response_knowledge_base_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


