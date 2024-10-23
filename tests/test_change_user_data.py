import allure
import requests
from src.urls import D_USER
from src.request import update_user


class TestChangeUserData:

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_change_reg_user_success(self, new_user):
        access_token = new_user["access_token"]
        update_data = update_user()
        response_update = requests.patch(D_USER, json=update_data, headers={"Authorization": access_token})
        assert response_update.json()["success"] == True
        assert response_update.json()["user"]["email"] == update_data["email"]
        assert response_update.json()["user"]["name"] == update_data["name"]

    @allure.title('Изменение данных пользователя без авторизации')
    def test_change_unreg_user_failture(self):
        update_data = update_user()
        response_update = requests.patch(D_USER, json=update_data)
        assert response_update.status_code == 401
        assert response_update.json()["success"] == False
        assert response_update.json()["message"] == "You should be authorised"
