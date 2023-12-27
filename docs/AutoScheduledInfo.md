# AutoScheduledInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | ISO 8601 Date which is trimmed to the start of the day passed | [optional] 
**deadline_type** | **str** |  | [optional] [default to 'SOFT']
**schedule** | **str** | Schedule the task must adhere to. Schedule MUST be &#39;Work Hours&#39; if scheduling the task for another user. | [optional] [default to 'Work Hours']

## Example

```python
from usemotion_api_client.models.auto_scheduled_info import AutoScheduledInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AutoScheduledInfo from a JSON string
auto_scheduled_info_instance = AutoScheduledInfo.from_json(json)
# print the JSON string representation of the object
print AutoScheduledInfo.to_json()

# convert the object into a dict
auto_scheduled_info_dict = auto_scheduled_info_instance.to_dict()
# create an instance of AutoScheduledInfo from a dict
auto_scheduled_info_form_dict = auto_scheduled_info.from_dict(auto_scheduled_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


