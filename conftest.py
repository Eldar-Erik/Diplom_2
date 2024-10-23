import pytest
import requests
from src.urls import C_USER, D_USER
from src.request import gen_new_user


@pytest.fixture
def new_user():
    payload = gen_new_user()
    response = requests.post(C_USER, json=payload)
    assert response.json()["success"] == True
    access_token = response.json()["accessToken"]
    user = {
        "access_token": access_token,
        "email": response.json()["user"]["email"],
        "name": response.json()["user"]["name"]
        }
    yield user

    response_delete = requests.delete(D_USER, headers={"Authorization": access_token})
    assert response_delete.json()["message"] == "User successfully removed"

