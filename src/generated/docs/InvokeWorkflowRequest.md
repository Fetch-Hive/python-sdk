# InvokeWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | **str** | Slug of the workflow deployment to invoke. | 
**variant** | **str** | Optional variant name to override the default. | [optional] [default to '']
**inputs** | **Dict[str, object]** | Input variables for the workflow. | [optional] 
**var_async** | [**AsyncConfig**](AsyncConfig.md) |  | [optional] 
**user** | **str** | Optional opaque caller identifier for audit logging. | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Flat caller-defined metadata stored separately from internal metadata for log display and filtering. Keys must be non-empty strings; values must be strings, numbers, booleans, or null. | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_workflow_request import InvokeWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeWorkflowRequest from a JSON string
invoke_workflow_request_instance = InvokeWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(InvokeWorkflowRequest.to_json())

# convert the object into a dict
invoke_workflow_request_dict = invoke_workflow_request_instance.to_dict()
# create an instance of InvokeWorkflowRequest from a dict
invoke_workflow_request_from_dict = InvokeWorkflowRequest.from_dict(invoke_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


