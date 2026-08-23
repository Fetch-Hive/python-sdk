# InvokeHiveAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hive_agent** | **str** | Hive Agent ID from the dashboard. | 
**objective** | **str** | Specific objective for the planner to create work nodes from. | 
**sources** | [**HiveAgentSources**](HiveAgentSources.md) |  | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Flat caller-defined metadata stored separately from internal metadata for log display and filtering. Keys must be non-empty strings; values must be strings, numbers, booleans, or null. | [optional] 
**var_async** | [**HiveAgentAsyncConfig**](HiveAgentAsyncConfig.md) |  | 

## Example

```python
from fetch_hive_sdk.models.invoke_hive_agent_request import InvokeHiveAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeHiveAgentRequest from a JSON string
invoke_hive_agent_request_instance = InvokeHiveAgentRequest.from_json(json)
# print the JSON string representation of the object
print(InvokeHiveAgentRequest.to_json())

# convert the object into a dict
invoke_hive_agent_request_dict = invoke_hive_agent_request_instance.to_dict()
# create an instance of InvokeHiveAgentRequest from a dict
invoke_hive_agent_request_from_dict = InvokeHiveAgentRequest.from_dict(invoke_hive_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


