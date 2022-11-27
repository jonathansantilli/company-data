# coding: utf-8

from typing import List, Optional

from pydantic import BaseModel, Field
from openapi_server.models.full_date import FullDate
from openapi_server.models.officer import Officer
from openapi_server.models.official_address import OfficialAddress


class Company(BaseModel):
    """
    Company - a model defined in OpenAPI

        company_number: The company_number of this Company [Optional].
        company_name: The company_name of this Company [Optional].
        jurisdiction_code: The jurisdiction_code of this Company [Optional].
        company_type: The company_type of this Company [Optional].
        status: The status of this Company [Optional].
        date_established: The date_established of this Company [Optional].
        date_dissolved: The date_dissolved of this Company [Optional].
        official_address: The official_address of this Company [Optional].
        officers: The officers of this Company [Optional].
    """

    company_number: Optional[str] = Field(alias="company_number", default=None)
    company_name: Optional[str] = Field(alias="company_name", default=None)
    jurisdiction_code: Optional[str] = Field(alias="jurisdiction_code", default=None)
    company_type: Optional[str] = Field(alias="company_type", default=None)
    status: Optional[str] = Field(alias="status", default=None)
    date_established: Optional[FullDate] = Field(alias="date_established", default=None)
    date_dissolved: Optional[FullDate] = Field(alias="date_dissolved", default=None)
    official_address: Optional[OfficialAddress] = Field(
        alias="official_address", default=None
    )
    officers: Optional[List[Officer]] = Field(alias="officers", default=None)


Company.update_forward_refs()
