# PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequestKnowledgeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**search_type** | **str** |  | [optional] 
**search_score_threshold** | **float** |  | [optional] 
**search_chunk_limit** | **UUID** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_post_request_knowledge_base import PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequestKnowledgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequestKnowledgeBase from a JSON string
public_workspaces_workspace_id_knowledge_bases_post_request_knowledge_base_instance = PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequestKnowledgeBase.from_json(json)
# print the JSON string representation of the object
print(PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequestKnowledgeBase.to_json())

# convert the object into a dict
public_workspaces_workspace_id_knowledge_bases_post_request_knowledge_base_dict = public_workspaces_workspace_id_knowledge_bases_post_request_knowledge_base_instance.to_dict()
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequestKnowledgeBase from a dict
public_workspaces_workspace_id_knowledge_bases_post_request_knowledge_base_from_dict = PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequestKnowledgeBase.from_dict(public_workspaces_workspace_id_knowledge_bases_post_request_knowledge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


