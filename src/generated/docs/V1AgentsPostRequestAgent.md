# V1AgentsPostRequestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**llm_model** | **str** |  | 
**model_type** | **str** |  | 
**description** | **str** |  | [optional] 
**instruction_prompt** | **str** |  | [optional] 
**temperature** | **float** |  | [optional] 
**max_token** | **UUID** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.v1_agents_post_request_agent import V1AgentsPostRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of V1AgentsPostRequestAgent from a JSON string
v1_agents_post_request_agent_instance = V1AgentsPostRequestAgent.from_json(json)
# print the JSON string representation of the object
print(V1AgentsPostRequestAgent.to_json())

# convert the object into a dict
v1_agents_post_request_agent_dict = v1_agents_post_request_agent_instance.to_dict()
# create an instance of V1AgentsPostRequestAgent from a dict
v1_agents_post_request_agent_from_dict = V1AgentsPostRequestAgent.from_dict(v1_agents_post_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


