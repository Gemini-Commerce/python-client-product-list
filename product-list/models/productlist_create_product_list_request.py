# coding: utf-8

"""
    Collection Service

    API for managing collection

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from product-list.models.productlist_localized_text import ProductlistLocalizedText
from product-list.models.protobuf_any import ProtobufAny
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProductlistCreateProductListRequest(BaseModel):
    """
    ProductlistCreateProductListRequest
    """ # noqa: E501
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    code: Optional[StrictStr] = None
    url_key: Optional[ProductlistLocalizedText] = Field(default=None, alias="urlKey")
    entity_type: Optional[StrictStr] = Field(default=None, alias="entityType")
    entity_code: Optional[StrictStr] = Field(default=None, alias="entityCode")
    attributes: Optional[Dict[str, ProtobufAny]] = None
    __properties: ClassVar[List[str]] = ["tenantId", "code", "urlKey", "entityType", "entityCode", "attributes"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProductlistCreateProductListRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of url_key
        if self.url_key:
            _dict['urlKey'] = self.url_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict)
        _field_dict = {}
        if self.attributes:
            for _key in self.attributes:
                if self.attributes[_key]:
                    _field_dict[_key] = self.attributes[_key].to_dict()
            _dict['attributes'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProductlistCreateProductListRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "code": obj.get("code"),
            "urlKey": ProductlistLocalizedText.from_dict(obj.get("urlKey")) if obj.get("urlKey") is not None else None,
            "entityType": obj.get("entityType"),
            "entityCode": obj.get("entityCode"),
            "attributes": dict(
                (_k, ProtobufAny.from_dict(_v))
                for _k, _v in obj.get("attributes").items()
            )
            if obj.get("attributes") is not None
            else None
        })
        return _obj

