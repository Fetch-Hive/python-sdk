# HiveAgentSources

Optional grounded context for the Hive Agent run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_urls** | **List[str]** | Public website URLs to include as sources. | [optional] 
**asset_ids** | **List[str]** | Workspace asset IDs to include as sources. | [optional] 
**knowledge_base_ids** | **List[str]** | Knowledge base IDs to include as sources. | [optional] 
**knowledge_base_item_ids** | **List[str]** | Knowledge base item IDs to include as sources. | [optional] 

## Example

```python
from fetch_hive_sdk.models.hive_agent_sources import HiveAgentSources

# TODO update the JSON string below
json = "{}"
# create an instance of HiveAgentSources from a JSON string
hive_agent_sources_instance = HiveAgentSources.from_json(json)
# print the JSON string representation of the object
print(HiveAgentSources.to_json())

# convert the object into a dict
hive_agent_sources_dict = hive_agent_sources_instance.to_dict()
# create an instance of HiveAgentSources from a dict
hive_agent_sources_from_dict = HiveAgentSources.from_dict(hive_agent_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


