# PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | **str** |  | 
**search_type** | **str** |  | 
**search_chunk_limit** | **int** |  | 
**search_score_threshold** | **float** |  | 

## Example

```python
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_id_search_post_request import PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest from a JSON string
public_workspaces_workspace_id_knowledge_bases_id_search_post_request_instance = PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest.from_json(json)
# print the JSON string representation of the object
print(PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest.to_json())

# convert the object into a dict
public_workspaces_workspace_id_knowledge_bases_id_search_post_request_dict = public_workspaces_workspace_id_knowledge_bases_id_search_post_request_instance.to_dict()
# create an instance of PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest from a dict
public_workspaces_workspace_id_knowledge_bases_id_search_post_request_from_dict = PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest.from_dict(public_workspaces_workspace_id_knowledge_bases_id_search_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


