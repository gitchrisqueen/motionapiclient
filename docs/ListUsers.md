# ListUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[User]**](User.md) |  | 
**meta** | [**MetaResult**](MetaResult.md) |  | [optional] 

## Example

```python
from usemotion_api_client.models.list_users import ListUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsers from a JSON string
list_users_instance = ListUsers.from_json(json)
# print the JSON string representation of the object
print ListUsers.to_json()

# convert the object into a dict
list_users_dict = list_users_instance.to_dict()
# create an instance of ListUsers from a dict
list_users_form_dict = list_users.from_dict(list_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


