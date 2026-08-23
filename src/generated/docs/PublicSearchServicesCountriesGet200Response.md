# PublicSearchServicesCountriesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[PublicSearchServicesCountriesGet200ResponseServicesInner]**](PublicSearchServicesCountriesGet200ResponseServicesInner.md) |  | 

## Example

```python
from fetch_hive_sdk.models.public_search_services_countries_get200_response import PublicSearchServicesCountriesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSearchServicesCountriesGet200Response from a JSON string
public_search_services_countries_get200_response_instance = PublicSearchServicesCountriesGet200Response.from_json(json)
# print the JSON string representation of the object
print(PublicSearchServicesCountriesGet200Response.to_json())

# convert the object into a dict
public_search_services_countries_get200_response_dict = public_search_services_countries_get200_response_instance.to_dict()
# create an instance of PublicSearchServicesCountriesGet200Response from a dict
public_search_services_countries_get200_response_from_dict = PublicSearchServicesCountriesGet200Response.from_dict(public_search_services_countries_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


