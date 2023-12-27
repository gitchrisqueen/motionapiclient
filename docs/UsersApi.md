# openapi_client.UsersApi

All URIs are relative to *https://api.usemotion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_controller_get**](UsersApi.md#users_controller_get) | **GET** /users | List users
[**users_controller_get_me**](UsersApi.md#users_controller_get_me) | **GET** /users/me | Get My User


# **users_controller_get**
> ListUsers users_controller_get(cursor=cursor, workspace_id=workspace_id, team_id=team_id)

List users

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_users import ListUsers
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.usemotion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    cursor = 'cursor_example' # str | Use if a previous request returned a cursor. Will page through results (optional)
    workspace_id = 'workspace_id_example' # str |  (optional)
    team_id = 'team_id_example' # str |  (optional)

    try:
        # List users
        api_response = api_instance.users_controller_get(cursor=cursor, workspace_id=workspace_id, team_id=team_id)
        print("The response of UsersApi->users_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_controller_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Use if a previous request returned a cursor. Will page through results | [optional] 
 **workspace_id** | **str**|  | [optional] 
 **team_id** | **str**|  | [optional] 

### Return type

[**ListUsers**](ListUsers.md)

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

# **users_controller_get_me**
> User users_controller_get_me()

Get My User

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.usemotion.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)

    try:
        # Get My User
        api_response = api_instance.users_controller_get_me()
        print("The response of UsersApi->users_controller_get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_controller_get_me: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

