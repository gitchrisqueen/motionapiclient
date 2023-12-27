# TaskPatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name / title of the task | [optional] 
**due_date** | **datetime** | ISO 8601 Due date on the task. REQUIRED for scheduled tasks | [optional] 
**duration** | [**TaskPatchDuration**](TaskPatchDuration.md) |  | [optional] 
**status** | **str** | Defaults to workspace default status. | [optional] 
**auto_scheduled** | [**AutoScheduledInfo**](AutoScheduledInfo.md) |  | [optional] 
**project_id** | **str** |  | [optional] 
**description** | **str** | Input as GitHub Flavored Markdown | [optional] 
**priority** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**assignee_id** | **str** | The user id the task should be assigned to | [optional] 

## Example

```python
from openapi_client.models.task_patch import TaskPatch

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPatch from a JSON string
task_patch_instance = TaskPatch.from_json(json)
# print the JSON string representation of the object
print TaskPatch.to_json()

# convert the object into a dict
task_patch_dict = task_patch_instance.to_dict()
# create an instance of TaskPatch from a dict
task_patch_form_dict = task_patch.from_dict(task_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


