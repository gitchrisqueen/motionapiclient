# coding: utf-8

"""
    Motion REST API

    <!-- theme: warning -->  > ### Rate Limit Information > > The Motion API is currently rate limited to 12 requests per minute per user. In the event a user exceeds this rate limit 3 times > in a singe 24 hour period, their API access will be disabled and will require that they contact support to have it re-enabled.  <!-- theme: info -->  > ### Note on Date Formats > > All dates that the Motion API works with are in the format of ISO 8601. **Motion will always return dates in UTC.** 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.list_projects import ListProjects

class TestListProjects(unittest.TestCase):
    """ListProjects unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListProjects:
        """Test ListProjects
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListProjects`
        """
        model = ListProjects()
        if include_optional:
            return ListProjects(
                projects = [
                    openapi_client.models.project.Project(
                        id = '', 
                        name = '', 
                        description = '', 
                        workspace_id = '', )
                    ],
                meta = openapi_client.models.meta_result.MetaResult(
                    next_cursor = '', 
                    page_size = 1.337, )
            )
        else:
            return ListProjects(
                projects = [
                    openapi_client.models.project.Project(
                        id = '', 
                        name = '', 
                        description = '', 
                        workspace_id = '', )
                    ],
        )
        """

    def testListProjects(self):
        """Test ListProjects"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
