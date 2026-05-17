# WorkspaceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**default_charge_type** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_archived** | **bool** |  | [optional] 
**is_default_charge_type_hosted** | **bool** |  | [optional] 
**is_default_charge_type_personal** | **bool** |  | [optional] 
**active_prompts_count** | **int** |  | [optional] 
**archived_prompts_count** | **int** |  | [optional] 
**active_prompt_endpoints_count** | **int** |  | [optional] 
**archived_prompt_endpoints_count** | **int** |  | [optional] 
**sample_evaluators_count** | **int** |  | [optional] 
**sample_inputs_count** | **int** |  | [optional] 
**sample_tools_count** | **int** |  | [optional] 
**openai_enabled** | **bool** |  | [optional] 
**anthropic_enabled** | **bool** |  | [optional] 
**deepseek_enabled** | **bool** |  | [optional] 
**llama_enabled** | **bool** |  | [optional] 
**mistral_enabled** | **bool** |  | [optional] 
**gemma_enabled** | **bool** |  | [optional] 
**gemini_enabled** | **bool** |  | [optional] 
**xai_enabled** | **bool** |  | [optional] 
**exa_enabled** | **bool** |  | [optional] 
**perplexity_enabled** | **bool** |  | [optional] 
**qwen_enabled** | **bool** |  | [optional] 
**minimax_enabled** | **bool** |  | [optional] 
**kimi_enabled** | **bool** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.workspace_object import WorkspaceObject

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceObject from a JSON string
workspace_object_instance = WorkspaceObject.from_json(json)
# print the JSON string representation of the object
print(WorkspaceObject.to_json())

# convert the object into a dict
workspace_object_dict = workspace_object_instance.to_dict()
# create an instance of WorkspaceObject from a dict
workspace_object_from_dict = WorkspaceObject.from_dict(workspace_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


