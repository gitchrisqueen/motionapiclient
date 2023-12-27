# TaskPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **datetime** | ISO 8601 Due date on the task. REQUIRED for scheduled tasks | [optional] 
**duration** | [**TaskDuration**](TaskDuration.md) |  | [optional] 
**status** | **str** | Defaults to workspace default status. | [optional] 
**auto_scheduled** | [**AutoScheduledInfo**](AutoScheduledInfo.md) |  | [optional] 
**name** | **str** | Name / title of the task | 
**project_id** | **str** |  | [optional] 
**workspace_id** | **str** |  | 
**description** | **str** | Input as GitHub Flavored Markdown | [optional] 
**priority** | **str** |  | [optional] [default to 'MEDIUM']
**labels** | **List[str]** |  | [optional] 
**assignee_id** | **str** | The user id the task should be assigned to | [optional] 

## Example

```python
from usemotion_api_client.models.task_post import TaskPost

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPost from a JSON string
task_post_instance = TaskPost.from_json(json)
# print the JSON string representation of the object
print TaskPost.to_json()

# convert the object into a dict
task_post_dict = task_post_instance.to_dict()
# create an instance of TaskPost from a dict
task_post_form_dict = task_post.from_dict(task_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


