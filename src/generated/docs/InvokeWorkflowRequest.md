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
**tool_approval** | **str** | &#x60;policy&#x60; follows the deployment&#39;s saved auto-approve switch. Omit the field for the same behavior. &#x60;auto_approve&#x60; applies to this call only, and only when the API key is allowed to auto-approve actions. Any other value is &#x60;400 invalid_tool_approval&#x60;. A key without the permission, a signed-in token, or a webhook is &#x60;403 tool_approval_override_not_permitted&#x60; before the workflow starts. The call does not change the deployment&#39;s saved switch. Destructive actions still ask. Deny rules still block the action.  | [optional] 

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


