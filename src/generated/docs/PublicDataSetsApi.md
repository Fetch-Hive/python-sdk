# fetch_hive_sdk.PublicDataSetsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_knowledge_bases_id_delete**](PublicDataSetsApi.md#v1_knowledge_bases_id_delete) | **DELETE** /v1/knowledge_bases/{id} | Delete a data set
[**v1_knowledge_bases_id_get**](PublicDataSetsApi.md#v1_knowledge_bases_id_get) | **GET** /v1/knowledge_bases/{id} | Get a data set
[**v1_knowledge_bases_id_patch**](PublicDataSetsApi.md#v1_knowledge_bases_id_patch) | **PATCH** /v1/knowledge_bases/{id} | Update a data set
[**v1_knowledge_bases_id_search_post**](PublicDataSetsApi.md#v1_knowledge_bases_id_search_post) | **POST** /v1/knowledge_bases/{id}/search | Search a data set
[**v1_knowledge_bases_post**](PublicDataSetsApi.md#v1_knowledge_bases_post) | **POST** /v1/knowledge_bases | Create a data set


# **v1_knowledge_bases_id_delete**
> V1KnowledgeBasesIdDelete200Response v1_knowledge_bases_id_delete(id)

Delete a data set

Marks a data set for deletion and enqueues a background job to clean it up.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_knowledge_bases_id_delete200_response import V1KnowledgeBasesIdDelete200Response
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
    api_instance = fetch_hive_sdk.PublicDataSetsApi(api_client)
    id = 'id_example' # str | Data set UUID

    try:
        # Delete a data set
        api_response = api_instance.v1_knowledge_bases_id_delete(id)
        print("The response of PublicDataSetsApi->v1_knowledge_bases_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicDataSetsApi->v1_knowledge_bases_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Data set UUID | 

### Return type

[**V1KnowledgeBasesIdDelete200Response**](V1KnowledgeBasesIdDelete200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data set marked for deletion |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_get**
> V1KnowledgeBasesIdGet200Response v1_knowledge_bases_id_get(id)

Get a data set

Returns a single active data set belonging to the first workspace.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_knowledge_bases_id_get200_response import V1KnowledgeBasesIdGet200Response
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
    api_instance = fetch_hive_sdk.PublicDataSetsApi(api_client)
    id = 'id_example' # str | Data set UUID

    try:
        # Get a data set
        api_response = api_instance.v1_knowledge_bases_id_get(id)
        print("The response of PublicDataSetsApi->v1_knowledge_bases_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicDataSetsApi->v1_knowledge_bases_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Data set UUID | 

### Return type

[**V1KnowledgeBasesIdGet200Response**](V1KnowledgeBasesIdGet200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data set returned |  -  |
**401** | unauthorized |  -  |
**422** | data set not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_patch**
> V1KnowledgeBasesIdPatch200Response v1_knowledge_bases_id_patch(id, v1_knowledge_bases_id_patch_request)

Update a data set

Updates name, description, or search settings of an existing data set.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_knowledge_bases_id_patch200_response import V1KnowledgeBasesIdPatch200Response
from fetch_hive_sdk.models.v1_knowledge_bases_id_patch_request import V1KnowledgeBasesIdPatchRequest
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
    api_instance = fetch_hive_sdk.PublicDataSetsApi(api_client)
    id = 'id_example' # str | Data set UUID
    v1_knowledge_bases_id_patch_request = fetch_hive_sdk.V1KnowledgeBasesIdPatchRequest() # V1KnowledgeBasesIdPatchRequest | 

    try:
        # Update a data set
        api_response = api_instance.v1_knowledge_bases_id_patch(id, v1_knowledge_bases_id_patch_request)
        print("The response of PublicDataSetsApi->v1_knowledge_bases_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicDataSetsApi->v1_knowledge_bases_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Data set UUID | 
 **v1_knowledge_bases_id_patch_request** | [**V1KnowledgeBasesIdPatchRequest**](V1KnowledgeBasesIdPatchRequest.md)|  | 

### Return type

[**V1KnowledgeBasesIdPatch200Response**](V1KnowledgeBasesIdPatch200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data set updated |  -  |
**401** | unauthorized |  -  |
**422** | data set not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_search_post**
> V1KnowledgeBasesIdSearchPost200Response v1_knowledge_bases_id_search_post(id, v1_knowledge_bases_id_search_post_request)

Search a data set

Performs a vector, full-text, or hybrid search against the data set.
Returns matching chunks above the configured score threshold.


### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_knowledge_bases_id_search_post200_response import V1KnowledgeBasesIdSearchPost200Response
from fetch_hive_sdk.models.v1_knowledge_bases_id_search_post_request import V1KnowledgeBasesIdSearchPostRequest
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
    api_instance = fetch_hive_sdk.PublicDataSetsApi(api_client)
    id = 'id_example' # str | Data set UUID
    v1_knowledge_bases_id_search_post_request = fetch_hive_sdk.V1KnowledgeBasesIdSearchPostRequest() # V1KnowledgeBasesIdSearchPostRequest | 

    try:
        # Search a data set
        api_response = api_instance.v1_knowledge_bases_id_search_post(id, v1_knowledge_bases_id_search_post_request)
        print("The response of PublicDataSetsApi->v1_knowledge_bases_id_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicDataSetsApi->v1_knowledge_bases_id_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Data set UUID | 
 **v1_knowledge_bases_id_search_post_request** | [**V1KnowledgeBasesIdSearchPostRequest**](V1KnowledgeBasesIdSearchPostRequest.md)|  | 

### Return type

[**V1KnowledgeBasesIdSearchPost200Response**](V1KnowledgeBasesIdSearchPost200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search results returned |  -  |
**401** | unauthorized |  -  |
**422** | invalid search type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_post**
> V1KnowledgeBasesPost200Response v1_knowledge_bases_post(v1_knowledge_bases_post_request)

Create a data set

Creates a new data set in the first workspace of the account.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_knowledge_bases_post200_response import V1KnowledgeBasesPost200Response
from fetch_hive_sdk.models.v1_knowledge_bases_post_request import V1KnowledgeBasesPostRequest
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
    api_instance = fetch_hive_sdk.PublicDataSetsApi(api_client)
    v1_knowledge_bases_post_request = fetch_hive_sdk.V1KnowledgeBasesPostRequest() # V1KnowledgeBasesPostRequest | 

    try:
        # Create a data set
        api_response = api_instance.v1_knowledge_bases_post(v1_knowledge_bases_post_request)
        print("The response of PublicDataSetsApi->v1_knowledge_bases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicDataSetsApi->v1_knowledge_bases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_knowledge_bases_post_request** | [**V1KnowledgeBasesPostRequest**](V1KnowledgeBasesPostRequest.md)|  | 

### Return type

[**V1KnowledgeBasesPost200Response**](V1KnowledgeBasesPost200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | data set created |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

