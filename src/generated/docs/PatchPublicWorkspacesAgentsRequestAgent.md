# PatchPublicWorkspacesAgentsRequestAgent


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
from fetch_hive_sdk.models.patch_public_workspaces_agents_request_agent import PatchPublicWorkspacesAgentsRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPublicWorkspacesAgentsRequestAgent from a JSON string
patch_public_workspaces_agents_request_agent_instance = PatchPublicWorkspacesAgentsRequestAgent.from_json(json)
# print the JSON string representation of the object
print(PatchPublicWorkspacesAgentsRequestAgent.to_json())

# convert the object into a dict
patch_public_workspaces_agents_request_agent_dict = patch_public_workspaces_agents_request_agent_instance.to_dict()
# create an instance of PatchPublicWorkspacesAgentsRequestAgent from a dict
patch_public_workspaces_agents_request_agent_from_dict = PatchPublicWorkspacesAgentsRequestAgent.from_dict(patch_public_workspaces_agents_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


