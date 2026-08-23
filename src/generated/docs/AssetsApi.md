# fetch_hive_sdk.AssetsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_workspaces_assets**](AssetsApi.md#get_public_workspaces_assets) | **GET** /public/workspaces/{workspace_id}/assets | List public workspace assets
[**post_public_workspaces_assets**](AssetsApi.md#post_public_workspaces_assets) | **POST** /public/workspaces/{workspace_id}/assets | Upload a public workspace asset


# **get_public_workspaces_assets**
> GetPublicWorkspacesAssets200Response get_public_workspaces_assets(workspace_id)

List public workspace assets

Returns assets scoped to the workspace attached to the public API key.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_assets200_response import GetPublicWorkspacesAssets200Response
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
        api_response = api_instance.get_public_workspaces_assets(workspace_id)
        print("The response of AssetsApi->get_public_workspaces_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_public_workspaces_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 

### Return type

[**GetPublicWorkspacesAssets200Response**](GetPublicWorkspacesAssets200Response.md)

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

# **post_public_workspaces_assets**
> PostPublicWorkspacesAssets200Response post_public_workspaces_assets(workspace_id)

Upload a public workspace asset

Uploads a file and creates a workspace-scoped Asset that can be used as a Hive Agent source.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.post_public_workspaces_assets200_response import PostPublicWorkspacesAssets200Response
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
        api_response = api_instance.post_public_workspaces_assets(workspace_id)
        print("The response of AssetsApi->post_public_workspaces_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->post_public_workspaces_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 

### Return type

[**PostPublicWorkspacesAssets200Response**](PostPublicWorkspacesAssets200Response.md)

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

