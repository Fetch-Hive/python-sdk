# AgentInvokeAsyncConfig

Controls background workflow tools for this invoke. Defaults: `allow_background` is true when `thread_id` is present, or when `callback_url` is set; otherwise it is false so existing stateless integrators keep synchronous behaviour. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | HTTPS URL that receives a signed &#x60;agent.delegation.completed&#x60; POST when a background workflow finishes. Signed with the parent agent&#39;s webhook secret.  | [optional] 
**allow_background** | **bool** | When false, &#x60;run_workflow&#x60; stays synchronous. Long or human-in-the-loop workflows return a tool error instead of a pending delegation.  | [optional] 

## Example

```python
from fetch_hive_sdk.models.agent_invoke_async_config import AgentInvokeAsyncConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentInvokeAsyncConfig from a JSON string
agent_invoke_async_config_instance = AgentInvokeAsyncConfig.from_json(json)
# print the JSON string representation of the object
print(AgentInvokeAsyncConfig.to_json())

# convert the object into a dict
agent_invoke_async_config_dict = agent_invoke_async_config_instance.to_dict()
# create an instance of AgentInvokeAsyncConfig from a dict
agent_invoke_async_config_from_dict = AgentInvokeAsyncConfig.from_dict(agent_invoke_async_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


