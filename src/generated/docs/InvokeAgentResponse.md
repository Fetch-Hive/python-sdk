# InvokeAgentResponse

Agent response. All fields are optional because the shape differs slightly between streaming and non-streaming modes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier for this invocation. | [optional] 
**response** | **str** | The agent&#39;s final text response (non-streaming only).  | [optional] 
**thread_id** | **str** | Thread identifier. Present when &#x60;thread_id&#x60; was supplied. | [optional] 
**model** | **str** | Model used for this invocation. | [optional] 
**usage** | [**TokenUsage**](TokenUsage.md) |  | [optional] 
**tool_calls** | [**List[ToolInvocation]**](ToolInvocation.md) | Tool invocations made during this run (if any). | [optional] 
**artifacts** | [**List[GeneratedArtifact]**](GeneratedArtifact.md) | Generated documents and images produced by completed artifact tools. | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_agent_response import InvokeAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeAgentResponse from a JSON string
invoke_agent_response_instance = InvokeAgentResponse.from_json(json)
# print the JSON string representation of the object
print(InvokeAgentResponse.to_json())

# convert the object into a dict
invoke_agent_response_dict = invoke_agent_response_instance.to_dict()
# create an instance of InvokeAgentResponse from a dict
invoke_agent_response_from_dict = InvokeAgentResponse.from_dict(invoke_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


