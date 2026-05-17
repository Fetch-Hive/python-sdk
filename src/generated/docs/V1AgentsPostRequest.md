# V1AgentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**V1AgentsPostRequestAgent**](V1AgentsPostRequestAgent.md) |  | 

## Example

```python
from fetch_hive_sdk.models.v1_agents_post_request import V1AgentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AgentsPostRequest from a JSON string
v1_agents_post_request_instance = V1AgentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AgentsPostRequest.to_json())

# convert the object into a dict
v1_agents_post_request_dict = v1_agents_post_request_instance.to_dict()
# create an instance of V1AgentsPostRequest from a dict
v1_agents_post_request_from_dict = V1AgentsPostRequest.from_dict(v1_agents_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


