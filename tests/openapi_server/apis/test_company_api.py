# coding: utf-8

from fastapi.testclient import TestClient


def test_success_get_company_data(client: TestClient):
    headers = {}
    jurisdiction_code = "uk"
    company_number = 1111

    response = client.request(
        "GET",
        f"/v1/company/{jurisdiction_code}/{company_number}",
        headers=headers,
    )

    assert response.status_code == 200
    assert response.json() == {
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
                "full_name": "Hank Schrader",
                "date_from": {"year": 1992, "month": 7, "day": 25},
                "date_to": None,
                "role": "Director",
                "date_of_birth": {"year": 1960, "month": 4},
            },
            {
                "full_name": "Los Pollos Hermanos",
                "date_from": {"year": 1990, "month": 8, "day": 29},
                "date_to": {"year": 1991, "month": 3, "day": 27},
                "role": "Secretary",
                "date_of_birth": None,
            },
        ],
    }


def test_bad_request_get_company_data(client: TestClient):
    headers = {}
    jurisdiction_code = "uk"
    company_number = 0

    response = client.request(
        "GET",
        f"/v1/company/{jurisdiction_code}/{company_number}",
        headers=headers,
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Unsupported company '0' for 'uk' jurisdiction"
    }
