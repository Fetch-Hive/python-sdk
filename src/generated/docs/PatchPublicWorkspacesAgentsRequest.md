# PatchPublicWorkspacesAgentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**PatchPublicWorkspacesAgentsRequestAgent**](PatchPublicWorkspacesAgentsRequestAgent.md) |  | 

## Example

```python
from fetch_hive_sdk.models.patch_public_workspaces_agents_request import PatchPublicWorkspacesAgentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPublicWorkspacesAgentsRequest from a JSON string
patch_public_workspaces_agents_request_instance = PatchPublicWorkspacesAgentsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchPublicWorkspacesAgentsRequest.to_json())

# convert the object into a dict
patch_public_workspaces_agents_request_dict = patch_public_workspaces_agents_request_instance.to_dict()
# create an instance of PatchPublicWorkspacesAgentsRequest from a dict
patch_public_workspaces_agents_request_from_dict = PatchPublicWorkspacesAgentsRequest.from_dict(patch_public_workspaces_agents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


