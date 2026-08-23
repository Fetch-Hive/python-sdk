# GetPublicSearchServicesCountries2404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**supported_services** | **List[str]** |  | [optional] 

## Example

```python
from fetch_hive_sdk.models.get_public_search_services_countries2404_response import GetPublicSearchServicesCountries2404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicSearchServicesCountries2404Response from a JSON string
get_public_search_services_countries2404_response_instance = GetPublicSearchServicesCountries2404Response.from_json(json)
# print the JSON string representation of the object
print(GetPublicSearchServicesCountries2404Response.to_json())

# convert the object into a dict
get_public_search_services_countries2404_response_dict = get_public_search_services_countries2404_response_instance.to_dict()
# create an instance of GetPublicSearchServicesCountries2404Response from a dict
get_public_search_services_countries2404_response_from_dict = GetPublicSearchServicesCountries2404Response.from_dict(get_public_search_services_countries2404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


