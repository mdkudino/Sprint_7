import allure
import pytest
from utils import CourierDataGenerator, CourierUtils

class TestCreateCourier:

    
    @allure.title('Проверка ручки создания нового курьера')
    @allure.description('Отправляем запрос на создание курьера, проверяем ответ и удаляем созданного курьера')
    def test_registration_courier_successfull_with_valid_data(self):
        courier_data = CourierDataGenerator.generate_fake_valid_courier_data()
        response = CourierUtils.create_courier(courier_data)

        assert response.status_code == 201
        assert "ok" in response.text

        login_resp = CourierUtils.login_courier(courier_data)
        courier_id = CourierUtils.get_courier_id(login_resp)

        CourierUtils.delete_courier(courier_id)

    @allure.title('Проверка ошибки при создании двух одинаковых курьеров')
    @allure.description('Отправляем повторный запрос на создание курьера, проверяем ответ и удаляем курьера')
    def test_registration_double_courier_failed(self):
        courier_data = CourierDataGenerator.generate_fake_valid_courier_data()
        response = CourierUtils.create_courier(courier_data)

        assert response.status_code == 201
        assert "ok" in response.text

        response_second = CourierUtils.create_courier(courier_data)

        assert response_second.status_code == 409
        assert "Этот логин уже используется" in response_second.text
        
        login_resp = CourierUtils.login_courier(courier_data)
        courier_id = CourierUtils.get_courier_id(login_resp)

        CourierUtils.delete_courier(courier_id)

    @allure.title('Проверка ошибки при создании курьера без обязательных полей (пустые строки)')
    @allure.description('Отправляем запрос без обязательных полей и проверяем ошибку')
    @pytest.mark.parametrize('data_empty', [
        "login", 
        "password"
    ])
    def test_courier_registration_empty_parameters_failed(self, data_empty):
        courier_data = CourierDataGenerator.generate_fake_invalid_courier_data_empty_field(data_empty)
        response = CourierUtils.create_courier(courier_data)
    
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text

    @allure.title('Проверка ошибки при создании курьера с отсутствующими обязательными полями')
    @allure.description('Отправляем запрос без обязательных полей и проверяем ошибку')
    @pytest.mark.parametrize('contained_data', [
        ["login"], 
        ["password"]
    ])
    def test_courier_registration_without_parameters_failed(self, contained_data):
        courier_data = CourierDataGenerator.generate_fake_invalid_courier_data_no_field(contained_data)
        response = CourierUtils.create_courier(courier_data)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text
