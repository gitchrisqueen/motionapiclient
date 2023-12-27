# MetaResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** | Returned if there are more entities to return. Pass back with the cursor param set to continue paging. | [optional] 
**page_size** | **float** | Maximum number of entities delivered per page | 

## Example

```python
from usemotion_api_client.models.meta_result import MetaResult

# TODO update the JSON string below
json = "{}"
# create an instance of MetaResult from a JSON string
meta_result_instance = MetaResult.from_json(json)
# print the JSON string representation of the object
print MetaResult.to_json()

# convert the object into a dict
meta_result_dict = meta_result_instance.to_dict()
# create an instance of MetaResult from a dict
meta_result_form_dict = meta_result.from_dict(meta_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


