# fetch_hive_sdk.KnowledgeBaseItemsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_public_workspaces_knowledge_bases_items**](KnowledgeBaseItemsApi.md#delete_public_workspaces_knowledge_bases_items) | **DELETE** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id} | Delete a knowledge base item
[**get_public_workspaces_knowledge_bases_items**](KnowledgeBaseItemsApi.md#get_public_workspaces_knowledge_bases_items) | **GET** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items | List public workspace knowledge base items
[**get_public_workspaces_knowledge_bases_items2**](KnowledgeBaseItemsApi.md#get_public_workspaces_knowledge_bases_items2) | **GET** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id} | Get a knowledge base item
[**patch_public_workspaces_knowledge_bases_items**](KnowledgeBaseItemsApi.md#patch_public_workspaces_knowledge_bases_items) | **PATCH** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id} | Update a knowledge base item
[**post_public_workspaces_knowledge_bases_items**](KnowledgeBaseItemsApi.md#post_public_workspaces_knowledge_bases_items) | **POST** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items | Create a knowledge base item
[**post_public_workspaces_knowledge_bases_items_regenerate**](KnowledgeBaseItemsApi.md#post_public_workspaces_knowledge_bases_items_regenerate) | **POST** /public/workspaces/{workspace_id}/knowledge_bases/{knowledge_base_id}/items/{id}/regenerate | Regenerate a knowledge base item


# **delete_public_workspaces_knowledge_bases_items**
> DeletePublicWorkspacesKnowledgeBasesItems200Response delete_public_workspaces_knowledge_bases_items(workspace_id, knowledge_base_id, id)

Delete a knowledge base item

Destroys a knowledge base item in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.delete_public_workspaces_knowledge_bases_items200_response import DeletePublicWorkspacesKnowledgeBasesItems200Response
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
        api_response = api_instance.delete_public_workspaces_knowledge_bases_items(workspace_id, knowledge_base_id, id)
        print("The response of KnowledgeBaseItemsApi->delete_public_workspaces_knowledge_bases_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->delete_public_workspaces_knowledge_bases_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **id** | **UUID**| Knowledge base item UUID | 

### Return type

[**DeletePublicWorkspacesKnowledgeBasesItems200Response**](DeletePublicWorkspacesKnowledgeBasesItems200Response.md)

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

# **get_public_workspaces_knowledge_bases_items**
> GetPublicWorkspacesKnowledgeBasesItems200Response get_public_workspaces_knowledge_bases_items(workspace_id, knowledge_base_id)

List public workspace knowledge base items

Returns items for a knowledge base in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_knowledge_bases_items200_response import GetPublicWorkspacesKnowledgeBasesItems200Response
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
        api_response = api_instance.get_public_workspaces_knowledge_bases_items(workspace_id, knowledge_base_id)
        print("The response of KnowledgeBaseItemsApi->get_public_workspaces_knowledge_bases_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->get_public_workspaces_knowledge_bases_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 

### Return type

[**GetPublicWorkspacesKnowledgeBasesItems200Response**](GetPublicWorkspacesKnowledgeBasesItems200Response.md)

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

# **get_public_workspaces_knowledge_bases_items2**
> GetPublicWorkspacesKnowledgeBasesItems2200Response get_public_workspaces_knowledge_bases_items2(workspace_id, knowledge_base_id, id)

Get a knowledge base item

Returns a single knowledge base item in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_knowledge_bases_items2200_response import GetPublicWorkspacesKnowledgeBasesItems2200Response
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
        api_response = api_instance.get_public_workspaces_knowledge_bases_items2(workspace_id, knowledge_base_id, id)
        print("The response of KnowledgeBaseItemsApi->get_public_workspaces_knowledge_bases_items2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->get_public_workspaces_knowledge_bases_items2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **id** | **UUID**| Knowledge base item UUID | 

### Return type

[**GetPublicWorkspacesKnowledgeBasesItems2200Response**](GetPublicWorkspacesKnowledgeBasesItems2200Response.md)

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

# **patch_public_workspaces_knowledge_bases_items**
> PatchPublicWorkspacesKnowledgeBasesItems200Response patch_public_workspaces_knowledge_bases_items(workspace_id, knowledge_base_id, id, patch_public_workspaces_knowledge_bases_items_request)

Update a knowledge base item

Updates an existing knowledge base item in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.patch_public_workspaces_knowledge_bases_items200_response import PatchPublicWorkspacesKnowledgeBasesItems200Response
from fetch_hive_sdk.models.patch_public_workspaces_knowledge_bases_items_request import PatchPublicWorkspacesKnowledgeBasesItemsRequest
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
    patch_public_workspaces_knowledge_bases_items_request = fetch_hive_sdk.PatchPublicWorkspacesKnowledgeBasesItemsRequest() # PatchPublicWorkspacesKnowledgeBasesItemsRequest | 

    try:
        # Update a knowledge base item
        api_response = api_instance.patch_public_workspaces_knowledge_bases_items(workspace_id, knowledge_base_id, id, patch_public_workspaces_knowledge_bases_items_request)
        print("The response of KnowledgeBaseItemsApi->patch_public_workspaces_knowledge_bases_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->patch_public_workspaces_knowledge_bases_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **id** | **UUID**| Knowledge base item UUID | 
 **patch_public_workspaces_knowledge_bases_items_request** | [**PatchPublicWorkspacesKnowledgeBasesItemsRequest**](PatchPublicWorkspacesKnowledgeBasesItemsRequest.md)|  | 

### Return type

[**PatchPublicWorkspacesKnowledgeBasesItems200Response**](PatchPublicWorkspacesKnowledgeBasesItems200Response.md)

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

# **post_public_workspaces_knowledge_bases_items**
> PostPublicWorkspacesKnowledgeBasesItems200Response post_public_workspaces_knowledge_bases_items(workspace_id, knowledge_base_id, post_public_workspaces_knowledge_bases_items_request)

Create a knowledge base item

Creates a new item in a knowledge base in the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_items200_response import PostPublicWorkspacesKnowledgeBasesItems200Response
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_items_request import PostPublicWorkspacesKnowledgeBasesItemsRequest
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
    post_public_workspaces_knowledge_bases_items_request = fetch_hive_sdk.PostPublicWorkspacesKnowledgeBasesItemsRequest() # PostPublicWorkspacesKnowledgeBasesItemsRequest | 

    try:
        # Create a knowledge base item
        api_response = api_instance.post_public_workspaces_knowledge_bases_items(workspace_id, knowledge_base_id, post_public_workspaces_knowledge_bases_items_request)
        print("The response of KnowledgeBaseItemsApi->post_public_workspaces_knowledge_bases_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->post_public_workspaces_knowledge_bases_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **post_public_workspaces_knowledge_bases_items_request** | [**PostPublicWorkspacesKnowledgeBasesItemsRequest**](PostPublicWorkspacesKnowledgeBasesItemsRequest.md)|  | 

### Return type

[**PostPublicWorkspacesKnowledgeBasesItems200Response**](PostPublicWorkspacesKnowledgeBasesItems200Response.md)

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

# **post_public_workspaces_knowledge_bases_items_regenerate**
> PostPublicWorkspacesKnowledgeBasesItemsRegenerate200Response post_public_workspaces_knowledge_bases_items_regenerate(workspace_id, knowledge_base_id, id)

Regenerate a knowledge base item

Enqueues a background job to re-fetch and re-embed the knowledge base item. Returns a request_id for async tracking.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.post_public_workspaces_knowledge_bases_items_regenerate200_response import PostPublicWorkspacesKnowledgeBasesItemsRegenerate200Response
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
        api_response = api_instance.post_public_workspaces_knowledge_bases_items_regenerate(workspace_id, knowledge_base_id, id)
        print("The response of KnowledgeBaseItemsApi->post_public_workspaces_knowledge_bases_items_regenerate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseItemsApi->post_public_workspaces_knowledge_bases_items_regenerate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **knowledge_base_id** | **UUID**| Knowledge base UUID | 
 **id** | **UUID**| Knowledge base item UUID | 

### Return type

[**PostPublicWorkspacesKnowledgeBasesItemsRegenerate200Response**](PostPublicWorkspacesKnowledgeBasesItemsRegenerate200Response.md)

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

