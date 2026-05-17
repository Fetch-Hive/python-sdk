# V1RequestsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**status** | **str** |  | 
**request_type** | **str** |  | 
**started_at** | **datetime** | (value may be null) | [optional] 
**ended_at** | **datetime** | (value may be null) | [optional] 

## Example

```python
from fetch_hive_sdk.models.v1_requests_id_get200_response import V1RequestsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1RequestsIdGet200Response from a JSON string
v1_requests_id_get200_response_instance = V1RequestsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1RequestsIdGet200Response.to_json())

# convert the object into a dict
v1_requests_id_get200_response_dict = v1_requests_id_get200_response_instance.to_dict()
# create an instance of V1RequestsIdGet200Response from a dict
v1_requests_id_get200_response_from_dict = V1RequestsIdGet200Response.from_dict(v1_requests_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


