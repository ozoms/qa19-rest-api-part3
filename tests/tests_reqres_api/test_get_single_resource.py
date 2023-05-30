import requests
from dotenv import load_dotenv
from pytest_voluptuous import S
from schemas.resource import single_resource


def test_get_resource_schema(reqres):
    response = reqres.get('api/unknown/2')

    assert response.status_code == 200
    assert S(single_resource) == response.json()
