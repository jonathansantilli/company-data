# coding: utf-8

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FullDate(BaseModel):
    """
    FullDate - a model defined in OpenAPI

        year: The year of this FullDate [Optional].
        month: The month of this FullDate [Optional].
        day: The day of this FullDate [Optional].
    """

    year: Optional[int] = Field(alias="year", default=None)
    month: Optional[int] = Field(alias="month", default=None)
    day: Optional[int] = Field(alias="day", default=None)


FullDate.update_forward_refs()
