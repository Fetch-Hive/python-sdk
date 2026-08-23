# PostPublicWorkspacesAgentsChats200ResponseChat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** | (value may be null) | [optional] 
**last_message_content** | **str** | (value may be null) | [optional] 
**last_message_sent_at** | **datetime** | (value may be null) | [optional] 
**message_count** | **int** |  | 
**generated_at** | **datetime** |  | 
**status** | **str** |  | 
**agent** | **object** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.post_public_workspaces_agents_chats200_response_chat import PostPublicWorkspacesAgentsChats200ResponseChat

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesAgentsChats200ResponseChat from a JSON string
post_public_workspaces_agents_chats200_response_chat_instance = PostPublicWorkspacesAgentsChats200ResponseChat.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesAgentsChats200ResponseChat.to_json())

# convert the object into a dict
post_public_workspaces_agents_chats200_response_chat_dict = post_public_workspaces_agents_chats200_response_chat_instance.to_dict()
# create an instance of PostPublicWorkspacesAgentsChats200ResponseChat from a dict
post_public_workspaces_agents_chats200_response_chat_from_dict = PostPublicWorkspacesAgentsChats200ResponseChat.from_dict(post_public_workspaces_agents_chats200_response_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


