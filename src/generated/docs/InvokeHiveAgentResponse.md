# InvokeHiveAgentResponse

Hive Agent run accepted response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Identifier for the queued Hive Agent run. | [optional] 
**request_id** | **str** | Unique identifier for this invocation. | [optional] 
**status** | **str** | Initial run status. Usually &#x60;pending&#x60;. | [optional] 
**webhook_secret** | **str** | Secret used to verify the signed callback. | [optional] 

## Example

```python
from fetch_hive_sdk.models.invoke_hive_agent_response import InvokeHiveAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeHiveAgentResponse from a JSON string
invoke_hive_agent_response_instance = InvokeHiveAgentResponse.from_json(json)
# print the JSON string representation of the object
print(InvokeHiveAgentResponse.to_json())

# convert the object into a dict
invoke_hive_agent_response_dict = invoke_hive_agent_response_instance.to_dict()
# create an instance of InvokeHiveAgentResponse from a dict
invoke_hive_agent_response_from_dict = InvokeHiveAgentResponse.from_dict(invoke_hive_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


