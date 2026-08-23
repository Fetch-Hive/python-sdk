# GetPublicWorkspacesAssets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[AssetObject]**](AssetObject.md) |  | 

## Example

```python
from fetch_hive_sdk.models.get_public_workspaces_assets200_response import GetPublicWorkspacesAssets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicWorkspacesAssets200Response from a JSON string
get_public_workspaces_assets200_response_instance = GetPublicWorkspacesAssets200Response.from_json(json)
# print the JSON string representation of the object
print(GetPublicWorkspacesAssets200Response.to_json())

# convert the object into a dict
get_public_workspaces_assets200_response_dict = get_public_workspaces_assets200_response_instance.to_dict()
# create an instance of GetPublicWorkspacesAssets200Response from a dict
get_public_workspaces_assets200_response_from_dict = GetPublicWorkspacesAssets200Response.from_dict(get_public_workspaces_assets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


