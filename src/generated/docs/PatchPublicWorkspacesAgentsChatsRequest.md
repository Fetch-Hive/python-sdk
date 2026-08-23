# PatchPublicWorkspacesAgentsChatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**PatchPublicWorkspacesAgentsChatsRequestChat**](PatchPublicWorkspacesAgentsChatsRequestChat.md) |  | 

## Example

```python
from fetch_hive_sdk.models.patch_public_workspaces_agents_chats_request import PatchPublicWorkspacesAgentsChatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPublicWorkspacesAgentsChatsRequest from a JSON string
patch_public_workspaces_agents_chats_request_instance = PatchPublicWorkspacesAgentsChatsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchPublicWorkspacesAgentsChatsRequest.to_json())

# convert the object into a dict
patch_public_workspaces_agents_chats_request_dict = patch_public_workspaces_agents_chats_request_instance.to_dict()
# create an instance of PatchPublicWorkspacesAgentsChatsRequest from a dict
patch_public_workspaces_agents_chats_request_from_dict = PatchPublicWorkspacesAgentsChatsRequest.from_dict(patch_public_workspaces_agents_chats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


