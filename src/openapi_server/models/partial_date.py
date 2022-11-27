# coding: utf-8

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class PartialDate(BaseModel):
    """
    PartialDate - a model defined in OpenAPI

        year: The year of this PartialDate [Optional].
        month: The month of this PartialDate [Optional].
    """

    year: Optional[int] = Field(alias="year", default=None)
    month: Optional[int] = Field(alias="month", default=None)


PartialDate.update_forward_refs()
