# PublicWorkspacesWorkspaceIdAgentsIdPatchRequestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**llm_model** | **str** |  | [optional] 
**model_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instruction_prompt** | **str** |  | [optional] 
**temperature** | **float** |  | [optional] 
**max_token** | **int** |  | [optional] 
**max_thinking_token** | **int** |  | [optional] 
**anthropic_prompt_cache_ttl** | **str** |  | [optional] 
**reasoning_effort** | **str** |  | [optional] 
**tool_choice** | **str** |  | [optional] 
**max_tool_calls** | **int** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_id_patch_request_agent import PublicWorkspacesWorkspaceIdAgentsIdPatchRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PublicWorkspacesWorkspaceIdAgentsIdPatchRequestAgent from a JSON string
public_workspaces_workspace_id_agents_id_patch_request_agent_instance = PublicWorkspacesWorkspaceIdAgentsIdPatchRequestAgent.from_json(json)
# print the JSON string representation of the object
print(PublicWorkspacesWorkspaceIdAgentsIdPatchRequestAgent.to_json())

# convert the object into a dict
public_workspaces_workspace_id_agents_id_patch_request_agent_dict = public_workspaces_workspace_id_agents_id_patch_request_agent_instance.to_dict()
# create an instance of PublicWorkspacesWorkspaceIdAgentsIdPatchRequestAgent from a dict
public_workspaces_workspace_id_agents_id_patch_request_agent_from_dict = PublicWorkspacesWorkspaceIdAgentsIdPatchRequestAgent.from_dict(public_workspaces_workspace_id_agents_id_patch_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


