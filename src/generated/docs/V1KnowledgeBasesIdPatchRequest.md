# V1KnowledgeBasesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base** | [**V1KnowledgeBasesIdPatchRequestKnowledgeBase**](V1KnowledgeBasesIdPatchRequestKnowledgeBase.md) |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.v1_knowledge_bases_id_patch_request import V1KnowledgeBasesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1KnowledgeBasesIdPatchRequest from a JSON string
v1_knowledge_bases_id_patch_request_instance = V1KnowledgeBasesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1KnowledgeBasesIdPatchRequest.to_json())

# convert the object into a dict
v1_knowledge_bases_id_patch_request_dict = v1_knowledge_bases_id_patch_request_instance.to_dict()
# create an instance of V1KnowledgeBasesIdPatchRequest from a dict
v1_knowledge_bases_id_patch_request_from_dict = V1KnowledgeBasesIdPatchRequest.from_dict(v1_knowledge_bases_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


