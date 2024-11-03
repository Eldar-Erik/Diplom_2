import allure
import requests
from src.urls import C_USER, D_USER
from src.request import *


class TestCreateUser:

    @allure.title('Создать уникального пользователя')
    def test_create_user_success(self):
        payload = gen_new_user()
        response = requests.post(C_USER, json=payload)
        assert response.json()["success"] == True

        access_token = response.json()["accessToken"]
        response_delete = requests.delete(D_USER, headers={"Authorization": access_token})
        assert response_delete.json()["message"] == 'User successfully removed'

    @allure.title('Создать пользователя, который уже зарегистрирован')
    def test_create_duplicate_user_false(self):
        payload = gen_reg_user()
        response = requests.post(C_USER, json=payload)
        assert response.status_code == 403
        assert response.json()["message"] == 'User already exists'

    @allure.title('Создать пользователя и не заполнить одно из обязательных полей.')
    def test_create_user_whithout_email_false(self):
        payload = gen_user_whithout_email()
        response = requests.post(C_USER, json=payload)
        assert response.status_code == 403
        assert response.json()["message"] == 'Email, password and name are required fields'
