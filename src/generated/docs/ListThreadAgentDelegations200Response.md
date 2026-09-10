# ListThreadAgentDelegations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegations** | [**List[AgentDelegation]**](AgentDelegation.md) |  | 

## Example

```python
from fetch_hive_sdk.models.list_thread_agent_delegations200_response import ListThreadAgentDelegations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListThreadAgentDelegations200Response from a JSON string
list_thread_agent_delegations200_response_instance = ListThreadAgentDelegations200Response.from_json(json)
# print the JSON string representation of the object
print(ListThreadAgentDelegations200Response.to_json())

# convert the object into a dict
list_thread_agent_delegations200_response_dict = list_thread_agent_delegations200_response_instance.to_dict()
# create an instance of ListThreadAgentDelegations200Response from a dict
list_thread_agent_delegations200_response_from_dict = ListThreadAgentDelegations200Response.from_dict(list_thread_agent_delegations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


