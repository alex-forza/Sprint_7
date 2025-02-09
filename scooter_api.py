import requests
import allure
from data import Urls
from data import Api
from helpers import DataGeneration

class CourierMethods:
    @staticmethod
    @allure.step("Создание нового курьера")
    def create_courier(data_payload):
        response = requests.post(Urls.url + Api.api_create_courier, data=data_payload)
        return response

    @staticmethod
    @allure.step("Повторное создание курьера (дублирование)")
    def dublicate_create_courier(data_payload):
        requests.post(Urls.url + Api.api_create_courier, data=data_payload)
        response_two = requests.post(Urls.url + Api.api_create_courier, data=data_payload)
        return response_two

    @staticmethod
    @allure.step("Попытка создания курьера без одного обязательного поля")
    def not_once_required_field():
        data_login = DataGeneration.register_new_courier_and_return_login_password()["login"]
        data = {
            "login": data_login,
            "password": ""
        }
        response = requests.post(Urls.url + Api.api_create_courier, data=data)
        return response

    @staticmethod
    @allure.step("Логин курьера")
    def login_courier(data_payload):
        requests.post(Urls.url + Api.api_create_courier, data=data_payload)
        response = requests.post(Urls.url + Api.api_login_courier, data=data_payload)
        return response

    @staticmethod
    @allure.step("Попытка логина курьера в системе без поля пароль")
    def login_courier_not_field_password():
        data_payload = DataGeneration.register_new_courier_and_return_login_password()
        data = {
            "login": data_payload["login"],
            "password": ""
        }
        response = requests.post(Urls.url + Api.api_login_courier, data=data)
        return response

    @staticmethod
    @allure.step("Попытка залогиниться в систему с несуществующими логином и паролем")
    def login_no_such_username_and_password():
        data_payload = DataGeneration.register_new_courier_and_return_login_password()
        response = requests.post(Urls.url + Api.api_login_courier, data=data_payload)
        return response

class DataOrder:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        response = requests.post(Urls.url + Api.api_order, data=payload)
        return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_list_order():
        response = requests.get(Urls.url + Api.api_order)
        return response