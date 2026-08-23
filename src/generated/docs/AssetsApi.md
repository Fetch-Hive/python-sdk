# fetch_hive_sdk.AssetsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_workspaces_workspace_id_assets_get**](AssetsApi.md#public_workspaces_workspace_id_assets_get) | **GET** /public/workspaces/{workspace_id}/assets | List public workspace assets
[**public_workspaces_workspace_id_assets_post**](AssetsApi.md#public_workspaces_workspace_id_assets_post) | **POST** /public/workspaces/{workspace_id}/assets | Upload a public workspace asset


# **public_workspaces_workspace_id_assets_get**
> PublicWorkspacesWorkspaceIdAssetsGet200Response public_workspaces_workspace_id_assets_get(workspace_id)

List public workspace assets

Returns assets scoped to the workspace attached to the public API key.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_assets_get200_response import PublicWorkspacesWorkspaceIdAssetsGet200Response
from fetch_hive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fetchhive.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fetch_hive_sdk.Configuration(
    host = "https://api.fetchhive.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer_auth
configuration = fetch_hive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fetch_hive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetch_hive_sdk.AssetsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID

    try:
        # List public workspace assets
        api_response = api_instance.public_workspaces_workspace_id_assets_get(workspace_id)
        print("The response of AssetsApi->public_workspaces_workspace_id_assets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->public_workspaces_workspace_id_assets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdAssetsGet200Response**](PublicWorkspacesWorkspaceIdAssetsGet200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | assets returned |  -  |
**401** | unauthorized |  -  |
**404** | workspace not found for API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_assets_post**
> PublicWorkspacesWorkspaceIdAssetsPost200Response public_workspaces_workspace_id_assets_post(workspace_id)

Upload a public workspace asset

Uploads a file and creates a workspace-scoped Asset that can be used as a Hive Agent source.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_assets_post200_response import PublicWorkspacesWorkspaceIdAssetsPost200Response
from fetch_hive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fetchhive.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fetch_hive_sdk.Configuration(
    host = "https://api.fetchhive.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer_auth
configuration = fetch_hive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fetch_hive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetch_hive_sdk.AssetsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID

    try:
        # Upload a public workspace asset
        api_response = api_instance.public_workspaces_workspace_id_assets_post(workspace_id)
        print("The response of AssetsApi->public_workspaces_workspace_id_assets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->public_workspaces_workspace_id_assets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdAssetsPost200Response**](PublicWorkspacesWorkspaceIdAssetsPost200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | asset uploaded |  -  |
**422** | no file provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

