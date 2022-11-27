from openapi_server.models.error import Error
from typing import Optional


def validate_parameters(jurisdiction_code: str, company_number: int) -> Optional[Error]:
    """
    Validate parameters to satisfy requirement:
        - Any request outside these boundaries will need to throw an error.
    """
    if jurisdiction_code not in ["uk", "nl", "de"]:
        return Error(
            detail=f"Unsupported jurisdiction '{jurisdiction_code}'", status=400
        )

    if jurisdiction_code == "uk" and company_number not in [1111, 2222]:
        return Error(
            detail=f"Unsupported company '{company_number}' for 'uk' jurisdiction",
            status=400,
        )

    if jurisdiction_code == "de" and company_number not in [3333, 4444]:
        return Error(
            detail=f"Unsupported company '{company_number}' for 'de' jurisdiction",
            status=400,
        )

    if jurisdiction_code == "nl" and company_number not in [5555, 6666]:
        return Error(
            detail=f"Unsupported company '{company_number}' for 'nl' jurisdiction",
            status=400,
        )

    return None
