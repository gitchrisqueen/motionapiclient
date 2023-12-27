# ListComments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[Comment]**](Comment.md) |  | 
**meta** | [**MetaResult**](MetaResult.md) |  | [optional] 

## Example

```python
from usemotion_api_client.models.list_comments import ListComments

# TODO update the JSON string below
json = "{}"
# create an instance of ListComments from a JSON string
list_comments_instance = ListComments.from_json(json)
# print the JSON string representation of the object
print ListComments.to_json()

# convert the object into a dict
list_comments_dict = list_comments_instance.to_dict()
# create an instance of ListComments from a dict
list_comments_form_dict = list_comments.from_dict(list_comments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


