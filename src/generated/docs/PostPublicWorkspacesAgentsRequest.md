# PostPublicWorkspacesAgentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**PostPublicWorkspacesAgentsRequestAgent**](PostPublicWorkspacesAgentsRequestAgent.md) |  | 

## Example

```python
from fetch_hive_sdk.models.post_public_workspaces_agents_request import PostPublicWorkspacesAgentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesAgentsRequest from a JSON string
post_public_workspaces_agents_request_instance = PostPublicWorkspacesAgentsRequest.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesAgentsRequest.to_json())

# convert the object into a dict
post_public_workspaces_agents_request_dict = post_public_workspaces_agents_request_instance.to_dict()
# create an instance of PostPublicWorkspacesAgentsRequest from a dict
post_public_workspaces_agents_request_from_dict = PostPublicWorkspacesAgentsRequest.from_dict(post_public_workspaces_agents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


