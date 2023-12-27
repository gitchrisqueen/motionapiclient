# RecurringTasksPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | Frequency in which the task should be scheduled. Please carefully read how to construct above. | 
**deadline_type** | **str** |  | [optional] [default to 'SOFT']
**duration** | [**RecurringTasksPostDuration**](RecurringTasksPostDuration.md) |  | [optional] 
**starting_on** | **datetime** | ISO 8601 Date which is trimmed to the start of the day passed | [optional] 
**ideal_time** | **str** |  | [optional] 
**schedule** | **str** | Schedule the task must adhere to | [optional] [default to 'Work Hours']
**name** | **str** | Name / title of the task | 
**workspace_id** | **str** |  | 
**description** | **str** |  | [optional] 
**priority** | **str** |  | [default to 'MEDIUM']
**assignee_id** | **str** | The user id the task should be assigned too | 

## Example

```python
from usemotion_api_client.models.recurring_tasks_post import RecurringTasksPost

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringTasksPost from a JSON string
recurring_tasks_post_instance = RecurringTasksPost.from_json(json)
# print the JSON string representation of the object
print RecurringTasksPost.to_json()

# convert the object into a dict
recurring_tasks_post_dict = recurring_tasks_post_instance.to_dict()
# create an instance of RecurringTasksPost from a dict
recurring_tasks_post_form_dict = recurring_tasks_post.from_dict(recurring_tasks_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


