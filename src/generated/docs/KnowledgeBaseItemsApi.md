# fetch_hive_sdk.KnowledgeBaseItemsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_get**](KnowledgeBaseItemsApi.md#public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_get) | **GET** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items | List public workspace knowledge base items
[**public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_delete**](KnowledgeBaseItemsApi.md#public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_delete) | **DELETE** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id} | Delete a knowledge base item
[**public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_get**](KnowledgeBaseItemsApi.md#public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_get) | **GET** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id} | Get a knowledge base item
[**public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch**](KnowledgeBaseItemsApi.md#public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch) | **PATCH** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id} | Update a knowledge base item
[**public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_regenerate_post**](KnowledgeBaseItemsApi.md#public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_regenerate_post) | **POST** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id}/regenerate | Regenerate a knowledge base item
[**public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post**](KnowledgeBaseItemsApi.md#public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post) | **POST** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items | Create a knowledge base item


# **public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_get**
> PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsGet200Response public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_get(workspace_id, knowledge_base_id)

List public workspace knowledge base items

Returns items for a knowledge base in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_get200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsGet200Response
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
    api_instance = fetch_hive_sdk.KnowledgeBaseItemsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    knowledge_base_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID

    try:
        # List public workspace knowledge base items
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_get(workspace_id, knowledge_base_id)
        print("The response of KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsGet200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsGet200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | knowledge base items returned |  -  |
**401** | unauthorized |  -  |
**422** | knowledge base not found in workspace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_delete**
> PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdDelete200Response public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_delete(workspace_id, knowledge_base_id, id)

Delete a knowledge base item

Destroys a knowledge base item in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_delete200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdDelete200Response
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
    api_instance = fetch_hive_sdk.KnowledgeBaseItemsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    knowledge_base_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base item UUID

    try:
        # Delete a knowledge base item
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_delete(workspace_id, knowledge_base_id, id)
        print("The response of KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **id** | **UUID**| Knowledge base item UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdDelete200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdDelete200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | item deleted |  -  |
**401** | unauthorized |  -  |
**422** | item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_get**
> PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdGet200Response public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_get(workspace_id, knowledge_base_id, id)

Get a knowledge base item

Returns a single knowledge base item in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_get200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdGet200Response
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
    api_instance = fetch_hive_sdk.KnowledgeBaseItemsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    knowledge_base_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base item UUID

    try:
        # Get a knowledge base item
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_get(workspace_id, knowledge_base_id, id)
        print("The response of KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **id** | **UUID**| Knowledge base item UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdGet200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdGet200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | item returned |  -  |
**401** | unauthorized |  -  |
**422** | item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch**
> PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatch200Response public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch(workspace_id, knowledge_base_id, id, public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request)

Update a knowledge base item

Updates an existing knowledge base item in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatch200Response
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequest
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
    api_instance = fetch_hive_sdk.KnowledgeBaseItemsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    knowledge_base_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base item UUID
    public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request = fetch_hive_sdk.PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequest() # PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequest | 

    try:
        # Update a knowledge base item
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch(workspace_id, knowledge_base_id, id, public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request)
        print("The response of KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **id** | **UUID**| Knowledge base item UUID | 
 **public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_patch_request** | [**PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequest**](PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatchRequest.md)|  | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatch200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdPatch200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | item updated |  -  |
**401** | unauthorized |  -  |
**422** | item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_regenerate_post**
> PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdRegeneratePost200Response public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_regenerate_post(workspace_id, knowledge_base_id, id)

Regenerate a knowledge base item

Enqueues a background job to re-fetch and re-embed the knowledge base item. Returns a request_id for async tracking.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_regenerate_post200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdRegeneratePost200Response
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
    api_instance = fetch_hive_sdk.KnowledgeBaseItemsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    knowledge_base_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base item UUID

    try:
        # Regenerate a knowledge base item
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_regenerate_post(workspace_id, knowledge_base_id, id)
        print("The response of KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_regenerate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_id_regenerate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **id** | **UUID**| Knowledge base item UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdRegeneratePost200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsIdRegeneratePost200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | regeneration enqueued |  -  |
**401** | unauthorized |  -  |
**422** | item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post**
> PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPost200Response public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post(workspace_id, knowledge_base_id, public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request)

Create a knowledge base item

Creates a new item in a knowledge base in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post200_response import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPost200Response
from fetch_hive_sdk.models.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request import PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequest
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
    api_instance = fetch_hive_sdk.KnowledgeBaseItemsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    knowledge_base_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Knowledge base UUID
    public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request = fetch_hive_sdk.PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequest() # PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequest | 

    try:
        # Create a knowledge base item
        api_response = api_instance.public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post(workspace_id, knowledge_base_id, public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request)
        print("The response of KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **public_workspaces_workspace_id_knowledge_bases_knowledge_base_id_items_post_request** | [**PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequest**](PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPostRequest.md)|  | 

### Return type

[**PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPost200Response**](PublicWorkspacesWorkspaceIdKnowledgeBasesKnowledgeBaseIdItemsPost200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | item created |  -  |
**401** | unauthorized |  -  |
**422** | validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

