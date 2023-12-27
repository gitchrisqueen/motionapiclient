# openapi_client.TasksApi

All URIs are relative to *https://api.usemotion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_controller_delete_assignee**](TasksApi.md#tasks_controller_delete_assignee) | **DELETE** /tasks/{taskId}/assignee | Unassign a task
[**tasks_controller_delete_task**](TasksApi.md#tasks_controller_delete_task) | **DELETE** /tasks/{taskId} | Delete a Task
[**tasks_controller_get**](TasksApi.md#tasks_controller_get) | **GET** /tasks | List Tasks
[**tasks_controller_get_by_id**](TasksApi.md#tasks_controller_get_by_id) | **GET** /tasks/{taskId} | Retrieve a Task
[**tasks_controller_move_task**](TasksApi.md#tasks_controller_move_task) | **PATCH** /tasks/{taskId}/move | Move Workspace
[**tasks_controller_post**](TasksApi.md#tasks_controller_post) | **POST** /tasks | Create Task
[**tasks_controller_update_task**](TasksApi.md#tasks_controller_update_task) | **PATCH** /tasks/{taskId} | Update a Task


# **tasks_controller_delete_assignee**
> tasks_controller_delete_assignee(task_id)

Unassign a task

<!-- theme: warning -->  > ### Note > > For simplicity, use this endpoint to unassign a task > instead of the generic update task endpoint. > This also prevents bugs and accidental unassignments. 

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Unassign a task
        api_instance.tasks_controller_delete_assignee(task_id)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_controller_delete_assignee: %s\n" % e)
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

# **tasks_controller_delete_task**
> tasks_controller_delete_task(task_id)

Delete a Task

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Delete a Task
        api_instance.tasks_controller_delete_task(task_id)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_controller_delete_task: %s\n" % e)
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

# **tasks_controller_get**
> ListTasks tasks_controller_get(cursor=cursor, label=label, status=status, workspace_id=workspace_id, project_id=project_id, name=name, assignee_id=assignee_id)

List Tasks

<!-- theme: warning -->  > ### Note > > By default, all tasks that are completed are left out unless > specifically filtered for via the status. 

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_tasks import ListTasks
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
    api_instance = openapi_client.TasksApi(api_client)
    cursor = 'cursor_example' # str | Use if a previous request returned a cursor. Will page through results (optional)
    label = 'label_example' # str | Limit tasks returned by label on the task (optional)
    status = 'status_example' # str | Limit tasks returned by the status on the task (optional)
    workspace_id = 'workspace_id_example' # str | The id of the workspace you want tasks from. If not provided, will return tasks from all workspaces the user is a member of. (optional)
    project_id = 'project_id_example' # str | Limit tasks returned to a given project (optional)
    name = 'name_example' # str | Limit tasks returned to those that contain this string. Case in-sensitive (optional)
    assignee_id = 'assignee_id_example' # str | Limit tasks returned to a specific assignee (optional)

    try:
        # List Tasks
        api_response = api_instance.tasks_controller_get(cursor=cursor, label=label, status=status, workspace_id=workspace_id, project_id=project_id, name=name, assignee_id=assignee_id)
        print("The response of TasksApi->tasks_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_controller_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Use if a previous request returned a cursor. Will page through results | [optional] 
 **label** | **str**| Limit tasks returned by label on the task | [optional] 
 **status** | **str**| Limit tasks returned by the status on the task | [optional] 
 **workspace_id** | **str**| The id of the workspace you want tasks from. If not provided, will return tasks from all workspaces the user is a member of. | [optional] 
 **project_id** | **str**| Limit tasks returned to a given project | [optional] 
 **name** | **str**| Limit tasks returned to those that contain this string. Case in-sensitive | [optional] 
 **assignee_id** | **str**| Limit tasks returned to a specific assignee | [optional] 

### Return type

[**ListTasks**](ListTasks.md)

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

# **tasks_controller_get_by_id**
> Task tasks_controller_get_by_id(task_id)

Retrieve a Task

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.task import Task
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
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Retrieve a Task
        api_response = api_instance.tasks_controller_get_by_id(task_id)
        print("The response of TasksApi->tasks_controller_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_controller_get_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**Task**](Task.md)

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

# **tasks_controller_move_task**
> Task tasks_controller_move_task(task_id, move_task)

Move Workspace

### Notes  When moving tasks from one workspace to another, the tasks project, status, and label(s) and assignee will all be reset 

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.move_task import MoveTask
from openapi_client.models.task import Task
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
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    move_task = openapi_client.MoveTask() # MoveTask | 

    try:
        # Move Workspace
        api_response = api_instance.tasks_controller_move_task(task_id, move_task)
        print("The response of TasksApi->tasks_controller_move_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_controller_move_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **move_task** | [**MoveTask**](MoveTask.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Motion_API_Key](../README.md#Motion_API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_controller_post**
> Task tasks_controller_post(task_post)

Create Task

## Description Input  When passing in a task description, the input will be treated as [GitHub Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). 

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.task import Task
from openapi_client.models.task_post import TaskPost
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
    api_instance = openapi_client.TasksApi(api_client)
    task_post = openapi_client.TaskPost() # TaskPost | 

    try:
        # Create Task
        api_response = api_instance.tasks_controller_post(task_post)
        print("The response of TasksApi->tasks_controller_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_controller_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_post** | [**TaskPost**](TaskPost.md)|  | 

### Return type

[**Task**](Task.md)

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

# **tasks_controller_update_task**
> Task tasks_controller_update_task(task_id, task_patch)

Update a Task

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import openapi_client
from openapi_client.models.task import Task
from openapi_client.models.task_patch import TaskPatch
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
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    task_patch = openapi_client.TaskPatch() # TaskPatch | 

    try:
        # Update a Task
        api_response = api_instance.tasks_controller_update_task(task_id, task_patch)
        print("The response of TasksApi->tasks_controller_update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_controller_update_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **task_patch** | [**TaskPatch**](TaskPatch.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Motion_API_Key](../README.md#Motion_API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

