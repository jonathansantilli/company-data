from openapi_server.service.third_party_b import (
    get_date,
    get_address,
    get_officer,
    get_company,
)
from openapi_server.models.full_date import FullDate
from openapi_server.models.official_address import OfficialAddress
from openapi_server.models.officer import Officer
from openapi_server.models.partial_date import PartialDate
from openapi_server.models.company import Company


def test_get_date_with_value():
    date = "13/11/2014"

    result = get_date(date)

    assert result == FullDate(year=2014, month=11, day=13)


def test_get_date_without_value():
    date = None

    result = get_date(date)

    assert result is None


def test_get_address_with_value():
    address = "21a Andreasstraße, Berlin, Germany, 10243"

    result = get_address(address)

    assert result == OfficialAddress(
        street="21a Andreasstraße", city="Berlin", country="Germany", postcode="10243"
    )


def test_get_address_without_value():
    address = None

    result = get_address(address)

    assert result is None


def test_get_officer_with_name():
    person = {
        "name": "Tyrion Lannister",
        "dateFrom": "13/11/2014",
        "dateTo": None,
        "type": "Director",
        "birthDate": "12/04/1982",
        "nationality": "Westerosi",
    }

    result = get_officer(person)

    assert result == Officer(
        full_name="Tyrion Lannister",
        date_from=FullDate(year=2014, month=11, day=13),
        date_to=None,
        role="Director",
        date_of_birth=PartialDate(year=1982, month=4),
    )


def test_get_company():
    company_data = {
        "companyNumber": "3333",
        "companyName": "Game of Thrones GmbH",
        "country": "de",
        "dateFrom": "22/01/2011",
        "dateTo": None,
        "address": "21a Andreasstraße, Berlin, Germany, 10243",
        "activities": [
            {"activityCode": 2244, "activityDescription": "Software"},
            {"activityCode": 2266, "activityDescription": "Technology"},
        ],
        "relatedPersons": [
            {
                "name": "Tyrion Lannister",
                "dateFrom": "13/11/2014",
                "dateTo": None,
                "type": "Director",
                "birthDate": "12/04/1982",
                "nationality": "Westerosi",
            },
            {
                "name": "Sansa Stark",
                "dateFrom": "05/09/2012",
                "dateTo": None,
                "type": "Owner",
                "ownership": "40.0",
                "birthDate": "12/04/1982",
                "nationality": "Westerosi",
            },
        ],
        "relatedCompanies": [
            {
                "name": "Iron Bank of Braavos Ltd",
                "dateFrom": "14/07/2012",
                "dateTo": "21/06/2019",
                "type": "Director",
                "country": "Braavos",
            },
            {
                "name": "The Golden Company Plc",
                "dateFrom": "07/11/2014",
                "dateTo": None,
                "type": "Owner",
                "ownership": "60.0",
                "country": "Pentos",
            },
        ],
    }

    result = get_company(company_data)

    assert result == Company(
        company_number="3333",
        company_name="Game of Thrones GmbH",
        jurisdiction_code="de",
        company_type=None,
        status="Active",
        date_established=FullDate(year=2011, month=1, day=22),
        date_dissolved=None,
        official_address=OfficialAddress(
            street="21a Andreasstraße",
            city="Berlin",
            country="Germany",
            postcode="10243",
        ),
        officers=[
            Officer(
                full_name="Tyrion Lannister",
                date_from=FullDate(year=2014, month=11, day=13),
                date_to=None,
                role="Director",
                date_of_birth=PartialDate(year=1982, month=4),
            ),
            Officer(
                full_name="Sansa Stark",
                date_from=FullDate(year=2012, month=9, day=5),
                date_to=None,
                role="Owner",
                date_of_birth=PartialDate(year=1982, month=4),
            ),
        ],
    )
