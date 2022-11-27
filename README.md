# Company information

Get multiple information related to a company from a particular jurisdiction

## Requirements

- Python >= 3.9
- Docker & Docker Compose

## Installation & Usage

To run the server, please execute the following from the root directory:

```bash
pip3 install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080
```

and open your browser at `http://localhost:8080/docs/` to see the docs.

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
docker-compose up --build service
```

## Tests

To run the tests locally:

In Docker (Recommended):
```bash
docker-compose up --build test_runner
```

In localhost
```bash
pip3 install pytest
PYTHONPATH=src pytest tests
```

## Docs
Open http://localhost:8080/docs on a browser

## How to call the service
`/v1/company/{jurisdiction_code}/{company_number}`

Example:
```bash
curl -X 'GET' \                                                                                                                                (docker-desktop/default)
  'http://0.0.0.0:8080/v1/company/uk/1111' \
  -H 'accept: application/json'
```

## TODO and known issues
- In the [API test](tests/openapi_server/apis/test_company_api.py) is perform as an integration test, the calls to the server should be mocked.
- Validations are weak, for instance, the names, they can have multiple spaces between name, middle name and last name.
- Some validations are hardcoded just to satisfy the requirements of this exercise, however, it does not scale.
- Code formatting/Auto formatting.
- Establish data contracts between the sources and Sikoia.
- Merge the information from both sources, in case one source has information the other does not.
  - `activities` that comes from third party B
  - `owners` there are different possibilities here, for instance, an owner could also have a role in the company, 
  better talk to product about this case.
  - Officers `nationality` from the third party B
  - `relatedCompanies` from the third party B

## Next Steps
Besides addressing the issues mentioned in the previous section, the following are recommendation in order to consider
this project to be deployed in a Production environment.

- Improve validations: consider wrapping the call to external sources with timeouts, and try-catch.
- Improve developer experience, with no need to rebuild the image to test the code in docker
- Cache the response from the sources
- Persist response from sources (in case the data does not change over the time with too much frequency)
  -In that case, keep the data up to date.
- The third party services (`src/openapi_server/service/third_party_a.py and src/openapi_server/service/third_party_b.py`)
  could implement and interface or similar to generate the expected data view returned to the client.