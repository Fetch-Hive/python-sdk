# fetch_hive_sdk.PromptsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoke_prompt**](PromptsApi.md#invoke_prompt) | **POST** /prompt/invoke | Invoke a prompt deployment


# **invoke_prompt**
> InvokePromptResponse invoke_prompt(invoke_prompt_request)

Invoke a prompt deployment

Runs a configured prompt deployment and returns the model response.
Set `streaming: true` to receive a Server-Sent Events stream instead
of a single JSON object.


### Example

* Bearer Authentication (BearerAuth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.invoke_prompt_request import InvokePromptRequest
from fetch_hive_sdk.models.invoke_prompt_response import InvokePromptResponse
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
    api_instance = fetch_hive_sdk.PromptsApi(api_client)
    invoke_prompt_request = fetch_hive_sdk.InvokePromptRequest() # InvokePromptRequest | 

    try:
        # Invoke a prompt deployment
        api_response = api_instance.invoke_prompt(invoke_prompt_request)
        print("The response of PromptsApi->invoke_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->invoke_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoke_prompt_request** | [**InvokePromptRequest**](InvokePromptRequest.md)|  | 

### Return type

[**InvokePromptResponse**](InvokePromptResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. When &#x60;streaming&#x60; is &#x60;false&#x60; (default) this is a single JSON object. When &#x60;streaming&#x60; is &#x60;true&#x60; the response is a &#x60;text/event-stream&#x60; where each &#x60;data:&#x60; line contains a JSON object of type &#x60;SseChunk&#x60;.  |  -  |
**400** | Invalid request body or parameters. |  -  |
**401** | Missing or invalid API token. |  -  |
**500** | Unexpected server-side error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

