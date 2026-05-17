# InvokeWorkflowAsyncResponse

Asynchronous workflow accepted response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Identifier for the queued workflow run. Use this to poll &#x60;GET /v1/workflow_runs/{id}&#x60; on the management API.  | [optional] 
**status** | **str** | Always &#x60;\&quot;queued\&quot;&#x60; for async responses. | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_workflow_async_response import InvokeWorkflowAsyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeWorkflowAsyncResponse from a JSON string
invoke_workflow_async_response_instance = InvokeWorkflowAsyncResponse.from_json(json)
# print the JSON string representation of the object
print(InvokeWorkflowAsyncResponse.to_json())

# convert the object into a dict
invoke_workflow_async_response_dict = invoke_workflow_async_response_instance.to_dict()
# create an instance of InvokeWorkflowAsyncResponse from a dict
invoke_workflow_async_response_from_dict = InvokeWorkflowAsyncResponse.from_dict(invoke_workflow_async_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


