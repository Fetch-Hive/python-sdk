# fetch_hive_sdk.AgentsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_public_workspaces_agents**](AgentsApi.md#delete_public_workspaces_agents) | **DELETE** /public/workspaces/{workspace_id}/agents/{id} | Delete an agent
[**get_public_workspaces_agents**](AgentsApi.md#get_public_workspaces_agents) | **GET** /public/workspaces/{workspace_id}/agents/{id} | Get an agent
[**get_public_workspaces_agents2**](AgentsApi.md#get_public_workspaces_agents2) | **GET** /public/workspaces/{workspace_id}/agents | List public workspace agents
[**invoke_agent**](AgentsApi.md#invoke_agent) | **POST** /agent/invoke | Invoke an agent
[**patch_public_workspaces_agents**](AgentsApi.md#patch_public_workspaces_agents) | **PATCH** /public/workspaces/{workspace_id}/agents/{id} | Update an agent
[**post_public_workspaces_agents**](AgentsApi.md#post_public_workspaces_agents) | **POST** /public/workspaces/{workspace_id}/agents | Create an agent


# **delete_public_workspaces_agents**
> DeletePublicWorkspacesAgents200Response delete_public_workspaces_agents(workspace_id, id)

Delete an agent

Destroys the agent record.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.delete_public_workspaces_agents200_response import DeletePublicWorkspacesAgents200Response
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
    api_instance = fetch_hive_sdk.AgentsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID

    try:
        # Delete an agent
        api_response = api_instance.delete_public_workspaces_agents(workspace_id, id)
        print("The response of AgentsApi->delete_public_workspaces_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_public_workspaces_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Agent UUID | 

### Return type

[**DeletePublicWorkspacesAgents200Response**](DeletePublicWorkspacesAgents200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | agent deleted |  -  |
**401** | unauthorized |  -  |
**422** | agent not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_workspaces_agents**
> GetPublicWorkspacesAgents200Response get_public_workspaces_agents(workspace_id, id)

Get an agent

Returns a single active agent belonging to the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_agents200_response import GetPublicWorkspacesAgents200Response
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
    api_instance = fetch_hive_sdk.AgentsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID

    try:
        # Get an agent
        api_response = api_instance.get_public_workspaces_agents(workspace_id, id)
        print("The response of AgentsApi->get_public_workspaces_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_public_workspaces_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Agent UUID | 

### Return type

[**GetPublicWorkspacesAgents200Response**](GetPublicWorkspacesAgents200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | agent returned |  -  |
**401** | unauthorized |  -  |
**404** | workspace not found |  -  |
**422** | agent not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_workspaces_agents2**
> GetPublicWorkspacesAgents2200Response get_public_workspaces_agents2(workspace_id)

List public workspace agents

Returns standalone agents scoped to the requested public API workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_agents2200_response import GetPublicWorkspacesAgents2200Response
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
    api_instance = fetch_hive_sdk.AgentsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID

    try:
        # List public workspace agents
        api_response = api_instance.get_public_workspaces_agents2(workspace_id)
        print("The response of AgentsApi->get_public_workspaces_agents2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_public_workspaces_agents2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 

### Return type

[**GetPublicWorkspacesAgents2200Response**](GetPublicWorkspacesAgents2200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | agents returned |  -  |
**401** | unauthorized |  -  |
**404** | workspace not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_agent**
> InvokeAgentResponse invoke_agent(invoke_agent_request)

Invoke an agent

Sends a message to a configured agent and returns its response.
Agents can use tools, maintain conversation history via `thread_id`,
or accept ephemeral history via the `messages` field.

Set `streaming: true` to receive a Server-Sent Events stream. Each
`data:` line contains a JSON object of type `SseChunk`.

Documents and image URLs can be supplied in `attachments`. Existing
account Assets can be discovered through `known_artifact_refs` and
explicitly selected through `artifact_refs`.


### Example

* Bearer Authentication (BearerAuth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.invoke_agent_request import InvokeAgentRequest
from fetch_hive_sdk.models.invoke_agent_response import InvokeAgentResponse
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

# Configure Bearer authorization: BearerAuth
configuration = fetch_hive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fetch_hive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetch_hive_sdk.AgentsApi(api_client)
    invoke_agent_request = fetch_hive_sdk.InvokeAgentRequest() # InvokeAgentRequest | 

    try:
        # Invoke an agent
        api_response = api_instance.invoke_agent(invoke_agent_request)
        print("The response of AgentsApi->invoke_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->invoke_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoke_agent_request** | [**InvokeAgentRequest**](InvokeAgentRequest.md)|  | 

### Return type

[**InvokeAgentResponse**](InvokeAgentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent response. When &#x60;streaming&#x60; is &#x60;false&#x60; this is a single JSON object. When &#x60;streaming&#x60; is &#x60;true&#x60; the response is a &#x60;text/event-stream&#x60; where each &#x60;data:&#x60; line contains an &#x60;SseChunk&#x60;.  |  -  |
**400** | Invalid request body or parameters. |  -  |
**401** | Missing or invalid API token. |  -  |
**500** | Unexpected server-side error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_public_workspaces_agents**
> PatchPublicWorkspacesAgents200Response patch_public_workspaces_agents(workspace_id, id, patch_public_workspaces_agents_request)

Update an agent

Updates an existing agent in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.patch_public_workspaces_agents200_response import PatchPublicWorkspacesAgents200Response
from fetch_hive_sdk.models.patch_public_workspaces_agents_request import PatchPublicWorkspacesAgentsRequest
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
    api_instance = fetch_hive_sdk.AgentsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID
    patch_public_workspaces_agents_request = fetch_hive_sdk.PatchPublicWorkspacesAgentsRequest() # PatchPublicWorkspacesAgentsRequest | 

    try:
        # Update an agent
        api_response = api_instance.patch_public_workspaces_agents(workspace_id, id, patch_public_workspaces_agents_request)
        print("The response of AgentsApi->patch_public_workspaces_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->patch_public_workspaces_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **id** | **UUID**| Agent UUID | 
 **patch_public_workspaces_agents_request** | [**PatchPublicWorkspacesAgentsRequest**](PatchPublicWorkspacesAgentsRequest.md)|  | 

### Return type

[**PatchPublicWorkspacesAgents200Response**](PatchPublicWorkspacesAgents200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | agent updated |  -  |
**401** | unauthorized |  -  |
**404** | workspace not found |  -  |
**422** | agent not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_public_workspaces_agents**
> PostPublicWorkspacesAgents200Response post_public_workspaces_agents(workspace_id, post_public_workspaces_agents_request)

Create an agent

Creates a new agent in the requested workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.post_public_workspaces_agents200_response import PostPublicWorkspacesAgents200Response
from fetch_hive_sdk.models.post_public_workspaces_agents_request import PostPublicWorkspacesAgentsRequest
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
    api_instance = fetch_hive_sdk.AgentsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    post_public_workspaces_agents_request = fetch_hive_sdk.PostPublicWorkspacesAgentsRequest() # PostPublicWorkspacesAgentsRequest | 

    try:
        # Create an agent
        api_response = api_instance.post_public_workspaces_agents(workspace_id, post_public_workspaces_agents_request)
        print("The response of AgentsApi->post_public_workspaces_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->post_public_workspaces_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **post_public_workspaces_agents_request** | [**PostPublicWorkspacesAgentsRequest**](PostPublicWorkspacesAgentsRequest.md)|  | 

### Return type

[**PostPublicWorkspacesAgents200Response**](PostPublicWorkspacesAgents200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | agent created |  -  |
**401** | unauthorized |  -  |
**422** | invalid LLM model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

