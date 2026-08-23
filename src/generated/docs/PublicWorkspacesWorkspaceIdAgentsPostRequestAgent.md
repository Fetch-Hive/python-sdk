# PublicWorkspacesWorkspaceIdAgentsPostRequestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**llm_model** | **str** |  | 
**model_type** | **str** |  | 
**description** | **str** |  | [optional] 
**instruction_prompt** | **str** |  | [optional] 
**temperature** | **float** |  | [optional] 
**max_token** | **UUID** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_post_request_agent import PublicWorkspacesWorkspaceIdAgentsPostRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PublicWorkspacesWorkspaceIdAgentsPostRequestAgent from a JSON string
public_workspaces_workspace_id_agents_post_request_agent_instance = PublicWorkspacesWorkspaceIdAgentsPostRequestAgent.from_json(json)
# print the JSON string representation of the object
print(PublicWorkspacesWorkspaceIdAgentsPostRequestAgent.to_json())

# convert the object into a dict
public_workspaces_workspace_id_agents_post_request_agent_dict = public_workspaces_workspace_id_agents_post_request_agent_instance.to_dict()
# create an instance of PublicWorkspacesWorkspaceIdAgentsPostRequestAgent from a dict
public_workspaces_workspace_id_agents_post_request_agent_from_dict = PublicWorkspacesWorkspaceIdAgentsPostRequestAgent.from_dict(public_workspaces_workspace_id_agents_post_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


