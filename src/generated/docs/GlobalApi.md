# fetch_hive_sdk.GlobalApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_global_embeddings_post**](GlobalApi.md#v1_global_embeddings_post) | **POST** /v1/global/embeddings | Generate a text embedding


# **v1_global_embeddings_post**
> V1GlobalEmbeddingsPost200Response v1_global_embeddings_post(v1_global_embeddings_post_request=v1_global_embeddings_post_request)

Generate a text embedding

Generates a vector embedding for the provided text using OpenAI's embeddings API.
Authenticated via a shared global API key passed as a Bearer  or X-API-Key header.
Intended for internal service-to-service use (e.g. Rust API calling Rails).


### Example

* Bearer Authentication (global_api_key):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_global_embeddings_post200_response import V1GlobalEmbeddingsPost200Response
from fetch_hive_sdk.models.v1_global_embeddings_post_request import V1GlobalEmbeddingsPostRequest
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

# Configure Bearer authorization: global_api_key
configuration = fetch_hive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fetch_hive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fetch_hive_sdk.GlobalApi(api_client)
    v1_global_embeddings_post_request = fetch_hive_sdk.V1GlobalEmbeddingsPostRequest() # V1GlobalEmbeddingsPostRequest |  (optional)

    try:
        # Generate a text embedding
        api_response = api_instance.v1_global_embeddings_post(v1_global_embeddings_post_request=v1_global_embeddings_post_request)
        print("The response of GlobalApi->v1_global_embeddings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalApi->v1_global_embeddings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_global_embeddings_post_request** | [**V1GlobalEmbeddingsPostRequest**](V1GlobalEmbeddingsPostRequest.md)|  | [optional] 

### Return type

[**V1GlobalEmbeddingsPost200Response**](V1GlobalEmbeddingsPost200Response.md)

### Authorization

[global_api_key](../README.md#global_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | embedding generated |  -  |
**401** | invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

