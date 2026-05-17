# fetch_hive_sdk.WorkflowsApi

All URIs are relative to *https://api.fetchhive.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoke_workflow**](WorkflowsApi.md#invoke_workflow) | **POST** /workflow/invoke | Invoke a workflow deployment


# **invoke_workflow**
> InvokeWorkflowResponse invoke_workflow(invoke_workflow_request)

Invoke a workflow deployment

Runs a configured workflow deployment. Supports both synchronous and
asynchronous execution via the `async` field.

When `async.enabled` is `false` (default), the request blocks until
the workflow completes and returns the output directly.

When `async.enabled` is `true`, the server returns a `202` with a
`run_id`. Poll `GET /v1/workflow_runs/{id}` on the management API to
check status.


### Example

* Bearer Authentication (BearerAuth):

```python
import fetch_hive_sdk
from fetch_hive_sdk.models.invoke_workflow_request import InvokeWorkflowRequest
from fetch_hive_sdk.models.invoke_workflow_response import InvokeWorkflowResponse
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
    api_instance = fetch_hive_sdk.WorkflowsApi(api_client)
    invoke_workflow_request = fetch_hive_sdk.InvokeWorkflowRequest() # InvokeWorkflowRequest | 

    try:
        # Invoke a workflow deployment
        api_response = api_instance.invoke_workflow(invoke_workflow_request)
        print("The response of WorkflowsApi->invoke_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->invoke_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoke_workflow_request** | [**InvokeWorkflowRequest**](InvokeWorkflowRequest.md)|  | 

### Return type

[**InvokeWorkflowResponse**](InvokeWorkflowResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synchronous workflow result. |  -  |
**202** | Async workflow accepted. Poll using the returned &#x60;run_id&#x60;. |  -  |
**400** | Invalid request body or parameters. |  -  |
**401** | Missing or invalid API token. |  -  |
**500** | Unexpected server-side error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

