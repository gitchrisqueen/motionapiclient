# Task


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | [**TaskDuration**](TaskDuration.md) |  | [optional] 
**workspace** | [**Workspace**](Workspace.md) |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**due_date** | **datetime** |  | 
**deadline_type** | **str** |  | [default to 'SOFT']
**parent_recurring_task_id** | **str** |  | 
**completed** | **bool** |  | 
**creator** | [**User**](User.md) |  | 
**project** | [**Project**](Project.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | 
**priority** | **str** |  | 
**labels** | [**List[Label]**](Label.md) |  | 
**assignees** | [**List[User]**](User.md) |  | 
**scheduled_start** | **datetime** | The time that motion has scheduled this task to start | [optional] 
**created_time** | **datetime** | The time that the task was created | 
**scheduled_end** | **datetime** | The time that motion has scheduled this task to end | [optional] 
**scheduling_issue** | **bool** | Returns true if Motion was unable to schedule this task. Check Motion directly to address | 

## Example

```python
from openapi_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_form_dict = task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


