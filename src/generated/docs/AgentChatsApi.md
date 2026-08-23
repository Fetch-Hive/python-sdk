# fetch_hive_sdk.AgentChatsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_public_workspaces_agents_chats**](AgentChatsApi.md#delete_public_workspaces_agents_chats) | **DELETE** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{id} | Delete a chat
[**get_public_workspaces_agents_chats**](AgentChatsApi.md#get_public_workspaces_agents_chats) | **GET** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{id} | Get a chat
[**patch_public_workspaces_agents_chats**](AgentChatsApi.md#patch_public_workspaces_agents_chats) | **PATCH** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{id} | Update a chat
[**patch_public_workspaces_agents_chats_clear_messages**](AgentChatsApi.md#patch_public_workspaces_agents_chats_clear_messages) | **PATCH** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{id}/clear_messages | Clear all messages in a chat
[**post_public_workspaces_agents_chats**](AgentChatsApi.md#post_public_workspaces_agents_chats) | **POST** /public/workspaces/{workspace_id}/agents/{agent_id}/chats | Create a chat


# **delete_public_workspaces_agents_chats**
> DeletePublicWorkspacesAgentsChats200Response delete_public_workspaces_agents_chats(workspace_id, agent_id, id)

Delete a chat

Permanently deletes a chat and all its messages.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.delete_public_workspaces_agents_chats200_response import DeletePublicWorkspacesAgentsChats200Response
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
    api_instance = fetch_hive_sdk.AgentChatsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Chat UUID

    try:
        # Delete a chat
        api_response = api_instance.delete_public_workspaces_agents_chats(workspace_id, agent_id, id)
        print("The response of AgentChatsApi->delete_public_workspaces_agents_chats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->delete_public_workspaces_agents_chats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **id** | **UUID**| Chat UUID | 

### Return type

[**DeletePublicWorkspacesAgentsChats200Response**](DeletePublicWorkspacesAgentsChats200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chat deleted |  -  |
**401** | unauthorized |  -  |
**404** | chat not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_workspaces_agents_chats**
> GetPublicWorkspacesAgentsChats200Response get_public_workspaces_agents_chats(workspace_id, agent_id, id)

Get a chat

Returns a single chat belonging to the agent in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_agents_chats200_response import GetPublicWorkspacesAgentsChats200Response
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
    api_instance = fetch_hive_sdk.AgentChatsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Chat UUID

    try:
        # Get a chat
        api_response = api_instance.get_public_workspaces_agents_chats(workspace_id, agent_id, id)
        print("The response of AgentChatsApi->get_public_workspaces_agents_chats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->get_public_workspaces_agents_chats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **id** | **UUID**| Chat UUID | 

### Return type

[**GetPublicWorkspacesAgentsChats200Response**](GetPublicWorkspacesAgentsChats200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chat returned |  -  |
**401** | unauthorized |  -  |
**404** | workspace not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_public_workspaces_agents_chats**
> PatchPublicWorkspacesAgentsChats200Response patch_public_workspaces_agents_chats(workspace_id, agent_id, id, patch_public_workspaces_agents_chats_request)

Update a chat

Updates a chat name in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.patch_public_workspaces_agents_chats200_response import PatchPublicWorkspacesAgentsChats200Response
from fetch_hive_sdk.models.patch_public_workspaces_agents_chats_request import PatchPublicWorkspacesAgentsChatsRequest
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
    api_instance = fetch_hive_sdk.AgentChatsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Chat UUID
    patch_public_workspaces_agents_chats_request = fetch_hive_sdk.PatchPublicWorkspacesAgentsChatsRequest() # PatchPublicWorkspacesAgentsChatsRequest | 

    try:
        # Update a chat
        api_response = api_instance.patch_public_workspaces_agents_chats(workspace_id, agent_id, id, patch_public_workspaces_agents_chats_request)
        print("The response of AgentChatsApi->patch_public_workspaces_agents_chats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->patch_public_workspaces_agents_chats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **id** | **UUID**| Chat UUID | 
 **patch_public_workspaces_agents_chats_request** | [**PatchPublicWorkspacesAgentsChatsRequest**](PatchPublicWorkspacesAgentsChatsRequest.md)|  | 

### Return type

[**PatchPublicWorkspacesAgentsChats200Response**](PatchPublicWorkspacesAgentsChats200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chat updated |  -  |
**401** | unauthorized |  -  |
**404** | chat not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_public_workspaces_agents_chats_clear_messages**
> PatchPublicWorkspacesAgentsChatsClearMessages200Response patch_public_workspaces_agents_chats_clear_messages(workspace_id, agent_id, id)

Clear all messages in a chat

Destroys all messages in the chat and resets the last message content.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.patch_public_workspaces_agents_chats_clear_messages200_response import PatchPublicWorkspacesAgentsChatsClearMessages200Response
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
    api_instance = fetch_hive_sdk.AgentChatsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Chat UUID

    try:
        # Clear all messages in a chat
        api_response = api_instance.patch_public_workspaces_agents_chats_clear_messages(workspace_id, agent_id, id)
        print("The response of AgentChatsApi->patch_public_workspaces_agents_chats_clear_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->patch_public_workspaces_agents_chats_clear_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **id** | **UUID**| Chat UUID | 

### Return type

[**PatchPublicWorkspacesAgentsChatsClearMessages200Response**](PatchPublicWorkspacesAgentsChatsClearMessages200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | messages cleared |  -  |
**401** | unauthorized |  -  |
**404** | chat not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_public_workspaces_agents_chats**
> PostPublicWorkspacesAgentsChats200Response post_public_workspaces_agents_chats(workspace_id, agent_id, post_public_workspaces_agents_chats_request)

Create a chat

Creates a new chat session for the agent in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.post_public_workspaces_agents_chats200_response import PostPublicWorkspacesAgentsChats200Response
from fetch_hive_sdk.models.post_public_workspaces_agents_chats_request import PostPublicWorkspacesAgentsChatsRequest
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
    api_instance = fetch_hive_sdk.AgentChatsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID
    post_public_workspaces_agents_chats_request = fetch_hive_sdk.PostPublicWorkspacesAgentsChatsRequest() # PostPublicWorkspacesAgentsChatsRequest | 

    try:
        # Create a chat
        api_response = api_instance.post_public_workspaces_agents_chats(workspace_id, agent_id, post_public_workspaces_agents_chats_request)
        print("The response of AgentChatsApi->post_public_workspaces_agents_chats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->post_public_workspaces_agents_chats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **post_public_workspaces_agents_chats_request** | [**PostPublicWorkspacesAgentsChatsRequest**](PostPublicWorkspacesAgentsChatsRequest.md)|  | 

### Return type

[**PostPublicWorkspacesAgentsChats200Response**](PostPublicWorkspacesAgentsChats200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chat created |  -  |
**401** | unauthorized |  -  |
**404** | workspace not found |  -  |
**422** | validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

