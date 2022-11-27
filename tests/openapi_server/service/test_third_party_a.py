from openapi_server.service.third_party_a import (
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
    date = {"year": 2000, "month": 9, "day": 16}

    result = get_date(date)

    assert result == FullDate(year=2000, month=9, day=16)


def test_get_date_without_value():
    date = None

    result = get_date(date)

    assert result is None


def test_get_address_with_value():
    address = {
        "street": "87 New Road",
        "city": "London",
        "country": "United Kingdom",
        "postcode": "WC73 1SN",
    }

    result = get_address(address)

    assert result == OfficialAddress(
        street="87 New Road",
        city="London",
        country="United Kingdom",
        postcode="WC73 1SN",
    )


def test_get_address_without_value():
    address = None

    result = get_address(address)

    assert result is None


def test_get_officer_with_name():
    person = {
        "name": "Michael Jackson",
        "date_from": {"year": 2000, "month": 9, "day": 16},
        "date_to": {"year": 2020, "month": 6, "day": 3},
        "role": "Managing Director",
        "date_of_birth": {"year": 1988, "month": 9},
    }

    result = get_officer(person)

    assert result == Officer(
        full_name="Michael Jackson",
        date_from=FullDate(year=2000, month=9, day=16),
        date_to=FullDate(year=2020, month=6, day=3),
        role="Managing Director",
        date_of_birth=PartialDate(year=1988, month=9),
    )


def test_get_officer_with_middlename():
    person = {
        "first_name": "Jason",
        "middlenames": "Gary",
        "last_name": "Scott",
        "date_from": {"year": 2000, "month": 9, "day": 16},
        "date_to": {"year": 2020, "month": 6, "day": 3},
        "role": "Managing Director",
        "date_of_birth": {"year": 1988, "month": 9},
    }

    result = get_officer(person)

    assert result == Officer(
        full_name="Jason Gary Scott",
        date_from=FullDate(year=2000, month=9, day=16),
        date_to=FullDate(year=2020, month=6, day=3),
        role="Managing Director",
        date_of_birth=PartialDate(year=1988, month=9),
    )


def test_get_officer_with_first_name_and_last_name():
    person = {
        "first_name": "Will",
        "last_name": "Smith",
        "date_from": {"year": 2000, "month": 9, "day": 16},
        "date_to": {"year": 2020, "month": 6, "day": 3},
        "role": "Managing Director",
        "date_of_birth": {"year": 1988, "month": 9},
    }

    result = get_officer(person)

    assert result == Officer(
        full_name="Will Smith",
        date_from=FullDate(year=2000, month=9, day=16),
        date_to=FullDate(year=2020, month=6, day=3),
        role="Managing Director",
        date_of_birth=PartialDate(year=1988, month=9),
    )


def test_get_company():
    company_data = {
        "company_number": "1111",
        "company_name": "Breaking Bad Ltd",
        "jurisdiction_code": "uk",
        "company_type": "Ltd",
        "status": "Active",
        "date_established": None,
        "date_dissolved": None,
        "official_address": {
            "street": "87 New Road",
            "city": "London",
            "country": "United Kingdom",
            "postcode": "WC73 1SN",
        },
        "officers": [
            {
                "first_name": "Hank",
                "last_name": "Schrader",
                "date_from": {"year": 1992, "month": 7, "day": 25},
                "date_to": None,
                "role": "Director",
                "date_of_birth": {"year": 1960, "month": 4},
            },
            {
                "name": "Los Pollos Hermanos",
                "date_from": {"year": 1990, "month": 8, "day": 29},
                "date_to": {"year": 1991, "month": 3, "day": 27},
                "role": "Secretary",
            },
        ],
        "owners": [
            {
                "first_name": "Walter",
                "last_name": "White",
                "date_from": {"year": 1985, "month": 12, "day": 20},
                "date_to": None,
                "ownership_type": "Shareholder",
                "shares_held": 80,
                "date_of_birth": {"year": 1955, "month": 7},
            },
            {
                "first_name": "Jessie",
                "last_name": "Pinkman",
                "date_from": {"year": 1999, "month": 5, "day": 22},
                "date_to": None,
                "ownership_type": "Shareholder",
                "shares_held": 20,
                "date_of_birth": {"year": 1992, "month": 11},
            },
        ],
    }

    result = get_company(company_data)

    assert result == Company(
        company_number="1111",
        company_name="Breaking Bad Ltd",
        jurisdiction_code="uk",
        company_type="Ltd",
        status="Active",
        date_established=None,
        date_dissolved=None,
        official_address=OfficialAddress(
            street="87 New Road",
            city="London",
            country="United Kingdom",
            postcode="WC73 1SN",
        ),
        officers=[
            Officer(
                full_name="Hank Schrader",
                date_from=FullDate(year=1992, month=7, day=25),
                date_to=None,
                role="Director",
                date_of_birth=PartialDate(year=1960, month=4),
            ),
            Officer(
                full_name="Los Pollos Hermanos",
                date_from=FullDate(year=1990, month=8, day=29),
                date_to=FullDate(year=1991, month=3, day=27),
                role="Secretary",
                date_of_birth=None,
            ),
        ],
    )
