# PatchPublicWorkspacesKnowledgeBasesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base** | [**PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase**](PatchPublicWorkspacesKnowledgeBasesRequestKnowledgeBase.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.patch_public_workspaces_knowledge_bases_request import PatchPublicWorkspacesKnowledgeBasesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPublicWorkspacesKnowledgeBasesRequest from a JSON string
patch_public_workspaces_knowledge_bases_request_instance = PatchPublicWorkspacesKnowledgeBasesRequest.from_json(json)
# print the JSON string representation of the object
print(PatchPublicWorkspacesKnowledgeBasesRequest.to_json())

# convert the object into a dict
patch_public_workspaces_knowledge_bases_request_dict = patch_public_workspaces_knowledge_bases_request_instance.to_dict()
# create an instance of PatchPublicWorkspacesKnowledgeBasesRequest from a dict
patch_public_workspaces_knowledge_bases_request_from_dict = PatchPublicWorkspacesKnowledgeBasesRequest.from_dict(patch_public_workspaces_knowledge_bases_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


