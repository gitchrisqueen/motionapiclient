# usemotion_api_client.CommentsApi

All URIs are relative to *https://api.usemotion.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_controller_get_comments**](CommentsApi.md#comments_controller_get_comments) | **GET** /comments | List Comments
[**comments_controller_post_comment**](CommentsApi.md#comments_controller_post_comment) | **POST** /comments | Create Comment


# **comments_controller_get_comments**
> ListComments comments_controller_get_comments(task_id, cursor=cursor)

List Comments

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import usemotion_api_client
from usemotion_api_client.models.list_comments import ListComments
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
    api_instance = usemotion_api_client.CommentsApi(api_client)
    task_id = 'task_id_example' # str | 
    cursor = 'cursor_example' # str | Use if a previous request returned a cursor. Will page through results (optional)

    try:
        # List Comments
        api_response = api_instance.comments_controller_get_comments(task_id, cursor=cursor)
        print("The response of CommentsApi->comments_controller_get_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_controller_get_comments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **cursor** | **str**| Use if a previous request returned a cursor. Will page through results | [optional] 

### Return type

[**ListComments**](ListComments.md)

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

# **comments_controller_post_comment**
> Comment comments_controller_post_comment(comment_post)

Create Comment

## Comment Content Input  When posting a comment, the content will be treated as [GitHub Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). 

### Example

* Api Key Authentication (Motion_API_Key):
```python
import time
import os
import usemotion_api_client
from usemotion_api_client.models.comment import Comment
from usemotion_api_client.models.comment_post import CommentPost
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
    api_instance = usemotion_api_client.CommentsApi(api_client)
    comment_post = usemotion_api_client.CommentPost() # CommentPost | 

    try:
        # Create Comment
        api_response = api_instance.comments_controller_post_comment(comment_post)
        print("The response of CommentsApi->comments_controller_post_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_controller_post_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_post** | [**CommentPost**](CommentPost.md)|  | 

### Return type

[**Comment**](Comment.md)

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

