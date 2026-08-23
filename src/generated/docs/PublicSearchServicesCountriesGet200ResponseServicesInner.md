# PublicSearchServicesCountriesGet200ResponseServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | 
**name** | **str** |  | 
**country_value_field** | **str** |  | 
**country_value_format** | **str** |  | 
**countries** | [**List[PublicSearchServicesCountriesGet200ResponseServicesInnerCountriesInner]**](PublicSearchServicesCountriesGet200ResponseServicesInnerCountriesInner.md) |  | 

## Example

```python
from fetch_hive_sdk.models.public_search_services_countries_get200_response_services_inner import PublicSearchServicesCountriesGet200ResponseServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSearchServicesCountriesGet200ResponseServicesInner from a JSON string
public_search_services_countries_get200_response_services_inner_instance = PublicSearchServicesCountriesGet200ResponseServicesInner.from_json(json)
# print the JSON string representation of the object
print(PublicSearchServicesCountriesGet200ResponseServicesInner.to_json())

# convert the object into a dict
public_search_services_countries_get200_response_services_inner_dict = public_search_services_countries_get200_response_services_inner_instance.to_dict()
# create an instance of PublicSearchServicesCountriesGet200ResponseServicesInner from a dict
public_search_services_countries_get200_response_services_inner_from_dict = PublicSearchServicesCountriesGet200ResponseServicesInner.from_dict(public_search_services_countries_get200_response_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


