# GetPublicRequests200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**request_id** | **str** |  | 
**status** | **str** |  | 
**request_type** | **str** |  | 
**requestable_type** | **str** | (value may be null) | [optional] 
**requestable_id** | **UUID** | (value may be null) | [optional] 
**message** | **str** | (value may be null) | [optional] 
**generated_at** | **datetime** | (value may be null) | [optional] 
**started_at** | **datetime** | (value may be null) | [optional] 
**ended_at** | **datetime** | (value may be null) | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**user_metadata** | **Dict[str, object]** |  | [optional] 
**data** | **Dict[str, object]** | (value may be null) | [optional] 

## Example

```python
from fetch_hive_sdk.models.get_public_requests200_response import GetPublicRequests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicRequests200Response from a JSON string
get_public_requests200_response_instance = GetPublicRequests200Response.from_json(json)
# print the JSON string representation of the object
print(GetPublicRequests200Response.to_json())

# convert the object into a dict
get_public_requests200_response_dict = get_public_requests200_response_instance.to_dict()
# create an instance of GetPublicRequests200Response from a dict
get_public_requests200_response_from_dict = GetPublicRequests200Response.from_dict(get_public_requests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


