# InvokePromptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier for this invocation. | [optional] 
**response** | **str** | The model&#39;s text response. For streaming requests this field is absent; content arrives as &#x60;SseChunk&#x60; events instead.  | [optional] 
**model** | **str** | Model identifier used for this invocation. | [optional] 
**usage** | [**TokenUsage**](TokenUsage.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_prompt_response import InvokePromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvokePromptResponse from a JSON string
invoke_prompt_response_instance = InvokePromptResponse.from_json(json)
# print the JSON string representation of the object
print(InvokePromptResponse.to_json())

# convert the object into a dict
invoke_prompt_response_dict = invoke_prompt_response_instance.to_dict()
# create an instance of InvokePromptResponse from a dict
invoke_prompt_response_from_dict = InvokePromptResponse.from_dict(invoke_prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


