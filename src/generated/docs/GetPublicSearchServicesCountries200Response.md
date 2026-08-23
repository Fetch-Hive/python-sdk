# GetPublicSearchServicesCountries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[GetPublicSearchServicesCountries200ResponseServicesInner]**](GetPublicSearchServicesCountries200ResponseServicesInner.md) |  | 

## Example

```python
from fetch_hive_sdk.models.get_public_search_services_countries200_response import GetPublicSearchServicesCountries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicSearchServicesCountries200Response from a JSON string
get_public_search_services_countries200_response_instance = GetPublicSearchServicesCountries200Response.from_json(json)
# print the JSON string representation of the object
print(GetPublicSearchServicesCountries200Response.to_json())

# convert the object into a dict
get_public_search_services_countries200_response_dict = get_public_search_services_countries200_response_instance.to_dict()
# create an instance of GetPublicSearchServicesCountries200Response from a dict
get_public_search_services_countries200_response_from_dict = GetPublicSearchServicesCountries200Response.from_dict(get_public_search_services_countries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


