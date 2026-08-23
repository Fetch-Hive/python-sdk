# PostPublicWorkspacesAgentsChatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**PostPublicWorkspacesAgentsChatsRequestChat**](PostPublicWorkspacesAgentsChatsRequestChat.md) |  | 

## Example

```python
from fetch_hive_sdk.models.post_public_workspaces_agents_chats_request import PostPublicWorkspacesAgentsChatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesAgentsChatsRequest from a JSON string
post_public_workspaces_agents_chats_request_instance = PostPublicWorkspacesAgentsChatsRequest.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesAgentsChatsRequest.to_json())

# convert the object into a dict
post_public_workspaces_agents_chats_request_dict = post_public_workspaces_agents_chats_request_instance.to_dict()
# create an instance of PostPublicWorkspacesAgentsChatsRequest from a dict
post_public_workspaces_agents_chats_request_from_dict = PostPublicWorkspacesAgentsChatsRequest.from_dict(post_public_workspaces_agents_chats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


