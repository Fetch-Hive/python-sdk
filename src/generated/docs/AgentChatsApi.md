# fetch_hive_sdk.AgentChatsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_workspaces_workspace_id_agents_agent_id_chats_id_clear_messages_patch**](AgentChatsApi.md#public_workspaces_workspace_id_agents_agent_id_chats_id_clear_messages_patch) | **PATCH** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{id}/clear_messages | Clear all messages in a chat
[**public_workspaces_workspace_id_agents_agent_id_chats_id_delete**](AgentChatsApi.md#public_workspaces_workspace_id_agents_agent_id_chats_id_delete) | **DELETE** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{id} | Delete a chat
[**public_workspaces_workspace_id_agents_agent_id_chats_id_get**](AgentChatsApi.md#public_workspaces_workspace_id_agents_agent_id_chats_id_get) | **GET** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{id} | Get a chat
[**public_workspaces_workspace_id_agents_agent_id_chats_id_patch**](AgentChatsApi.md#public_workspaces_workspace_id_agents_agent_id_chats_id_patch) | **PATCH** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{id} | Update a chat
[**public_workspaces_workspace_id_agents_agent_id_chats_post**](AgentChatsApi.md#public_workspaces_workspace_id_agents_agent_id_chats_post) | **POST** /public/workspaces/{workspace_id}/agents/{agent_id}/chats | Create a chat


# **public_workspaces_workspace_id_agents_agent_id_chats_id_clear_messages_patch**
> PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdClearMessagesPatch200Response public_workspaces_workspace_id_agents_agent_id_chats_id_clear_messages_patch(workspace_id, agent_id, id)

Clear all messages in a chat

Destroys all messages in the chat and resets the last message content.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_agent_id_chats_id_clear_messages_patch200_response import PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdClearMessagesPatch200Response
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
        api_response = api_instance.public_workspaces_workspace_id_agents_agent_id_chats_id_clear_messages_patch(workspace_id, agent_id, id)
        print("The response of AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_id_clear_messages_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_id_clear_messages_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **id** | **UUID**| Chat UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdClearMessagesPatch200Response**](PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdClearMessagesPatch200Response.md)

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

# **public_workspaces_workspace_id_agents_agent_id_chats_id_delete**
> PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdDelete200Response public_workspaces_workspace_id_agents_agent_id_chats_id_delete(workspace_id, agent_id, id)

Delete a chat

Permanently deletes a chat and all its messages.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_agent_id_chats_id_delete200_response import PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdDelete200Response
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
        api_response = api_instance.public_workspaces_workspace_id_agents_agent_id_chats_id_delete(workspace_id, agent_id, id)
        print("The response of AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **id** | **UUID**| Chat UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdDelete200Response**](PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdDelete200Response.md)

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

# **public_workspaces_workspace_id_agents_agent_id_chats_id_get**
> PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdGet200Response public_workspaces_workspace_id_agents_agent_id_chats_id_get(workspace_id, agent_id, id)

Get a chat

Returns a single chat belonging to the agent in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_agent_id_chats_id_get200_response import PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdGet200Response
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
        api_response = api_instance.public_workspaces_workspace_id_agents_agent_id_chats_id_get(workspace_id, agent_id, id)
        print("The response of AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **id** | **UUID**| Chat UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdGet200Response**](PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdGet200Response.md)

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

# **public_workspaces_workspace_id_agents_agent_id_chats_id_patch**
> PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatch200Response public_workspaces_workspace_id_agents_agent_id_chats_id_patch(workspace_id, agent_id, id, public_workspaces_workspace_id_agents_agent_id_chats_id_patch_request)

Update a chat

Updates a chat name in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_agent_id_chats_id_patch200_response import PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatch200Response
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_agent_id_chats_id_patch_request import PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatchRequest
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
    public_workspaces_workspace_id_agents_agent_id_chats_id_patch_request = fetch_hive_sdk.PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatchRequest() # PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatchRequest | 

    try:
        # Update a chat
        api_response = api_instance.public_workspaces_workspace_id_agents_agent_id_chats_id_patch(workspace_id, agent_id, id, public_workspaces_workspace_id_agents_agent_id_chats_id_patch_request)
        print("The response of AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **id** | **UUID**| Chat UUID | 
 **public_workspaces_workspace_id_agents_agent_id_chats_id_patch_request** | [**PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatchRequest**](PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatchRequest.md)|  | 

### Return type

[**PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatch200Response**](PublicWorkspacesWorkspaceIdAgentsAgentIdChatsIdPatch200Response.md)

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

# **public_workspaces_workspace_id_agents_agent_id_chats_post**
> PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPost200Response public_workspaces_workspace_id_agents_agent_id_chats_post(workspace_id, agent_id, public_workspaces_workspace_id_agents_agent_id_chats_post_request)

Create a chat

Creates a new chat session for the agent in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_agent_id_chats_post200_response import PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPost200Response
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_agent_id_chats_post_request import PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPostRequest
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
    public_workspaces_workspace_id_agents_agent_id_chats_post_request = fetch_hive_sdk.PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPostRequest() # PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPostRequest | 

    try:
        # Create a chat
        api_response = api_instance.public_workspaces_workspace_id_agents_agent_id_chats_post(workspace_id, agent_id, public_workspaces_workspace_id_agents_agent_id_chats_post_request)
        print("The response of AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatsApi->public_workspaces_workspace_id_agents_agent_id_chats_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **public_workspaces_workspace_id_agents_agent_id_chats_post_request** | [**PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPostRequest**](PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPostRequest.md)|  | 

### Return type

[**PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPost200Response**](PublicWorkspacesWorkspaceIdAgentsAgentIdChatsPost200Response.md)

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

