from openapi_server.service.http import get
from openapi_server.models.company import Company
from openapi_server.models.full_date import FullDate
from openapi_server.models.official_address import OfficialAddress
from openapi_server.models.officer import Officer
from typing import Optional

SUPPORTED_JURISDICTION_CODES = ["uk", "de"]


async def get_company_data(
    jurisdiction_code: str, company_number: int
) -> Optional[Company]:
    if jurisdiction_code in SUPPORTED_JURISDICTION_CODES:
        company_data = await get(
            f"https://interview-df854r23.sikoia.com/v1/company/"
            f"{jurisdiction_code}/{company_number}"
        )
        return get_company(company_data)

    return None


def get_date(date) -> Optional[FullDate]:
    """
    Date:
        {
            "year": 2000,
            "month": 9,
            "day": 16
        }
    """
    if date:
        return FullDate(**date)

    return None


def get_address(address) -> Optional[OfficialAddress]:
    """
    Address:
        {
            "street": "87 New Road",
            "city": "London",
            "country": "United Kingdom",
            "postcode": "WC73 1SN"
        }
    """
    if address:
        return OfficialAddress(**address)

    return None


def get_officer(person) -> Officer:
    """
    Person:
        {
          "first_name": "Michael",
          "middlenames": "Gary",
          "last_name": "Scott",
          "date_from": {
            "year": 2000,
            "month": 9,
            "day": 16
          },
          "date_to": {
            "year": 2020,
            "month": 6,
            "day": 3
          },
          "role": "Managing Director",
          "date_of_birth": {
            "year": 1988,
            "month": 9
          }
        }
    """
    if person.get("name"):
        full_name = person.get("name")
    elif person.get("middlenames"):
        full_name = (
            f"{person.get('first_name')} "
            f"{person.get('middlenames')} "
            f"{person.get('last_name')}"
        )
    else:
        full_name = f"{person.get('first_name')} {person.get('last_name')}"
    date_from = get_date(person.get("date_from"))
    date_to = get_date(person.get("date_to"))
    role = person.get("role")
    date_of_birth = get_date(person.get("date_of_birth"))

    return Officer(
        full_name=full_name,
        date_from=date_from,
        date_to=date_to,
        role=role,
        date_of_birth=date_of_birth,
    )


def get_company(company_data) -> Company:
    company_number = company_data.get("company_number")
    company_name = company_data.get("company_name")
    jurisdiction_code = company_data.get("jurisdiction_code")
    company_type = company_data.get("company_type")
    status = company_data.get("status")
    date_established = get_date(company_data.get("date_established"))
    date_dissolved = get_date(company_data.get("date_dissolved"))
    official_address = get_address(company_data.get("official_address"))
    officers = [get_officer(person) for person in company_data.get("officers")]

    return Company(
        company_number=company_number,
        company_name=company_name,
        jurisdiction_code=jurisdiction_code,
        company_type=company_type,
        status=status,
        date_established=date_established,
        date_dissolved=date_dissolved,
        official_address=official_address,
        officers=officers,
    )
