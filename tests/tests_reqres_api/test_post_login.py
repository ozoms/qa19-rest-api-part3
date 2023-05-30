import requests
from pytest_voluptuous import S
from schemas.login import login


def test_post_login(reqres):
    response = reqres.post("api/login",
                             json={"email": "eve.holt@reqres.in", "password": "cityslicka"})

    assert response.status_code == 200
    assert response.json() == S(login)
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'
