# coding: utf-8

from __future__ import annotations
import re
from typing import Optional

from pydantic import BaseModel, Field, validator


class Error(BaseModel):
    """
    Error - a model defined in OpenAPI

        detail: The detail of this Error [Optional].
        status: The status of this Error [Optional].
    """

    detail: Optional[str] = Field(alias="detail", default=None)
    status: Optional[str] = Field(alias="status", default=None)

    @validator("status")
    def status_pattern(cls, value):
        assert value is not None and re.match(r"^[45]\d\d$", value)
        return value


Error.update_forward_refs()
