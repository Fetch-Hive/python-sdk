# fetch_hive_sdk.UsersProfileApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_users_me_get**](UsersProfileApi.md#v1_users_me_get) | **GET** /v1/users/me | Retrieve the authenticated user


# **v1_users_me_get**
> V1UsersMeGet200Response v1_users_me_get()

Retrieve the authenticated user

Returns the full user object for the currently authenticated user, including account and workspaces.

### Example

* Bearer (JWT) Authentication (bearer_auth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.v1_users_me_get200_response import V1UsersMeGet200Response
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
    api_instance = fetch_hive_sdk.UsersProfileApi(api_client)

    try:
        # Retrieve the authenticated user
        api_response = api_instance.v1_users_me_get()
        print("The response of UsersProfileApi->v1_users_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersProfileApi->v1_users_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1UsersMeGet200Response**](V1UsersMeGet200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | user returned |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

