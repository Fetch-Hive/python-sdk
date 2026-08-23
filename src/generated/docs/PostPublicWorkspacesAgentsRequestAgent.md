# PostPublicWorkspacesAgentsRequestAgent


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
from fetch_hive_sdk.models.post_public_workspaces_agents_request_agent import PostPublicWorkspacesAgentsRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesAgentsRequestAgent from a JSON string
post_public_workspaces_agents_request_agent_instance = PostPublicWorkspacesAgentsRequestAgent.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesAgentsRequestAgent.to_json())

# convert the object into a dict
post_public_workspaces_agents_request_agent_dict = post_public_workspaces_agents_request_agent_instance.to_dict()
# create an instance of PostPublicWorkspacesAgentsRequestAgent from a dict
post_public_workspaces_agents_request_agent_from_dict = PostPublicWorkspacesAgentsRequestAgent.from_dict(post_public_workspaces_agents_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


