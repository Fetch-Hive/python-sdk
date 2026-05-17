# V1KnowledgeBasesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base** | [**V1KnowledgeBasesPostRequestKnowledgeBase**](V1KnowledgeBasesPostRequestKnowledgeBase.md) |  | 

## Example

```python
from fetch_hive_sdk.models.v1_knowledge_bases_post_request import V1KnowledgeBasesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1KnowledgeBasesPostRequest from a JSON string
v1_knowledge_bases_post_request_instance = V1KnowledgeBasesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1KnowledgeBasesPostRequest.to_json())

# convert the object into a dict
v1_knowledge_bases_post_request_dict = v1_knowledge_bases_post_request_instance.to_dict()
# create an instance of V1KnowledgeBasesPostRequest from a dict
v1_knowledge_bases_post_request_from_dict = V1KnowledgeBasesPostRequest.from_dict(v1_knowledge_bases_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


