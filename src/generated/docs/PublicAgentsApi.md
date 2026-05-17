# fetch_hive_sdk.PublicAgentsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_agents_id_delete**](PublicAgentsApi.md#v1_agents_id_delete) | **DELETE** /v1/agents/{id} | Delete an agent
[**v1_agents_id_get**](PublicAgentsApi.md#v1_agents_id_get) | **GET** /v1/agents/{id} | Get an agent
[**v1_agents_post**](PublicAgentsApi.md#v1_agents_post) | **POST** /v1/agents | Create an agent


# **v1_agents_id_delete**
> V1AgentsIdDelete200Response v1_agents_id_delete(id)

Delete an agent

Destroys the agent record.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_agents_id_delete200_response import V1AgentsIdDelete200Response
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
    api_instance = fetch_hive_sdk.PublicAgentsApi(api_client)
    id = 'id_example' # str | Agent UUID

    try:
        # Delete an agent
        api_response = api_instance.v1_agents_id_delete(id)
        print("The response of PublicAgentsApi->v1_agents_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAgentsApi->v1_agents_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Agent UUID | 

### Return type

[**V1AgentsIdDelete200Response**](V1AgentsIdDelete200Response.md)

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

# **v1_agents_id_get**
> V1AgentsIdGet200Response v1_agents_id_get(id)

Get an agent

Returns a single active agent belonging to the authenticated account.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_agents_id_get200_response import V1AgentsIdGet200Response
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
    api_instance = fetch_hive_sdk.PublicAgentsApi(api_client)
    id = 'id_example' # str | Agent UUID

    try:
        # Get an agent
        api_response = api_instance.v1_agents_id_get(id)
        print("The response of PublicAgentsApi->v1_agents_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAgentsApi->v1_agents_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Agent UUID | 

### Return type

[**V1AgentsIdGet200Response**](V1AgentsIdGet200Response.md)

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
**422** | agent not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agents_post**
> V1AgentsPost200Response v1_agents_post(v1_agents_post_request)

Create an agent

Creates a new agent in the first workspace of the authenticated account.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_agents_post200_response import V1AgentsPost200Response
from fetch_hive_sdk.models.v1_agents_post_request import V1AgentsPostRequest
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
    api_instance = fetch_hive_sdk.PublicAgentsApi(api_client)
    v1_agents_post_request = fetch_hive_sdk.V1AgentsPostRequest() # V1AgentsPostRequest | 

    try:
        # Create an agent
        api_response = api_instance.v1_agents_post(v1_agents_post_request)
        print("The response of PublicAgentsApi->v1_agents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicAgentsApi->v1_agents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_agents_post_request** | [**V1AgentsPostRequest**](V1AgentsPostRequest.md)|  | 

### Return type

[**V1AgentsPost200Response**](V1AgentsPost200Response.md)

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

