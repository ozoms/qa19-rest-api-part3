import requests
from pytest_voluptuous import S
from schemas.user import create_new_user


def test_post_create_user(reqres):
    response = reqres.post("api/users", json={"name": "morpheus", "job": "leader"})

    assert response.status_code == 201
    assert response.json() == S(create_new_user)
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'
