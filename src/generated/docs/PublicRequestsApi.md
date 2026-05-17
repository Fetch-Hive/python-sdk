# fetch_hive_sdk.PublicRequestsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_requests_id_get**](PublicRequestsApi.md#v1_requests_id_get) | **GET** /v1/requests/{id} | Get a request


# **v1_requests_id_get**
> V1RequestsIdGet200Response v1_requests_id_get(id)

Get a request

Returns a request record including its status, type, and timing metadata.
The `id` must be a valid `request_id` in `req_[32 hex chars]` format.


### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_requests_id_get200_response import V1RequestsIdGet200Response
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
    api_instance = fetch_hive_sdk.PublicRequestsApi(api_client)
    id = 'id_example' # str | Request ID (format: req_[32 hex chars])

    try:
        # Get a request
        api_response = api_instance.v1_requests_id_get(id)
        print("The response of PublicRequestsApi->v1_requests_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicRequestsApi->v1_requests_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Request ID (format: req_[32 hex chars]) | 

### Return type

[**V1RequestsIdGet200Response**](V1RequestsIdGet200Response.md)

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

