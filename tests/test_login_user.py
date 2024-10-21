import allure
import requests
from src.urls import L_USER
from src.request import log_user, false_user


class TestLogin:

    @allure.title('логин под существующим пользователем.')
    def test_login_success(self):
        payload = log_user()
        response = requests.post(L_USER, json=payload)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('логин с неверным логином и паролем.')
    def test_login_false(self):
        payload = false_user()
        response = requests.post(L_USER, json=payload)
        assert response.status_code == 401
        assert response.json()["message"] == 'email or password are incorrect'
