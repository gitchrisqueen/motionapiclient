# MoveTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**assignee_id** | **str** | The user id the task should be assigned to | [optional] 

## Example

```python
from usemotion_api_client.models.move_task import MoveTask

# TODO update the JSON string below
json = "{}"
# create an instance of MoveTask from a JSON string
move_task_instance = MoveTask.from_json(json)
# print the JSON string representation of the object
print MoveTask.to_json()

# convert the object into a dict
move_task_dict = move_task_instance.to_dict()
# create an instance of MoveTask from a dict
move_task_form_dict = move_task.from_dict(move_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


