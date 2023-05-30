import requests
from pytest_voluptuous import S
from schemas.resource import resource_list_schema


def test_get_resource_list_schema(reqres):
    result = reqres.get("api/unknown/", params={"page": 2})

    assert S(resource_list_schema) == result.json()


def test_resource_default_count_on_page(reqres):
    response = reqres.get("api/unknown", params={"page": 1})
    per_page = response.json()["per_page"]
    data = response.json()["data"]

    assert per_page == 6
    assert len(data) == 6
