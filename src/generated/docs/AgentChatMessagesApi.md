# fetch_hive_sdk.AgentChatMessagesApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_workspaces_workspace_id_agents_agent_id_chats_chat_id_messages_get**](AgentChatMessagesApi.md#public_workspaces_workspace_id_agents_agent_id_chats_chat_id_messages_get) | **GET** /public/workspaces/{workspace_id}/agents/{agent_id}/chats/{chat_id}/messages | List messages in a chat


# **public_workspaces_workspace_id_agents_agent_id_chats_chat_id_messages_get**
> PublicWorkspacesWorkspaceIdAgentsAgentIdChatsChatIdMessagesGet200Response public_workspaces_workspace_id_agents_agent_id_chats_chat_id_messages_get(workspace_id, agent_id, chat_id)

List messages in a chat

Returns messages in the chat ordered chronologically (oldest first).

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_workspaces_workspace_id_agents_agent_id_chats_chat_id_messages_get200_response import PublicWorkspacesWorkspaceIdAgentsAgentIdChatsChatIdMessagesGet200Response
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
    api_instance = fetch_hive_sdk.AgentChatMessagesApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Workspace UUID
    agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Agent UUID
    chat_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Chat UUID

    try:
        # List messages in a chat
        api_response = api_instance.public_workspaces_workspace_id_agents_agent_id_chats_chat_id_messages_get(workspace_id, agent_id, chat_id)
        print("The response of AgentChatMessagesApi->public_workspaces_workspace_id_agents_agent_id_chats_chat_id_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentChatMessagesApi->public_workspaces_workspace_id_agents_agent_id_chats_chat_id_messages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**| Workspace UUID | 
 **agent_id** | **UUID**| Agent UUID | 
 **chat_id** | **UUID**| Chat UUID | 

### Return type

[**PublicWorkspacesWorkspaceIdAgentsAgentIdChatsChatIdMessagesGet200Response**](PublicWorkspacesWorkspaceIdAgentsAgentIdChatsChatIdMessagesGet200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | messages returned |  -  |
**401** | unauthorized |  -  |
**404** | workspace not found |  -  |
**422** | agent not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

