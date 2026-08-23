# GetPublicWorkspacesKnowledgeBases200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_bases** | [**List[KnowledgeBaseObject]**](KnowledgeBaseObject.md) |  | 

## Example

```python
from fetch_hive_sdk.models.get_public_workspaces_knowledge_bases200_response import GetPublicWorkspacesKnowledgeBases200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicWorkspacesKnowledgeBases200Response from a JSON string
get_public_workspaces_knowledge_bases200_response_instance = GetPublicWorkspacesKnowledgeBases200Response.from_json(json)
# print the JSON string representation of the object
print(GetPublicWorkspacesKnowledgeBases200Response.to_json())

# convert the object into a dict
get_public_workspaces_knowledge_bases200_response_dict = get_public_workspaces_knowledge_bases200_response_instance.to_dict()
# create an instance of GetPublicWorkspacesKnowledgeBases200Response from a dict
get_public_workspaces_knowledge_bases200_response_from_dict = GetPublicWorkspacesKnowledgeBases200Response.from_dict(get_public_workspaces_knowledge_bases200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


