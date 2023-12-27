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

from pydantic import BaseModel, Field, StrictStr


class DailySchedule(BaseModel):
    """
    DailySchedule
    """
    start: StrictStr = Field(..., description="24 hour time format. HH:mm")
    end: StrictStr = Field(..., description="24 hour time format. HH:mm")
    __properties = ["start", "end"]

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
    def from_json(cls, json_str: str) -> DailySchedule:
        """Create an instance of DailySchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DailySchedule:
        """Create an instance of DailySchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DailySchedule.parse_obj(obj)

        _obj = DailySchedule.parse_obj({
            "start": obj.get("start"),
            "end": obj.get("end")
        })
        return _obj
