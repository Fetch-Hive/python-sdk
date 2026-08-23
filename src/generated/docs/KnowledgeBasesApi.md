# fetch_hive_sdk.KnowledgeBasesApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_workspaces_workspace_id_knowledge_bases_get**](KnowledgeBasesApi.md#public_workspaces_workspace_id_knowledge_bases_get) | **GET** /public/workspaces/{workspace_id}/knowledge_bases | List public workspace knowledge bases
[**public_workspaces_workspace_id_knowledge_bases_id_delete**](KnowledgeBasesApi.md#public_workspaces_workspace_id_knowledge_bases_id_delete) | **DELETE** /public/workspaces/{workspace_id}/knowledge_bases/{id} | Delete a knowledge base
[**public_workspaces_workspace_id_knowledge_bases_id_get**](KnowledgeBasesApi.md#public_workspaces_workspace_id_knowledge_bases_id_get) | **GET** /public/workspaces/{workspace_id}/knowledge_bases/{id} | Get a knowledge base
[**public_workspaces_workspace_id_knowledge_bases_id_patch**](KnowledgeBasesApi.md#public_workspaces_workspace_id_knowledge_bases_id_patch) | **PATCH** /public/workspaces/{workspace_id}/knowledge_bases/{id} | Update a knowledge base
[**public_workspaces_workspace_id_knowledge_bases_id_search_post**](KnowledgeBasesApi.md#public_workspaces_workspace_id_knowledge_bases_id_search_post) | **POST** /public/workspaces/{workspace_id}/knowledge_bases/{id}/search | Search a knowledge base
[**public_workspaces_workspace_id_knowledge_bases_post**](KnowledgeBasesApi.md#public_workspaces_workspace_id_knowledge_bases_post) | **POST** /public/workspaces/{workspace_id}/knowledge_bases | Create a knowledge base


# **public_workspaces_workspace_id_knowledge_bases_get**
> PublicWorkspacesWorkspaceIdKnowledgeBasesGet200Response public_workspaces_workspace_id_knowledge_bases_get(workspace_id)

List public workspace knowledge bases

Returns knowledge bases scoped to the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_get200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesGet200Response
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
    api_instance = fetch_hive_sdk.KnowledgeBasesApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID

    try:
        # List public workspace knowledge bases
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_get(workspace_id)
        print("The response of KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesGet200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesGet200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | knowledge bases returned |  -  |
**401** | unauthorized |  -  |
**404** | workspace not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_id_delete**
> PublicWorkspacesWorkspaceIdKnowledgeBasesIdDelete200Response public_workspaces_workspace_id_knowledge_bases_id_delete(workspace_id, id)

Delete a knowledge base

Marks a knowledge base for deletion. Cleanup continues asynchronously in the background.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_id_delete200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesIdDelete200Response
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
    api_instance = fetch_hive_sdk.KnowledgeBasesApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID

    try:
        # Delete a knowledge base
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_id_delete(workspace_id, id)
        print("The response of KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Knowledge base UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesIdDelete200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesIdDelete200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | knowledge base marked for deletion |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_id_get**
> PublicWorkspacesWorkspaceIdKnowledgeBasesIdGet200Response public_workspaces_workspace_id_knowledge_bases_id_get(workspace_id, id)

Get a knowledge base

Returns a single active knowledge base belonging to the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_id_get200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesIdGet200Response
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
    api_instance = fetch_hive_sdk.KnowledgeBasesApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID

    try:
        # Get a knowledge base
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_id_get(workspace_id, id)
        print("The response of KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Knowledge base UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesIdGet200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesIdGet200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | knowledge base returned |  -  |
**401** | unauthorized |  -  |
**422** | knowledge base not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_id_patch**
> PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatch200Response public_workspaces_workspace_id_knowledge_bases_id_patch(workspace_id, id, public_workspaces_workspace_id_knowledge_bases_id_patch_request)

Update a knowledge base

Updates name, description, or search settings of an existing knowledge base.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_id_patch200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatch200Response
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_id_patch_request import PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest
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
    api_instance = fetch_hive_sdk.KnowledgeBasesApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID
    public_workspaces_workspace_id_knowledge_bases_id_patch_request = fetch_hive_sdk.PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest() # PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest | 

    try:
        # Update a knowledge base
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_id_patch(workspace_id, id, public_workspaces_workspace_id_knowledge_bases_id_patch_request)
        print("The response of KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Knowledge base UUID | 
 **public_workspaces_workspace_id_knowledge_bases_id_patch_request** | [**PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest**](PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatchRequest.md)|  | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatch200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesIdPatch200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | knowledge base updated |  -  |
**401** | unauthorized |  -  |
**422** | knowledge base not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_id_search_post**
> PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPost200Response public_workspaces_workspace_id_knowledge_bases_id_search_post(workspace_id, id, public_workspaces_workspace_id_knowledge_bases_id_search_post_request)

Search a knowledge base

Performs a vector, full-text, or hybrid search against the knowledge base.
Returns matching chunks above the configured score threshold.


### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_id_search_post200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPost200Response
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_id_search_post_request import PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest
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
    api_instance = fetch_hive_sdk.KnowledgeBasesApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID
    public_workspaces_workspace_id_knowledge_bases_id_search_post_request = fetch_hive_sdk.PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest() # PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest | 

    try:
        # Search a knowledge base
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_id_search_post(workspace_id, id, public_workspaces_workspace_id_knowledge_bases_id_search_post_request)
        print("The response of KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_id_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_id_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Knowledge base UUID | 
 **public_workspaces_workspace_id_knowledge_bases_id_search_post_request** | [**PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest**](PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPostRequest.md)|  | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPost200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesIdSearchPost200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results returned |  -  |
**401** | unauthorized |  -  |
**422** | invalid search type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_post**
> PublicWorkspacesWorkspaceIdKnowledgeBasesPost200Response public_workspaces_workspace_id_knowledge_bases_post(workspace_id, public_workspaces_workspace_id_knowledge_bases_post_request)

Create a knowledge base

Creates a new knowledge base in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_post200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesPost200Response
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_post_request import PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequest
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
    api_instance = fetch_hive_sdk.KnowledgeBasesApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    public_workspaces_workspace_id_knowledge_bases_post_request = fetch_hive_sdk.PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequest() # PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequest | 

    try:
        # Create a knowledge base
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_post(workspace_id, public_workspaces_workspace_id_knowledge_bases_post_request)
        print("The response of KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->public_workspaces_workspace_id_knowledge_bases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **public_workspaces_workspace_id_knowledge_bases_post_request** | [**PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequest**](PublicWorkspacesWorkspaceIdKnowledgeBasesPostRequest.md)|  | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesPost200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesPost200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | knowledge base created |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

