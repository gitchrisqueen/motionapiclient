# coding: utf-8

"""
    Motion REST API

    <!-- theme: warning -->  > ### Rate Limit Information > > The Motion API is currently rate limited to 12 requests per minute per user. In the event a user exceeds this rate limit 3 times > in a singe 24 hour period, their API access will be disabled and will require that they contact support to have it re-enabled.  <!-- theme: info -->  > ### Note on Date Formats > > All dates that the Motion API works with are in the format of ISO 8601. **Motion will always return dates in UTC.** 

    The version of the OpenAPI document: 1.0.0
    Contact: christopher.queen@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from usemotion_api_client.models.meta_result import MetaResult
from usemotion_api_client.models.task import Task


class ListTasks(BaseModel):
    """
    ListTasks
    """
    tasks: conlist(Task) = Field(...)
    meta: Optional[MetaResult] = None
    __properties = ["tasks", "meta"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ListTasks:
        """Create an instance of ListTasks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tasks (list)
        _items = []
        if self.tasks:
            for _item in self.tasks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListTasks:
        """Create an instance of ListTasks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListTasks.parse_obj(obj)

        _obj = ListTasks.parse_obj({
            "tasks": [Task.from_dict(_item) for _item in obj.get("tasks")]
            if obj.get("tasks") is not None else None,
            "meta":
            MetaResult.from_dict(obj.get("meta"))
            if obj.get("meta") is not None else None
        })
        return _obj
