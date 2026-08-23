# fetch_hive_sdk.SearchServicesApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_search_services_countries_get**](SearchServicesApi.md#public_search_services_countries_get) | **GET** /public/search_services/countries | List public search-service country catalogs
[**public_search_services_service_countries_get**](SearchServicesApi.md#public_search_services_service_countries_get) | **GET** /public/search_services/{service}/countries | Retrieve public search-service country catalog


# **public_search_services_countries_get**
> PublicSearchServicesCountriesGet200Response public_search_services_countries_get()

List public search-service country catalogs

Returns the country catalogs used by public search workflow services.
This endpoint is unauthenticated and exposes the value each service expects for location/country configuration.


### Example


```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_search_services_countries_get200_response import PublicSearchServicesCountriesGet200Response
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
        api_response = api_instance.public_search_services_countries_get()
        print("The response of SearchServicesApi->public_search_services_countries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchServicesApi->public_search_services_countries_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicSearchServicesCountriesGet200Response**](PublicSearchServicesCountriesGet200Response.md)

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

# **public_search_services_service_countries_get**
> PublicSearchServicesCountriesGet200ResponseServicesInner public_search_services_service_countries_get(service)

Retrieve public search-service country catalog

Returns the country catalog for one supported search workflow service.
Use each country object's `value` field when configuring that service.


### Example


```python
import fetch_hive_sdk
from fetch_hive_sdk.models.public_search_services_countries_get200_response_services_inner import PublicSearchServicesCountriesGet200ResponseServicesInner
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
        api_response = api_instance.public_search_services_service_countries_get(service)
        print("The response of SearchServicesApi->public_search_services_service_countries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchServicesApi->public_search_services_service_countries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Search workflow service key. | 

### Return type

[**PublicSearchServicesCountriesGet200ResponseServicesInner**](PublicSearchServicesCountriesGet200ResponseServicesInner.md)

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

