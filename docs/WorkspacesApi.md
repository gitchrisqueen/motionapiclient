# usemotion_api_client.WorkspacesApi

All URIs are relative to *https://api.usemotion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statuses_controller_get**](WorkspacesApi.md#statuses_controller_get) | **GET** /statuses | List statuses for a workspace
[**workspaces_controller_get**](WorkspacesApi.md#workspaces_controller_get) | **GET** /workspaces | List workspaces


# **statuses_controller_get**
> List[Status] statuses_controller_get(workspace_id)

List statuses for a workspace

### Example

* Api Key Authentication (Motion_API_Key):

```python
import time
import os
import usemotion_api_client
from usemotion_api_client.models.status import Status
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
    api_instance = usemotion_api_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List statuses for a workspace
        api_response = api_instance.statuses_controller_get(workspace_id)
        print("The response of WorkspacesApi->statuses_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->statuses_controller_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[Status]**](Status.md)

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

# **workspaces_controller_get**
> ListWorkspaces workspaces_controller_get(cursor=cursor, ids=ids)

List workspaces

### Example

* Api Key Authentication (Motion_API_Key):

```python
import time
import os
import usemotion_api_client
from usemotion_api_client.models.list_workspaces import ListWorkspaces
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
    api_instance = usemotion_api_client.WorkspacesApi(api_client)
    cursor = 'cursor_example' # str | Use if a previous request returned a cursor. Will page through results (optional)
    ids = ['ids_example'] # List[str] |  (optional)

    try:
        # List workspaces
        api_response = api_instance.workspaces_controller_get(cursor=cursor, ids=ids)
        print("The response of WorkspacesApi->workspaces_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->workspaces_controller_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Use if a previous request returned a cursor. Will page through results | [optional] 
 **ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ListWorkspaces**](ListWorkspaces.md)

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

