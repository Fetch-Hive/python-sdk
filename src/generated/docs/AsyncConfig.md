# AsyncConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | When &#x60;true&#x60;, the endpoint returns immediately with a &#x60;run_id&#x60; rather than waiting for the workflow to complete.  | 
**callback_url** | **str** | Optional HTTPS URL that receives a POST with the workflow result when execution finishes (async mode only).  | [optional] 

## Example

```python
from fetch_hive_sdk.models.async_config import AsyncConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncConfig from a JSON string
async_config_instance = AsyncConfig.from_json(json)
# print the JSON string representation of the object
print(AsyncConfig.to_json())

# convert the object into a dict
async_config_dict = async_config_instance.to_dict()
# create an instance of AsyncConfig from a dict
async_config_from_dict = AsyncConfig.from_dict(async_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


