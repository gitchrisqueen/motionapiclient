# ProjectPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **datetime** | ISO 8601 Due date on the task | [optional] 
**name** | **str** |  | 
**workspace_id** | **str** |  | 
**description** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_post import ProjectPost

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPost from a JSON string
project_post_instance = ProjectPost.from_json(json)
# print the JSON string representation of the object
print ProjectPost.to_json()

# convert the object into a dict
project_post_dict = project_post_instance.to_dict()
# create an instance of ProjectPost from a dict
project_post_form_dict = project_post.from_dict(project_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


