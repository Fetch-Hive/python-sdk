# fetch_hive_sdk.HiveAgentsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoke_hive_agent**](HiveAgentsApi.md#invoke_hive_agent) | **POST** /hive-agent/invoke | Invoke a Hive Agent


# **invoke_hive_agent**
> InvokeHiveAgentResponse invoke_hive_agent(invoke_hive_agent_request)

Invoke a Hive Agent

Starts a Hive Agent run asynchronously and returns identifiers
immediately. Hive Agent invocation does not stream and does not wait
for the final answer in the HTTP response. A signed callback is sent
to `async.callback_url` when the run completes, fails, or is cancelled.

`async.enabled` must be `true` and `async.callback_url` is required.


### Example

* Bearer Authentication (BearerAuth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.invoke_hive_agent_request import InvokeHiveAgentRequest
from fetch_hive_sdk.models.invoke_hive_agent_response import InvokeHiveAgentResponse
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
    api_instance = fetch_hive_sdk.HiveAgentsApi(api_client)
    invoke_hive_agent_request = fetch_hive_sdk.InvokeHiveAgentRequest() # InvokeHiveAgentRequest | 

    try:
        # Invoke a Hive Agent
        api_response = api_instance.invoke_hive_agent(invoke_hive_agent_request)
        print("The response of HiveAgentsApi->invoke_hive_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HiveAgentsApi->invoke_hive_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoke_hive_agent_request** | [**InvokeHiveAgentRequest**](InvokeHiveAgentRequest.md)|  | 

### Return type

[**InvokeHiveAgentResponse**](InvokeHiveAgentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Hive Agent run queued for execution. |  -  |
**400** | Invalid request body or parameters. |  -  |
**401** | Missing or invalid API token. |  -  |
**500** | Unexpected server-side error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

