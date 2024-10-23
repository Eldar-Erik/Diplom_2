import allure
import requests
from src.urls import C_ORDER
from src.helpers import order_data, order_data_empty, order_data_false

class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_auth_success(self, login_user):
        access_token = login_user
        order = order_data()
        response_order = requests.post(C_ORDER, json=order, headers={"Authorization": access_token})
        assert (response_order.json()["success"] == True and
                response_order.json()["order"]["number"] is not '')

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth_success(self):
        order = order_data()
        response_order = requests.post(C_ORDER, json=order)
        assert (response_order.json()["success"] == True and
                response_order.json()["order"]["number"] is not '')

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_ingridients_success(self):
        order = order_data()
        response_order = requests.post(C_ORDER, json=order)
        assert (response_order.json()["success"] == True and
                response_order.json()["order"]["number"] is not '')

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_no_ingridients_success(self):
        order = order_data_empty()
        response_order = requests.post(C_ORDER, json=order)
        assert (response_order.status_code == 400 and
                response_order.json()["success"] == False and
                response_order.json()["message"] == "Ingredient ids must be provided")

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_cach_success(self):
        order = order_data_false()
        response_order = requests.post(C_ORDER, json=order)
        assert response_order.status_code == 500
