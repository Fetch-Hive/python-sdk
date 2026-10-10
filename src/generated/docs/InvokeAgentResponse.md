# InvokeAgentResponse

Agent response. All fields are optional because the shape differs slightly between streaming and non-streaming modes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier for this invocation. | [optional] 
**response** | **str** | The agent&#39;s final text response (non-streaming only).  | [optional] 
**thread_id** | **str** | Caller &#x60;thread_id&#x60;, or null when the invoke did not send one.  (value may be null) | [optional] 
**status** | **str** | Always present. &#x60;completed&#x60; or &#x60;awaiting_approval&#x60;. With tool approvals disabled this is &#x60;completed&#x60;.  | [optional] 
**run_id** | **str** | Public request id for this run. Same value as &#x60;request_id&#x60;. | [optional] 
**pending_tool_approvals** | [**List[PendingToolApproval]**](PendingToolApproval.md) | Present only when &#x60;status&#x60; is &#x60;awaiting_approval&#x60;.  | [optional] 
**denied_tool_calls** | [**List[DeniedToolCall]**](DeniedToolCall.md) | Present only when this turn denied one or more tools. | [optional] 
**tool_approval** | **str** | Effective mode for this call. &#x60;auto_approve&#x60; when this call sent &#x60;auto_approve&#x60; or a saved auto-approve switch applied. Otherwise &#x60;policy&#x60;.  | [optional] 
**auto_approved_tool_calls** | [**List[InvokeAgentResponseAutoApprovedToolCallsInner]**](InvokeAgentResponseAutoApprovedToolCallsInner.md) | Present when one or more actions ran because of an auto-approve override. Each item has &#x60;summary&#x60; and &#x60;tool_name&#x60;.  | [optional] 
**model** | **str** | Model used for this invocation. | [optional] 
**usage** | [**TokenUsage**](TokenUsage.md) |  | [optional] 
**tool_calls** | [**List[ToolInvocation]**](ToolInvocation.md) | Tool invocations made during this run (if any). | [optional] 
**artifacts** | [**List[GeneratedArtifact]**](GeneratedArtifact.md) | Generated documents and images produced by completed artifact tools. | [optional] 
**pending_delegations** | [**List[PendingDelegation]**](PendingDelegation.md) | Background workflows started during this turn. Present only when the turn ended with one or more pending delegations.  | [optional] 

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


