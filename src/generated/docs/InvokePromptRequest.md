# InvokePromptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | **str** | Slug of the prompt deployment to invoke. | 
**variant** | **str** | Optional variant name to override the default. | [optional] [default to '']
**inputs** | **Dict[str, object]** | Key-value pairs that are substituted into the prompt template. Values may be strings, numbers, booleans, arrays, or nested objects.  | [optional] 
**streaming** | **bool** | When &#x60;true&#x60; the response is a Server-Sent Events stream rather than a single JSON body.  | [optional] [default to False]
**user** | **str** | Optional opaque caller identifier for audit logging. | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Flat caller-defined metadata stored separately from internal metadata for log display and filtering. Keys must be non-empty strings; values must be strings, numbers, booleans, or null. | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_prompt_request import InvokePromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvokePromptRequest from a JSON string
invoke_prompt_request_instance = InvokePromptRequest.from_json(json)
# print the JSON string representation of the object
print(InvokePromptRequest.to_json())

# convert the object into a dict
invoke_prompt_request_dict = invoke_prompt_request_instance.to_dict()
# create an instance of InvokePromptRequest from a dict
invoke_prompt_request_from_dict = InvokePromptRequest.from_dict(invoke_prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


