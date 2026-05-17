# InvokeWorkflowResponse

Synchronous workflow result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier for this invocation. | [optional] 
**run_id** | **str** | Workflow run identifier. | [optional] 
**status** | **str** | Final status of the workflow run. | [optional] 
**output** | **str** | The workflow&#39;s final output value. May contain serialised JSON; parse client-side as needed.  | [optional] 
**error** | **str** | Error message when &#x60;status&#x60; is &#x60;failed&#x60;. | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_workflow_response import InvokeWorkflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeWorkflowResponse from a JSON string
invoke_workflow_response_instance = InvokeWorkflowResponse.from_json(json)
# print the JSON string representation of the object
print(InvokeWorkflowResponse.to_json())

# convert the object into a dict
invoke_workflow_response_dict = invoke_workflow_response_instance.to_dict()
# create an instance of InvokeWorkflowResponse from a dict
invoke_workflow_response_from_dict = InvokeWorkflowResponse.from_dict(invoke_workflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


