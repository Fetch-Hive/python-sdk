# fetch_hive_sdk.RequestsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_requests**](RequestsApi.md#get_public_requests) | **GET** /public/requests/{id} | Get a request


# **get_public_requests**
> GetPublicRequests200Response get_public_requests(id)

Get a request

Returns the status, type, and timing metadata for a run.

Pass the `request_id` returned when you invoked a prompt, workflow, agent, or Hive Agent.


### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_requests200_response import GetPublicRequests200Response
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
    api_instance = fetch_hive_sdk.RequestsApi(api_client)
    id = 'id_example' # str | Request ID from a Fetch Hive API response (for example, `req_019b1ad1193763f2367afc4cda5ab9df`).

    try:
        # Get a request
        api_response = api_instance.get_public_requests(id)
        print("The response of RequestsApi->get_public_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_public_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Request ID from a Fetch Hive API response (for example, &#x60;req_019b1ad1193763f2367afc4cda5ab9df&#x60;). | 

### Return type

[**GetPublicRequests200Response**](GetPublicRequests200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | request returned |  -  |
**401** | unauthorized |  -  |
**404** | request not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

