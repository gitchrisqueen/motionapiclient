# ListProjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[Project]**](Project.md) |  | 
**meta** | [**MetaResult**](MetaResult.md) |  | [optional] 

## Example

```python
from usemotion_api_client.models.list_projects import ListProjects

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjects from a JSON string
list_projects_instance = ListProjects.from_json(json)
# print the JSON string representation of the object
print ListProjects.to_json()

# convert the object into a dict
list_projects_dict = list_projects_instance.to_dict()
# create an instance of ListProjects from a dict
list_projects_form_dict = list_projects.from_dict(list_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


