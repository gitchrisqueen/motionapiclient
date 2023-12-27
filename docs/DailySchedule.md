# DailySchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | 24 hour time format. HH:mm | 
**end** | **str** | 24 hour time format. HH:mm | 

## Example

```python
from openapi_client.models.daily_schedule import DailySchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DailySchedule from a JSON string
daily_schedule_instance = DailySchedule.from_json(json)
# print the JSON string representation of the object
print DailySchedule.to_json()

# convert the object into a dict
daily_schedule_dict = daily_schedule_instance.to_dict()
# create an instance of DailySchedule from a dict
daily_schedule_form_dict = daily_schedule.from_dict(daily_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


