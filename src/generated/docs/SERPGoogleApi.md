# fetch_hive_sdk.SERPGoogleApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_serp_google_languages_get**](SERPGoogleApi.md#v1_serp_google_languages_get) | **GET** /v1/serp/google/languages | List Google SERP languages
[**v1_serp_google_locations_get**](SERPGoogleApi.md#v1_serp_google_locations_get) | **GET** /v1/serp/google/locations | List Google SERP locations


# **v1_serp_google_languages_get**
> List[object] v1_serp_google_languages_get()

List Google SERP languages

Returns all available language codes for Google SERP queries.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
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
    api_instance = fetch_hive_sdk.SERPGoogleApi(api_client)

    try:
        # List Google SERP languages
        api_response = api_instance.v1_serp_google_languages_get()
        print("The response of SERPGoogleApi->v1_serp_google_languages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPGoogleApi->v1_serp_google_languages_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | languages returned |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_serp_google_locations_get**
> List[object] v1_serp_google_locations_get()

List Google SERP locations

Returns all available geographic targeting locations for Google SERP queries.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
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
    api_instance = fetch_hive_sdk.SERPGoogleApi(api_client)

    try:
        # List Google SERP locations
        api_response = api_instance.v1_serp_google_locations_get()
        print("The response of SERPGoogleApi->v1_serp_google_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SERPGoogleApi->v1_serp_google_locations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | locations returned |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

