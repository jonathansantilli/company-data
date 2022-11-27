# coding: utf-8

"""
    OpenAPI Company data

    Service to get information about companies across different jurisdictions

    The version of the OpenAPI document: 1.0.0
"""


from fastapi import FastAPI

from openapi_server.apis.company_api import router as CompanyApiRouter

app = FastAPI(
    title="OpenAPI Company data",
    description="Service to get information about companies across different jurisdictions",
    version="1.0.0",
)

app.include_router(CompanyApiRouter)
