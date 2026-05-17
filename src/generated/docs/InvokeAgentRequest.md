# InvokeAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The user&#39;s message to send to the agent. | 
**agent** | **str** | Slug of the agent to invoke. | 
**thread_id** | **str** | Find-or-create a persistent conversation thread by this caller- supplied string. Leave empty to start a stateless invocation.  | [optional] [default to '']
**streaming** | **bool** | When &#x60;true&#x60; the response is a Server-Sent Events stream.  | [optional] [default to False]
**user** | **str** | Optional opaque caller identifier for audit logging. | [optional] 
**messages** | [**List[AgentMessage]**](AgentMessage.md) | Ephemeral conversation history supplied by the caller. Not stored in the database. Takes precedence over &#x60;thread_id&#x60; history when both are provided.  | [optional] 
**image_urls** | **List[str]** | HTTPS image URLs attached to the current &#x60;message&#x60; for multimodal inputs. All URLs must start with &#x60;https://&#x60;.  | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_agent_request import InvokeAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeAgentRequest from a JSON string
invoke_agent_request_instance = InvokeAgentRequest.from_json(json)
# print the JSON string representation of the object
print(InvokeAgentRequest.to_json())

# convert the object into a dict
invoke_agent_request_dict = invoke_agent_request_instance.to_dict()
# create an instance of InvokeAgentRequest from a dict
invoke_agent_request_from_dict = InvokeAgentRequest.from_dict(invoke_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


