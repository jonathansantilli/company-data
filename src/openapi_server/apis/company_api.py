# coding: utf-8

from fastapi import APIRouter, Path, HTTPException

from openapi_server.models.company import Company
from openapi_server.models.error import Error
from openapi_server.service import validation
from openapi_server.service import third_party_a, third_party_b


router = APIRouter()


@router.get(
    "/v1/company/{jurisdiction_code}/{company_number}",
    responses={
        200: {"model": Company, "description": "Successful Response"},
        400: {
            "model": Error,
            "description": "Bad request, Invalid jurisdiction or company identifier",
        },
        422: {"model": Error, "description": "Validation Error"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["company"],
    summary="Get company data by jurisdiction",
    response_model_by_alias=True,
)
async def get_company_data(
    jurisdiction_code: str = Path(None, description="The jurisdiction identifier"),
    company_number: int = Path(None, description="The company identifier"),
) -> Company or HTTPException:
    """Get multiple information related to a company from a particular jurisdiction"""
    error = validation.validate_parameters(jurisdiction_code, company_number)
    if error:
        raise HTTPException(detail=error.detail, status_code=int(error.status))

    # TODO: These API calls should be perform in parallel
    company_from_third_party_a = await third_party_a.get_company_data(
        jurisdiction_code, company_number
    )
    if company_from_third_party_a:
        return company_from_third_party_a

    company_from_third_party_b = await third_party_b.get_company_data(
        jurisdiction_code, company_number
    )
    if company_from_third_party_b:
        return company_from_third_party_b

    # TODO: merge the information from both sources, in case one source has information the other does not.

    return HTTPException(
        detail=f"Information for company {company_number} "
        f"in {jurisdiction_code} jurisdiction not found",
        status_code=404,
    )
