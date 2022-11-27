from openapi_server.service.validation import validate_parameters
from openapi_server.models.error import Error


def test_validate_parameters_with_valid_jurisdiction_code():
    result = validate_parameters(jurisdiction_code="uk", company_number=1111)
    assert result is None
    result = validate_parameters(jurisdiction_code="uk", company_number=2222)
    assert result is None

    result = validate_parameters(jurisdiction_code="de", company_number=3333)
    assert result is None
    result = validate_parameters(jurisdiction_code="de", company_number=4444)
    assert result is None

    result = validate_parameters(jurisdiction_code="nl", company_number=5555)
    assert result is None
    result = validate_parameters(jurisdiction_code="nl", company_number=6666)
    assert result is None


def test_validate_parameters_with_invalid_uk_company_number():
    result = validate_parameters(jurisdiction_code="uk", company_number=0)

    assert result == Error(
        detail="Unsupported company '0' for 'uk' jurisdiction", status="400"
    )


def test_validate_parameters_with_invalid_de_company_number():
    result = validate_parameters(jurisdiction_code="de", company_number=0)

    assert result == Error(
        detail="Unsupported company '0' for 'de' jurisdiction", status="400"
    )


def test_validate_parameters_with_invalid_de_company_number():
    result = validate_parameters(jurisdiction_code="nl", company_number=0)

    assert result == Error(
        detail="Unsupported company '0' for 'nl' jurisdiction", status="400"
    )
