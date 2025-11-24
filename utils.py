import allure
from faker import Faker
import requests

from endpoints import Endpoints
from urls import Urls


class CourierDataGenerator:
    
    @staticmethod
    @allure.step("Генерируем валидные фейковые данные для создания курьера")
    def generate_fake_valid_courier_data():
        fake = Faker("ru_RU")
        login = fake.user_name()
        password = fake.password()
        firstname = fake.first_name()
        data = {
            "login": login,
            "firstName": firstname,
            "password": password
        }

        return data

    @staticmethod
    @allure.step("Генерируем невалидные фейковые данные (пустая строка) для создания курьера")
    def generate_fake_invalid_courier_data_empty_field(data_empty):
        fake = Faker("ru_RU")
        login = fake.user_name()
        firstname = fake.first_name()
        password = fake.password()
        data = {
            "login": "" if data_empty == "login" else login,
            "firstName": firstname,
            "password": "" if data_empty == "password" else password
        }

        return data

    @staticmethod
    @allure.step("Генерируем невалидные фейковые данные (отсутствуют обязательные поля) для создания курьера")
    def generate_fake_invalid_courier_data_no_field(contained_data):
        fake = Faker("ru_RU")
        firstname = fake.first_name()
        data = {"firstName": firstname}
        if "login" in contained_data:
            login = fake.user_name()
            data["login"] = login
        if "password" in contained_data:
            password = fake.password()
            data["password"] = password

        return data

    @staticmethod
    @allure.step("Генерируем невалидные данные для несуществующего курьера")
    def generate_null_invalid_courier_data():
        return {"login": "test", "password": "test"}

class CourierUtils:

    @staticmethod
    @allure.step("Отправляем запрос на создание курьера")
    def create_courier(courier_data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)
        return response
    
    @staticmethod
    @allure.step("Отправляем запрос на логин курьера")
    def login_courier(courier_data):
        login_response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=courier_data)
        return login_response

    @staticmethod
    @allure.step("Получаем ID курьера")
    def get_courier_id(login_response):
        return login_response.json().get("id")

    @staticmethod
    @allure.step("Отправляем запрос на удаление курьера")
    def delete_courier(courier_id):
        del_response = requests.delete(f'{Urls.QA_SCOOTER_URL}{Endpoints.delete_courier}{courier_id}')
        return del_response
