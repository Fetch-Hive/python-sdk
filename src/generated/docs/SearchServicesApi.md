# fetch_hive_sdk.SearchServicesApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_search_services_countries**](SearchServicesApi.md#get_public_search_services_countries) | **GET** /public/search_services/countries | List public search-service country catalogs
[**get_public_search_services_countries2**](SearchServicesApi.md#get_public_search_services_countries2) | **GET** /public/search_services/{service}/countries | Retrieve public search-service country catalog


# **get_public_search_services_countries**
> GetPublicSearchServicesCountries200Response get_public_search_services_countries()

List public search-service country catalogs

Returns the country catalogs used by public search workflow services.
This endpoint is unauthenticated and exposes the value each service expects for location/country configuration.


### Example


```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_search_services_countries200_response import GetPublicSearchServicesCountries200Response
from fetch_hive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fetchhive.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fetch_hive_sdk.Configuration(
    host = "https://api.fetchhive.com/v1"
)


# Enter a context with an instance of the API client
with fetch_hive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetch_hive_sdk.SearchServicesApi(api_client)

    try:
        # List public search-service country catalogs
        api_response = api_instance.get_public_search_services_countries()
        print("The response of SearchServicesApi->get_public_search_services_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchServicesApi->get_public_search_services_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPublicSearchServicesCountries200Response**](GetPublicSearchServicesCountries200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | country catalogs returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_search_services_countries2**
> GetPublicSearchServicesCountries200ResponseServicesInner get_public_search_services_countries2(service)

Retrieve public search-service country catalog

Returns the country catalog for one supported search workflow service.
Use each country object's `value` field when configuring that service.


### Example


```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_search_services_countries200_response_services_inner import GetPublicSearchServicesCountries200ResponseServicesInner
from fetch_hive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fetchhive.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fetch_hive_sdk.Configuration(
    host = "https://api.fetchhive.com/v1"
)


# Enter a context with an instance of the API client
with fetch_hive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetch_hive_sdk.SearchServicesApi(api_client)
    service = 'service_example' # str | Search workflow service key.

    try:
        # Retrieve public search-service country catalog
        api_response = api_instance.get_public_search_services_countries2(service)
        print("The response of SearchServicesApi->get_public_search_services_countries2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchServicesApi->get_public_search_services_countries2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Search workflow service key. | 

### Return type

[**GetPublicSearchServicesCountries200ResponseServicesInner**](GetPublicSearchServicesCountries200ResponseServicesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bing Search country catalog returned |  -  |
**404** | unsupported service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

