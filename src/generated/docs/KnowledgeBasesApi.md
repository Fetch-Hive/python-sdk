# fetch_hive_sdk.KnowledgeBasesApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_public_workspaces_knowledge_bases**](KnowledgeBasesApi.md#delete_public_workspaces_knowledge_bases) | **DELETE** /public/workspaces/{workspace_id}/knowledge_bases/{id} | Delete a knowledge base
[**get_public_workspaces_knowledge_bases**](KnowledgeBasesApi.md#get_public_workspaces_knowledge_bases) | **GET** /public/workspaces/{workspace_id}/knowledge_bases | List public workspace knowledge bases
[**get_public_workspaces_knowledge_bases2**](KnowledgeBasesApi.md#get_public_workspaces_knowledge_bases2) | **GET** /public/workspaces/{workspace_id}/knowledge_bases/{id} | Get a knowledge base
[**patch_public_workspaces_knowledge_bases**](KnowledgeBasesApi.md#patch_public_workspaces_knowledge_bases) | **PATCH** /public/workspaces/{workspace_id}/knowledge_bases/{id} | Update a knowledge base
[**post_public_workspaces_knowledge_bases**](KnowledgeBasesApi.md#post_public_workspaces_knowledge_bases) | **POST** /public/workspaces/{workspace_id}/knowledge_bases | Create a knowledge base
[**post_public_workspaces_knowledge_bases_search**](KnowledgeBasesApi.md#post_public_workspaces_knowledge_bases_search) | **POST** /public/workspaces/{workspace_id}/knowledge_bases/{id}/search | Search a knowledge base


# **delete_public_workspaces_knowledge_bases**
> DeletePublicWorkspacesKnowledgeBases200Response delete_public_workspaces_knowledge_bases(workspace_id, id)

Delete a knowledge base

Marks a knowledge base for deletion. Cleanup continues asynchronously in the background.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.delete_public_workspaces_knowledge_bases200_response import DeletePublicWorkspacesKnowledgeBases200Response
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
        api_response = api_instance.delete_public_workspaces_knowledge_bases(workspace_id, id)
        print("The response of KnowledgeBasesApi->delete_public_workspaces_knowledge_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->delete_public_workspaces_knowledge_bases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Knowledge base UUID | 

### Return type

[**DeletePublicWorkspacesKnowledgeBases200Response**](DeletePublicWorkspacesKnowledgeBases200Response.md)

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

# **get_public_workspaces_knowledge_bases**
> GetPublicWorkspacesKnowledgeBases200Response get_public_workspaces_knowledge_bases(workspace_id)

List public workspace knowledge bases

Returns knowledge bases scoped to the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_knowledge_bases200_response import GetPublicWorkspacesKnowledgeBases200Response
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
        api_response = api_instance.get_public_workspaces_knowledge_bases(workspace_id)
        print("The response of KnowledgeBasesApi->get_public_workspaces_knowledge_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_public_workspaces_knowledge_bases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 

### Return type

[**GetPublicWorkspacesKnowledgeBases200Response**](GetPublicWorkspacesKnowledgeBases200Response.md)

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

# **get_public_workspaces_knowledge_bases2**
> GetPublicWorkspacesKnowledgeBases2200Response get_public_workspaces_knowledge_bases2(workspace_id, id)

Get a knowledge base

Returns a single active knowledge base belonging to the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_knowledge_bases2200_response import GetPublicWorkspacesKnowledgeBases2200Response
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
        api_response = api_instance.get_public_workspaces_knowledge_bases2(workspace_id, id)
        print("The response of KnowledgeBasesApi->get_public_workspaces_knowledge_bases2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_public_workspaces_knowledge_bases2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Knowledge base UUID | 

### Return type

[**GetPublicWorkspacesKnowledgeBases2200Response**](GetPublicWorkspacesKnowledgeBases2200Response.md)

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

# **patch_public_workspaces_knowledge_bases**
> PatchPublicWorkspacesKnowledgeBases200Response patch_public_workspaces_knowledge_bases(workspace_id, id, patch_public_workspaces_knowledge_bases_request)

Update a knowledge base

Updates name, description, or search settings of an existing knowledge base.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.patch_public_workspaces_knowledge_bases200_response import PatchPublicWorkspacesKnowledgeBases200Response
from fetch_hive_sdk.models.patch_public_workspaces_knowledge_bases_request import PatchPublicWorkspacesKnowledgeBasesRequest
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
    patch_public_workspaces_knowledge_bases_request = fetch_hive_sdk.PatchPublicWorkspacesKnowledgeBasesRequest() # PatchPublicWorkspacesKnowledgeBasesRequest | 

    try:
        # Update a knowledge base
        api_response = api_instance.patch_public_workspaces_knowledge_bases(workspace_id, id, patch_public_workspaces_knowledge_bases_request)
        print("The response of KnowledgeBasesApi->patch_public_workspaces_knowledge_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->patch_public_workspaces_knowledge_bases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Knowledge base UUID | 
 **patch_public_workspaces_knowledge_bases_request** | [**PatchPublicWorkspacesKnowledgeBasesRequest**](PatchPublicWorkspacesKnowledgeBasesRequest.md)|  | 

### Return type

[**PatchPublicWorkspacesKnowledgeBases200Response**](PatchPublicWorkspacesKnowledgeBases200Response.md)

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

# **post_public_workspaces_knowledge_bases**
> PostPublicWorkspacesKnowledgeBases200Response post_public_workspaces_knowledge_bases(workspace_id, post_public_workspaces_knowledge_bases_request)

Create a knowledge base

Creates a new knowledge base in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases200_response import PostPublicWorkspacesKnowledgeBases200Response
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_request import PostPublicWorkspacesKnowledgeBasesRequest
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
    post_public_workspaces_knowledge_bases_request = fetch_hive_sdk.PostPublicWorkspacesKnowledgeBasesRequest() # PostPublicWorkspacesKnowledgeBasesRequest | 

    try:
        # Create a knowledge base
        api_response = api_instance.post_public_workspaces_knowledge_bases(workspace_id, post_public_workspaces_knowledge_bases_request)
        print("The response of KnowledgeBasesApi->post_public_workspaces_knowledge_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->post_public_workspaces_knowledge_bases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **post_public_workspaces_knowledge_bases_request** | [**PostPublicWorkspacesKnowledgeBasesRequest**](PostPublicWorkspacesKnowledgeBasesRequest.md)|  | 

### Return type

[**PostPublicWorkspacesKnowledgeBases200Response**](PostPublicWorkspacesKnowledgeBases200Response.md)

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

# **post_public_workspaces_knowledge_bases_search**
> PostPublicWorkspacesKnowledgeBasesSearch200Response post_public_workspaces_knowledge_bases_search(workspace_id, id, post_public_workspaces_knowledge_bases_search_request)

Search a knowledge base

Performs a vector, full-text, or hybrid search against the knowledge base.
Returns matching chunks above the configured score threshold.


### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_search200_response import PostPublicWorkspacesKnowledgeBasesSearch200Response
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_search_request import PostPublicWorkspacesKnowledgeBasesSearchRequest
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
    post_public_workspaces_knowledge_bases_search_request = fetch_hive_sdk.PostPublicWorkspacesKnowledgeBasesSearchRequest() # PostPublicWorkspacesKnowledgeBasesSearchRequest | 

    try:
        # Search a knowledge base
        api_response = api_instance.post_public_workspaces_knowledge_bases_search(workspace_id, id, post_public_workspaces_knowledge_bases_search_request)
        print("The response of KnowledgeBasesApi->post_public_workspaces_knowledge_bases_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->post_public_workspaces_knowledge_bases_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Knowledge base UUID | 
 **post_public_workspaces_knowledge_bases_search_request** | [**PostPublicWorkspacesKnowledgeBasesSearchRequest**](PostPublicWorkspacesKnowledgeBasesSearchRequest.md)|  | 

### Return type

[**PostPublicWorkspacesKnowledgeBasesSearch200Response**](PostPublicWorkspacesKnowledgeBasesSearch200Response.md)

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

