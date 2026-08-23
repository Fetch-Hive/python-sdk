# fetch_hive_sdk.ModelsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_models**](ModelsApi.md#get_public_models) | **GET** /public/models | List active models


# **get_public_models**
> List[GetPublicModels200ResponseInner] get_public_models()

List active models

Returns all active (non-deprecated) LLM and image-generation models
available in Fetch Hive as a flat array. Excludes embedding-only models.

`provider` identifies the underlying model maker (e.g. `openai`, `anthropic`, `minimaxai`).

`model_type` is `"llm"` for chat/text models and `"image_generation"` for
models that generate images. `is_vision` means a model accepts image input;
`is_image_generation` means a model generates images.

`is_reasoning` is `true` when the model supports reasoning capabilities.


### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.get_public_models200_response_inner import GetPublicModels200ResponseInner
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
    api_instance = fetch_hive_sdk.ModelsApi(api_client)

    try:
        # List active models
        api_response = api_instance.get_public_models()
        print("The response of ModelsApi->get_public_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_public_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetPublicModels200ResponseInner]**](GetPublicModels200ResponseInner.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | models returned |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

