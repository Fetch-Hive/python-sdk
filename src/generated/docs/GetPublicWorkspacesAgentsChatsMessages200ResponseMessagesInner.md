# GetPublicWorkspacesAgentsChatsMessages200ResponseMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**content** | **str** | (value may be null) | [optional] 
**role** | **str** |  | 
**sent_at** | **datetime** |  | 
**chat_id** | **UUID** |  | 

## Example

```python
from fetch_hive_sdk.models.get_public_workspaces_agents_chats_messages200_response_messages_inner import GetPublicWorkspacesAgentsChatsMessages200ResponseMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicWorkspacesAgentsChatsMessages200ResponseMessagesInner from a JSON string
get_public_workspaces_agents_chats_messages200_response_messages_inner_instance = GetPublicWorkspacesAgentsChatsMessages200ResponseMessagesInner.from_json(json)
# print the JSON string representation of the object
print(GetPublicWorkspacesAgentsChatsMessages200ResponseMessagesInner.to_json())

# convert the object into a dict
get_public_workspaces_agents_chats_messages200_response_messages_inner_dict = get_public_workspaces_agents_chats_messages200_response_messages_inner_instance.to_dict()
# create an instance of GetPublicWorkspacesAgentsChatsMessages200ResponseMessagesInner from a dict
get_public_workspaces_agents_chats_messages200_response_messages_inner_from_dict = GetPublicWorkspacesAgentsChatsMessages200ResponseMessagesInner.from_dict(get_public_workspaces_agents_chats_messages200_response_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


