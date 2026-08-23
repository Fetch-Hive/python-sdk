# KnowledgeBaseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**description** | **str** | (value may be null) | [optional] 
**data_item_count** | **int** |  | 
**search_score_threshold** | **str** |  | 
**search_chunk_limit** | **int** |  | 
**generated_at** | **datetime** | (value may be null) | [optional] 
**status** | **str** |  | 
**search_type** | **str** |  | 
**is_active** | **bool** |  | 
**is_archived** | **bool** |  | 
**is_hybrid_search** | **bool** |  | 
**is_vector_search** | **bool** |  | 
**is_full_text_search** | **bool** |  | 

## Example

```python
from fetch_hive_sdk.models.knowledge_base_object import KnowledgeBaseObject

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseObject from a JSON string
knowledge_base_object_instance = KnowledgeBaseObject.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseObject.to_json())

# convert the object into a dict
knowledge_base_object_dict = knowledge_base_object_instance.to_dict()
# create an instance of KnowledgeBaseObject from a dict
knowledge_base_object_from_dict = KnowledgeBaseObject.from_dict(knowledge_base_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


