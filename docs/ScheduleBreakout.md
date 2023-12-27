# ScheduleBreakout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monday** | [**List[DailySchedule]**](DailySchedule.md) | Array could be empty if there is no range for this day | 
**tuesday** | [**List[DailySchedule]**](DailySchedule.md) | Array could be empty if there is no range for this day | 
**wednesday** | [**List[DailySchedule]**](DailySchedule.md) | Array could be empty if there is no range for this day | 
**thursday** | [**List[DailySchedule]**](DailySchedule.md) | Array could be empty if there is no range for this day | 
**friday** | [**List[DailySchedule]**](DailySchedule.md) | Array could be empty if there is no range for this day | 
**saturday** | [**List[DailySchedule]**](DailySchedule.md) | Array could be empty if there is no range for this day | 
**sunday** | [**List[DailySchedule]**](DailySchedule.md) | Array could be empty if there is no range for this day | 

## Example

```python
from usemotion_api_client.models.schedule_breakout import ScheduleBreakout

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleBreakout from a JSON string
schedule_breakout_instance = ScheduleBreakout.from_json(json)
# print the JSON string representation of the object
print ScheduleBreakout.to_json()

# convert the object into a dict
schedule_breakout_dict = schedule_breakout_instance.to_dict()
# create an instance of ScheduleBreakout from a dict
schedule_breakout_form_dict = schedule_breakout.from_dict(schedule_breakout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


