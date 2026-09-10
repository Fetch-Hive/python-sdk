# AgentDelegation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**status** | **str** |  | 
**kind** | **str** |  | 
**target** | **Dict[str, object]** |  | 
**result** | **Dict[str, object]** | (value may be null) | [optional] 
**expected_by** | **datetime** | (value may be null) | [optional] 
**delivered_at** | **datetime** | (value may be null) | [optional] 
**delivery_error** | **str** | (value may be null) | [optional] 
**parent_request_id** | **str** |  | 
**tool_call_id** | **str** |  | 
**workflow_run_id** | **UUID** | (value may be null) | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.agent_delegation import AgentDelegation

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDelegation from a JSON string
agent_delegation_instance = AgentDelegation.from_json(json)
# print the JSON string representation of the object
print(AgentDelegation.to_json())

# convert the object into a dict
agent_delegation_dict = agent_delegation_instance.to_dict()
# create an instance of AgentDelegation from a dict
agent_delegation_from_dict = AgentDelegation.from_dict(agent_delegation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


