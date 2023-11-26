# openapi_client.ProjectsApi

All URIs are relative to *https://api.usemotion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_controller_get**](ProjectsApi.md#projects_controller_get) | **GET** /projects | List Projects
[**projects_controller_get_single_project**](ProjectsApi.md#projects_controller_get_single_project) | **GET** /projects/{projectId} | Retrieve Project
[**projects_controller_post**](ProjectsApi.md#projects_controller_post) | **POST** /projects | Create Project


# **projects_controller_get**
> ListProjects projects_controller_get(workspace_id, cursor=cursor)

List Projects

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_projects import ListProjects
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
    api_instance = openapi_client.ProjectsApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    cursor = 'cursor_example' # str | Use if a previous request returned a cursor. Will page through results (optional)

    try:
        # List Projects
        api_response = api_instance.projects_controller_get(workspace_id, cursor=cursor)
        print("The response of ProjectsApi->projects_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_controller_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **cursor** | **str**| Use if a previous request returned a cursor. Will page through results | [optional] 

### Return type

[**ListProjects**](ListProjects.md)

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

# **projects_controller_get_single_project**
> Project projects_controller_get_single_project(project_id)

Retrieve Project

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.project import Project
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Retrieve Project
        api_response = api_instance.projects_controller_get_single_project(project_id)
        print("The response of ProjectsApi->projects_controller_get_single_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_controller_get_single_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**Project**](Project.md)

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

# **projects_controller_post**
> Project projects_controller_post(project_post)

Create Project

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.project import Project
from openapi_client.models.project_post import ProjectPost
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_post = openapi_client.ProjectPost() # ProjectPost | 

    try:
        # Create Project
        api_response = api_instance.projects_controller_post(project_post)
        print("The response of ProjectsApi->projects_controller_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_controller_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_post** | [**ProjectPost**](ProjectPost.md)|  | 

### Return type

[**Project**](Project.md)

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

