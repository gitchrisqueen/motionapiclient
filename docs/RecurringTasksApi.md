# usemotion_api_client.RecurringTasksApi

All URIs are relative to *https://api.usemotion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recurring_tasks_controller_delete_task**](RecurringTasksApi.md#recurring_tasks_controller_delete_task) | **DELETE** /recurring-tasks/{taskId} | Delete a Recurring Task
[**recurring_tasks_controller_list_recurring_tasks**](RecurringTasksApi.md#recurring_tasks_controller_list_recurring_tasks) | **GET** /recurring-tasks | List Recurring Tasks
[**recurring_tasks_controller_post_recurring_task**](RecurringTasksApi.md#recurring_tasks_controller_post_recurring_task) | **POST** /recurring-tasks | Create a Recurring Task


# **recurring_tasks_controller_delete_task**
> recurring_tasks_controller_delete_task(task_id)

Delete a Recurring Task

### Example

* Api Key Authentication (Motion_API_Key):

```python
import time
import os
import usemotion_api_client
from usemotion_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.usemotion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = usemotion_api_client.Configuration(
    host = "https://api.usemotion.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Motion_API_Key
configuration.api_key['Motion_API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Motion_API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with usemotion_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usemotion_api_client.RecurringTasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Delete a Recurring Task
        api_instance.recurring_tasks_controller_delete_task(task_id)
    except Exception as e:
        print("Exception when calling RecurringTasksApi->recurring_tasks_controller_delete_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Motion_API_Key](../README.md#Motion_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recurring_tasks_controller_list_recurring_tasks**
> ListRecurringTasks recurring_tasks_controller_list_recurring_tasks(workspace_id, cursor=cursor)

List Recurring Tasks

### Example

* Api Key Authentication (Motion_API_Key):

```python
import time
import os
import usemotion_api_client
from usemotion_api_client.models.list_recurring_tasks import ListRecurringTasks
from usemotion_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.usemotion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = usemotion_api_client.Configuration(
    host = "https://api.usemotion.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Motion_API_Key
configuration.api_key['Motion_API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Motion_API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with usemotion_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usemotion_api_client.RecurringTasksApi(api_client)
    workspace_id = 'workspace_id_example' # str | The id of the workspace you want tasks from.
    cursor = 'cursor_example' # str | Use if a previous request returned a cursor. Will page through results (optional)

    try:
        # List Recurring Tasks
        api_response = api_instance.recurring_tasks_controller_list_recurring_tasks(workspace_id, cursor=cursor)
        print("The response of RecurringTasksApi->recurring_tasks_controller_list_recurring_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringTasksApi->recurring_tasks_controller_list_recurring_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The id of the workspace you want tasks from. | 
 **cursor** | **str**| Use if a previous request returned a cursor. Will page through results | [optional] 

### Return type

[**ListRecurringTasks**](ListRecurringTasks.md)

### Authorization

[Motion_API_Key](../README.md#Motion_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recurring_tasks_controller_post_recurring_task**
> RecurringTask recurring_tasks_controller_post_recurring_task(recurring_tasks_post)

Create a Recurring Task

## Description Input  When passing in a task description, the input will be treated as [GitHub Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).  # Defining Frequencies  In order to give our API all the power that motion has to offer, we allow calls to create recurring tasks in the same way you can through the UI.  ## Defining specific days for a frequency  <!-- theme: warning -->  > ### Note > > Defining days should always be used along with a specific frequency type as defined below. > A array of days should never be used on its own. See examples below.  When picking a set of specific week days, we expect it to be defined as an array with a subset of the following values.  - MO - Monday - TU - Tuesday - WE - Wednesday - TH - Thursday - FR - Friday - SA - Saturday - SU - Sunday  Example - `[MO, FR, SU]` would mean Monday, Friday and Sunday.  ## Defining a daily frequency  - `daily_every_day` - `daily_every_week_day` - `daily_specific_days_$DAYS_ARRAY$`   - Ex: `daily_specific_days_[MO, TU, FR]`  ## Defining a weekly frequency  - `weekly_any_day` - `weekly_any_week_day` - `weekly_specific_days_$DAYS_ARRAY$`   - Ex: `weekly_specific_days_[MO, TU, FR]`  ## Defining a bi-weekly frequency  - `biweekly_first_week_specific_days_$DAYS_ARRAY$`   - Ex: `biweekly_first_week_specific_days_[MO, TU, FR]` - `biweekly_first_week_any_day` - `biweekly_first_week_any_week_day` - `biweekly_second_week_any_day` - `biweekly_second_week_any_week_day`  ## Defining a monthly frequency  ### Specific Week Day Options  When choosing the 1st, 2nd, 3rd, 4th or last day of the week for the month, it takes the form of any of the following where $DAY$ can be substituted for the day code mentioned above.  - `monthly_first_$DAY$` - `monthly_second_$DAY$` - `monthly_third_$DAY$` - `monthly_fourth_$DAY$` - `monthly_last_$DAY$`  **Example** `monthly_first_MO`  ### Specific Day Options  When choosing a specific day of the month, for example the 6th, it would be defined with just the number like below.  Examples:  - `monthly_1` - `monthly_15` - `monthly_31`  In the case you choose a numeric value for a month that does not have that many days, we will default to the last day of the month.  ### Specific Week Options  **Any Day**  - `monthly_any_day_first_week` - `monthly_any_day_second_week` - `monthly_any_day_third_week` - `monthly_any_day_fourth_week` - `monthly_any_day_last_week`  **Any Week Day**  - `monthly_any_week_day_first_week` - `monthly_any_week_day_second_week` - `monthly_any_week_day_third_week` - `monthly_any_week_day_fourth_week` - `monthly_any_week_day_last_week`  ### Other Options  - `monthly_last_day_of_month` - `monthly_any_week_day_of_month` - `monthly_any_day_of_month`  ## Defining a quarterly frequency  ### First Days  - `quarterly_first_day` - `quarterly_first_week_day` - `quarterly_first_$DAY$`   - Ex. `quarterly_first_MO`  ### Last Days  - `quarterly_last_day` - `quarterly_last_week_day` - `quarterly_last_$DAY$`   - Ex. `quarterly_last_MO`  ### Other Options  - `quarterly_any_day_first_week` - `quarterly_any_day_second_week` - `quarterly_any_day_last_week` - `quarterly_any_day_first_month` - `quarterly_any_day_second_month` - `quarterly_any_day_third_month` 

### Example

* Api Key Authentication (Motion_API_Key):

```python
import time
import os
import usemotion_api_client
from usemotion_api_client.models.recurring_task import RecurringTask
from usemotion_api_client.models.recurring_tasks_post import RecurringTasksPost
from usemotion_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.usemotion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = usemotion_api_client.Configuration(
    host = "https://api.usemotion.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Motion_API_Key
configuration.api_key['Motion_API_Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Motion_API_Key'] = 'Bearer'

# Enter a context with an instance of the API client
with usemotion_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usemotion_api_client.RecurringTasksApi(api_client)
    recurring_tasks_post = usemotion_api_client.RecurringTasksPost() # RecurringTasksPost | 

    try:
        # Create a Recurring Task
        api_response = api_instance.recurring_tasks_controller_post_recurring_task(recurring_tasks_post)
        print("The response of RecurringTasksApi->recurring_tasks_controller_post_recurring_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringTasksApi->recurring_tasks_controller_post_recurring_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_tasks_post** | [**RecurringTasksPost**](RecurringTasksPost.md)|  | 

### Return type

[**RecurringTask**](RecurringTask.md)

### Authorization

[Motion_API_Key](../README.md#Motion_API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

