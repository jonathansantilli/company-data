# coding: utf-8

from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, Field
from openapi_server.models.full_date import FullDate
from openapi_server.models.partial_date import PartialDate


class Officer(BaseModel):
    """
    Officer - a model defined in OpenAPI

        full_name: The full_name of this Officer [Optional].
        date_from: The date_from of this Officer [Optional].
        date_to: The date_to of this Officer [Optional].
        role: The role of this Officer [Optional].
        date_of_birth: The date_of_birth of this Officer [Optional].
    """

    full_name: Optional[str] = Field(alias="full_name", default=None)
    date_from: Optional[FullDate] = Field(alias="date_from", default=None)
    date_to: Optional[FullDate] = Field(alias="date_to", default=None)
    role: Optional[str] = Field(alias="role", default=None)
    date_of_birth: Optional[PartialDate] = Field(alias="date_of_birth", default=None)


Officer.update_forward_refs()
