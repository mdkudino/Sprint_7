import allure
import requests
from endpoints import Endpoints
from urls import Urls

class TestOrderList:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Получаем список заказов и проверяем ответ')
    def test_list_orders_success(self):
        response = requests.get(f'{Urls.QA_SCOOTER_URL}{Endpoints.get_orders_list}')
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title('Проверка получения списка заказов с указанием ID курьера')
    @allure.description('Получаем список заказов и проверяем ответ')
    def test_list_orders_success_for_courier_id(self, courier):
        response = requests.get(f'{Urls.QA_SCOOTER_URL}{Endpoints.get_orders_list}?courierId={courier[1]}')
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title('Проверка получения списка заказов с указанием ID курьера')
    @allure.description('Получаем список заказов и проверяем ответ')
    def test_list_orders_fail_for_inexist_courier_id(self):
        courier_id = 1
        response = requests.get(f'{Urls.QA_SCOOTER_URL}{Endpoints.get_orders_list}?courierId={courier_id}')
        assert response.status_code == 404

