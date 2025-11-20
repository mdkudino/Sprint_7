import json
import allure
import pytest
import requests
from data import DataOrder
from endpoints import Endpoints
from urls import Urls


class TestOrder:

    @allure.title('Проверка создания заказа')
    @allure.description('Отправляем запрос на создание заказа с разными цветами, проверяем ответ')
    @pytest.mark.parametrize('color', 
                             [["BLACK"], 
                              ["GREY"], 
                              ["BLACK", "GRAY"],
                              [""]])
    def test_create_order_success(self, color):
        headers = {"Content-type": "application/json"}
        data = DataOrder.data
        data["color"] = color
        data = json.dumps(data)

        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_order}', headers=headers, data=data)
        assert response.status_code == 201
        assert "track" in response.text