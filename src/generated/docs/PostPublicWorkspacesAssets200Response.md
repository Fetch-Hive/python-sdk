# PostPublicWorkspacesAssets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**asset** | [**AssetObject**](AssetObject.md) |  | 

## Example

```python
from fetch_hive_sdk.models.post_public_workspaces_assets200_response import PostPublicWorkspacesAssets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesAssets200Response from a JSON string
post_public_workspaces_assets200_response_instance = PostPublicWorkspacesAssets200Response.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesAssets200Response.to_json())

# convert the object into a dict
post_public_workspaces_assets200_response_dict = post_public_workspaces_assets200_response_instance.to_dict()
# create an instance of PostPublicWorkspacesAssets200Response from a dict
post_public_workspaces_assets200_response_from_dict = PostPublicWorkspacesAssets200Response.from_dict(post_public_workspaces_assets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


