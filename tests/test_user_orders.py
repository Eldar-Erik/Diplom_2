import allure
import requests
from src.urls import C_ORDER


class TestUserOrder:
    @allure.title('Получение заказов авторизованного пользователя')
    def test_order_reg_user(self, login_user):
        access_token = login_user
        response_order = requests.get(C_ORDER, headers={"Authorization": access_token})
        assert response_order.json()["success"] == True

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_order_unreg_user(self):
        response_order = requests.get(C_ORDER)
        assert (response_order.json()["success"] == False and
                response_order.json()["message"] == 'You should be authorised')
