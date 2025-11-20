import allure
import pytest
import requests
from utils import CourierDataGenerator, CourierUtils
from endpoints import Endpoints
from urls import Urls


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера с валидными данными')
    @allure.description('Отправляем запрос на авторизацию в сервисе, проверяем ответ и удаляем курьера')
    def test_courier_login_successfull_with_valid_data(self, courier):
        response = CourierUtils.login_courier(courier[0])
        assert response.status_code == 200
        assert response.json()["id"]

    @allure.title('Проверка ошибки при авторизации курьера без заполнения обязательных полей Login/Password')
    @allure.description('Отправляем запрос на авторизацию в сервисе без заполнения обязательных полей Login/Password \
                        и проверяем ответ')
    @pytest.mark.parametrize('contained_data', [
        ["login"], 
        ["password"]
    ])
    def test_courier_login_without_parameters_failed(self, courier, contained_data):
        login_data = courier[0]
        if not 'login' in contained_data:
            login_data['login'] = ""
        if not 'password' in contained_data:
            login_data['password'] = ""
        print(login_data)
        response = CourierUtils.login_courier(login_data)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text

    @allure.title('Проверка ошибки при авторизации курьера с несуществующими данными')
    @allure.description('Отправляем запрос на авторизацию в сервисе с несуществующими данными и проверяем ответ')
    def test_courier_null_login_failed(self):
        null_data = CourierDataGenerator.generate_null_invalid_courier_data()
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=null_data)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text