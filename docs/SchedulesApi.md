# usemotion_api_client.SchedulesApi

All URIs are relative to *https://api.usemotion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_controller_get_my_schedules**](SchedulesApi.md#schedules_controller_get_my_schedules) | **GET** /schedules | Get schedules


# **schedules_controller_get_my_schedules**
> List[Schedule] schedules_controller_get_my_schedules()

Get schedules

Get a list of schedules for your user

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import usemotion_api_client
from usemotion_api_client.models.schedule import Schedule
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
    api_instance = usemotion_api_client.SchedulesApi(api_client)

    try:
        # Get schedules
        api_response = api_instance.schedules_controller_get_my_schedules()
        print("The response of SchedulesApi->schedules_controller_get_my_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->schedules_controller_get_my_schedules: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Schedule]**](Schedule.md)

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

