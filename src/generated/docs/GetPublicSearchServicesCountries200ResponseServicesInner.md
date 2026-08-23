# GetPublicSearchServicesCountries200ResponseServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | 
**name** | **str** |  | 
**country_value_field** | **str** |  | 
**country_value_format** | **str** |  | 
**countries** | [**List[GetPublicSearchServicesCountries200ResponseServicesInnerCountriesInner]**](GetPublicSearchServicesCountries200ResponseServicesInnerCountriesInner.md) |  | 

## Example

```python
from fetch_hive_sdk.models.get_public_search_services_countries200_response_services_inner import GetPublicSearchServicesCountries200ResponseServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicSearchServicesCountries200ResponseServicesInner from a JSON string
get_public_search_services_countries200_response_services_inner_instance = GetPublicSearchServicesCountries200ResponseServicesInner.from_json(json)
# print the JSON string representation of the object
print(GetPublicSearchServicesCountries200ResponseServicesInner.to_json())

# convert the object into a dict
get_public_search_services_countries200_response_services_inner_dict = get_public_search_services_countries200_response_services_inner_instance.to_dict()
# create an instance of GetPublicSearchServicesCountries200ResponseServicesInner from a dict
get_public_search_services_countries200_response_services_inner_from_dict = GetPublicSearchServicesCountries200ResponseServicesInner.from_dict(get_public_search_services_countries200_response_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


