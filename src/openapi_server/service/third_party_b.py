from openapi_server.service.http import get
from openapi_server.models.company import Company
from openapi_server.models.full_date import FullDate
from openapi_server.models.official_address import OfficialAddress
from openapi_server.models.officer import Officer
from typing import Optional

SUPPORTED_JURISDICTION_CODES = ["nl", "de"]


async def get_company_data(
    jurisdiction_code: str, company_number: int
) -> Optional[Company]:
    if jurisdiction_code in SUPPORTED_JURISDICTION_CODES:
        company_data = await get(
            f"https://interview-df854r23.sikoia.com/v1/company-data?"
            f"jurisdictionCode={jurisdiction_code}&companyNumber={company_number}"
        )
        return get_company(company_data)

    return None


def get_company(company_data) -> Company:
    company_number = company_data.get("companyNumber")
    company_name = company_data.get("companyName")
    jurisdiction_code = company_data.get("country")
    # TODO: company_type could be obtained from Third party A
    company_type = None
    # If there is not a dateTo, means the company is inactive
    status = "Inactive" if company_data.get("dateTo") else "Active"
    date_established = get_date(company_data.get("dateFrom"))
    date_dissolved = get_date(company_data.get("dateTo"))
    official_address = get_address(company_data.get("address"))
    officers = [get_officer(person) for person in company_data.get("relatedPersons")]

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


def get_address(address: Optional[str]) -> Optional[OfficialAddress]:
    """
    Address:
        "21a Andreasstraße, Berlin, Germany, 10243"
    """
    if address:
        street, city, country, postcode = address.split(",")
        return OfficialAddress(
            street=street.strip(),
            city=city.strip(),
            country=country.strip(),
            postcode=postcode.strip(),
        )

    return None


def get_date(date: Optional[str]) -> Optional[FullDate]:
    """
    Date:
        "13/11/2014"
    """
    if date:
        day, month, year = date.split("/")
        return FullDate(day=day, month=month, year=year)

    return None


def get_officer(person) -> Officer:
    """
    Person:
        {
          "name": "Tyrion Lannister",
          "dateFrom": "13/11/2014",
          "dateTo": null,
          "type": "Director",
          "birthDate": "12/04/1982",
          "nationality": "Westerosi"
        }
    """
    full_name = person.get("name")
    date_from = get_date(person.get("dateFrom"))
    date_to = get_date(person.get("dateTo"))
    role = person.get("type")
    date_of_birth = get_date(person.get("birthDate"))

    return Officer(
        full_name=full_name,
        date_from=date_from,
        date_to=date_to,
        role=role,
        date_of_birth=date_of_birth,
    )
