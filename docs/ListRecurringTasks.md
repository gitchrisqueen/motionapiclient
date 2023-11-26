# ListRecurringTasks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks** | [**List[RecurringTask]**](RecurringTask.md) |  | 
**meta** | [**MetaResult**](MetaResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_recurring_tasks import ListRecurringTasks

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecurringTasks from a JSON string
list_recurring_tasks_instance = ListRecurringTasks.from_json(json)
# print the JSON string representation of the object
print ListRecurringTasks.to_json()

# convert the object into a dict
list_recurring_tasks_dict = list_recurring_tasks_instance.to_dict()
# create an instance of ListRecurringTasks from a dict
list_recurring_tasks_form_dict = list_recurring_tasks.from_dict(list_recurring_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


