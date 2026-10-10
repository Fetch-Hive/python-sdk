# fetch_hive_sdk.ToolActionApprovalsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_workspaces_tool_action_approvals**](ToolActionApprovalsApi.md#get_public_workspaces_tool_action_approvals) | **GET** /public/workspaces/{workspace_id}/tool_action_approvals | List tool action approvals
[**get_public_workspaces_tool_action_approvals2**](ToolActionApprovalsApi.md#get_public_workspaces_tool_action_approvals2) | **GET** /public/workspaces/{workspace_id}/tool_action_approvals/{id} | Show a tool action approval
[**post_public_workspaces_tool_action_approvals_decide**](ToolActionApprovalsApi.md#post_public_workspaces_tool_action_approvals_decide) | **POST** /public/workspaces/{workspace_id}/tool_action_approvals/{id}/decide | Decide a tool action approval


# **get_public_workspaces_tool_action_approvals**
> GetPublicWorkspacesToolActionApprovals200Response get_public_workspaces_tool_action_approvals(workspace_id, status=status, agent_id=agent_id, run_id=run_id, request_id=request_id, cursor=cursor, limit=limit)

List tool action approvals

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_tool_action_approvals200_response import GetPublicWorkspacesToolActionApprovals200Response
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
    api_instance = fetch_hive_sdk.ToolActionApprovalsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    status = 'status_example' # str |  (optional)
    agent_id = 'agent_id_example' # str |  (optional)
    run_id = 'run_id_example' # str |  (optional)
    request_id = 'request_id_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List tool action approvals
        api_response = api_instance.get_public_workspaces_tool_action_approvals(workspace_id, status=status, agent_id=agent_id, run_id=run_id, request_id=request_id, cursor=cursor, limit=limit)
        print("The response of ToolActionApprovalsApi->get_public_workspaces_tool_action_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolActionApprovalsApi->get_public_workspaces_tool_action_approvals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**|  | 
 **status** | **str**|  | [optional] 
 **agent_id** | **str**|  | [optional] 
 **run_id** | **str**|  | [optional] 
 **request_id** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**GetPublicWorkspacesToolActionApprovals200Response**](GetPublicWorkspacesToolActionApprovals200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | pending approvals for this workspace |  -  |
**404** | workspace is outside the API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_workspaces_tool_action_approvals2**
> GetPublicWorkspacesToolActionApprovals2200Response get_public_workspaces_tool_action_approvals2(workspace_id, id)

Show a tool action approval

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_workspaces_tool_action_approvals2200_response import GetPublicWorkspacesToolActionApprovals2200Response
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
    api_instance = fetch_hive_sdk.ToolActionApprovalsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Show a tool action approval
        api_response = api_instance.get_public_workspaces_tool_action_approvals2(workspace_id, id)
        print("The response of ToolActionApprovalsApi->get_public_workspaces_tool_action_approvals2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolActionApprovalsApi->get_public_workspaces_tool_action_approvals2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**|  | 
 **id** | **UUID**|  | 

### Return type

[**GetPublicWorkspacesToolActionApprovals2200Response**](GetPublicWorkspacesToolActionApprovals2200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | approval returned |  -  |
**404** | approval is in another workspace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_public_workspaces_tool_action_approvals_decide**
> post_public_workspaces_tool_action_approvals_decide(workspace_id, id, post_public_workspaces_tool_action_approvals_decide_request=post_public_workspaces_tool_action_approvals_decide_request)

Decide a tool action approval

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.post_public_workspaces_tool_action_approvals_decide_request import PostPublicWorkspacesToolActionApprovalsDecideRequest
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
    api_instance = fetch_hive_sdk.ToolActionApprovalsApi(api_client)
    workspace_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    post_public_workspaces_tool_action_approvals_decide_request = fetch_hive_sdk.PostPublicWorkspacesToolActionApprovalsDecideRequest() # PostPublicWorkspacesToolActionApprovalsDecideRequest |  (optional)

    try:
        # Decide a tool action approval
        api_instance.post_public_workspaces_tool_action_approvals_decide(workspace_id, id, post_public_workspaces_tool_action_approvals_decide_request=post_public_workspaces_tool_action_approvals_decide_request)
    except Exception as e:
        print("Exception when calling ToolActionApprovalsApi->post_public_workspaces_tool_action_approvals_decide: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **UUID**|  | 
 **id** | **UUID**|  | 
 **post_public_workspaces_tool_action_approvals_decide_request** | [**PostPublicWorkspacesToolActionApprovalsDecideRequest**](PostPublicWorkspacesToolActionApprovalsDecideRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | allow once records the API key |  -  |
**409** | approval was already decided |  -  |
**422** | a destructive action cannot be allowed for the whole run |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

