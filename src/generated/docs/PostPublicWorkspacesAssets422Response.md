# PostPublicWorkspacesAssets422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**message** | **str** |  | 
**error_code** | **str** |  | 

## Example

```python
from fetch_hive_sdk.models.post_public_workspaces_assets422_response import PostPublicWorkspacesAssets422Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostPublicWorkspacesAssets422Response from a JSON string
post_public_workspaces_assets422_response_instance = PostPublicWorkspacesAssets422Response.from_json(json)
# print the JSON string representation of the object
print(PostPublicWorkspacesAssets422Response.to_json())

# convert the object into a dict
post_public_workspaces_assets422_response_dict = post_public_workspaces_assets422_response_instance.to_dict()
# create an instance of PostPublicWorkspacesAssets422Response from a dict
post_public_workspaces_assets422_response_from_dict = PostPublicWorkspacesAssets422Response.from_dict(post_public_workspaces_assets422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


