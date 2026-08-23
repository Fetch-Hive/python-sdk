# AgentAttachmentOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**file_url** | **str** |  | 
**file_name** | **str** |  | [optional] 
**file_type** | **str** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.agent_attachment_one_of import AgentAttachmentOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAttachmentOneOf from a JSON string
agent_attachment_one_of_instance = AgentAttachmentOneOf.from_json(json)
# print the JSON string representation of the object
print(AgentAttachmentOneOf.to_json())

# convert the object into a dict
agent_attachment_one_of_dict = agent_attachment_one_of_instance.to_dict()
# create an instance of AgentAttachmentOneOf from a dict
agent_attachment_one_of_from_dict = AgentAttachmentOneOf.from_dict(agent_attachment_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


