# HiveAgentAsyncConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Must be &#x60;true&#x60;. Hive Agent invocation is async-only. | 
**callback_url** | **str** | HTTPS URL that receives the signed terminal callback. | 

## Example

```python
from fetch_hive_sdk.models.hive_agent_async_config import HiveAgentAsyncConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HiveAgentAsyncConfig from a JSON string
hive_agent_async_config_instance = HiveAgentAsyncConfig.from_json(json)
# print the JSON string representation of the object
print(HiveAgentAsyncConfig.to_json())

# convert the object into a dict
hive_agent_async_config_dict = hive_agent_async_config_instance.to_dict()
# create an instance of HiveAgentAsyncConfig from a dict
hive_agent_async_config_from_dict = HiveAgentAsyncConfig.from_dict(hive_agent_async_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


