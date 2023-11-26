# RecurringTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace** | [**Workspace**](Workspace.md) |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**creator** | [**User**](User.md) |  | 
**assignee** | [**User**](User.md) |  | 
**project** | [**Project**](Project.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | 
**priority** | **str** |  | 
**labels** | [**List[Label]**](Label.md) |  | 

## Example

```python
from openapi_client.models.recurring_task import RecurringTask

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringTask from a JSON string
recurring_task_instance = RecurringTask.from_json(json)
# print the JSON string representation of the object
print RecurringTask.to_json()

# convert the object into a dict
recurring_task_dict = recurring_task_instance.to_dict()
# create an instance of RecurringTask from a dict
recurring_task_form_dict = recurring_task.from_dict(recurring_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


