import pytest
import requests
from src.urls import C_USER, D_USER, L_USER
from src.request import gen_new_user, log_user


@pytest.fixture
def new_user():
    payload = gen_new_user()
    response = requests.post(C_USER, json=payload)
    assert response.json()["success"] == True
    access_token = response.json()["accessToken"]
    yield access_token

    response_delete = requests.delete(D_USER, headers={"Authorization": access_token})
    assert response_delete.json()["message"] == "User successfully removed"

@pytest.fixture
def login_user():
    payload = log_user()
    response = requests.post(L_USER, json=payload)
    assert response.status_code == 200
    access_token = response.json()["accessToken"]
    yield access_token
