# TaskDuration

A duration can be one of the following... \"NONE\", \"REMINDER\", or a integer greater than 0

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.task_duration import TaskDuration

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDuration from a JSON string
task_duration_instance = TaskDuration.from_json(json)
# print the JSON string representation of the object
print TaskDuration.to_json()

# convert the object into a dict
task_duration_dict = task_duration_instance.to_dict()
# create an instance of TaskDuration from a dict
task_duration_form_dict = task_duration.from_dict(task_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


