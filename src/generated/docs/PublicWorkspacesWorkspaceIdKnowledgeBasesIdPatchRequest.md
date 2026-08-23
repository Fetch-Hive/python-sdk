# PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base** | [**PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequestKnowledgeBase**](PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequestKnowledgeBase.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_id_patch_request import PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest from a JSON string
public_workspaces_workspace_id_knowledge_bases_id_patch_request_instance = PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest.to_json())

# convert the object into a dict
public_workspaces_workspace_id_knowledge_bases_id_patch_request_dict = public_workspaces_workspace_id_knowledge_bases_id_patch_request_instance.to_dict()
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest from a dict
public_workspaces_workspace_id_knowledge_bases_id_patch_request_from_dict = PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest.from_dict(public_workspaces_workspace_id_knowledge_bases_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


