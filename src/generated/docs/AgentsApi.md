# fetch_hive_sdk.AgentsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoke_agent**](AgentsApi.md#invoke_agent) | **POST** /agent/invoke | Invoke an agent


# **invoke_agent**
> InvokeAgentResponse invoke_agent(invoke_agent_request)

Invoke an agent

Sends a message to a configured agent and returns its response.
Agents can use tools, maintain conversation history via `thread_id`,
or accept ephemeral history via the `messages` field.

Set `streaming: true` to receive a Server-Sent Events stream. Each
`data:` line contains a JSON object of type `SseChunk`.

Image URLs can be supplied in `image_urls` for multimodal inputs
(must be HTTPS).


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

