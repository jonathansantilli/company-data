# coding: utf-8

from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, Field


class OfficialAddress(BaseModel):
    """
    OfficialAddress - a model defined in OpenAPI

        street: The street of this OfficialAddress [Optional].
        city: The city of this OfficialAddress [Optional].
        country: The country of this OfficialAddress [Optional].
        postcode: The postcode of this OfficialAddress [Optional].
    """

    street: Optional[str] = Field(alias="street", default=None)
    city: Optional[str] = Field(alias="city", default=None)
    country: Optional[str] = Field(alias="country", default=None)
    postcode: Optional[str] = Field(alias="postcode", default=None)


OfficialAddress.update_forward_refs()
