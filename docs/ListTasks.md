# ListTasks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks** | [**List[Task]**](Task.md) |  | 
**meta** | [**MetaResult**](MetaResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_tasks import ListTasks

# TODO update the JSON string below
json = "{}"
# create an instance of ListTasks from a JSON string
list_tasks_instance = ListTasks.from_json(json)
# print the JSON string representation of the object
print ListTasks.to_json()

# convert the object into a dict
list_tasks_dict = list_tasks_instance.to_dict()
# create an instance of ListTasks from a dict
list_tasks_form_dict = list_tasks.from_dict(list_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


