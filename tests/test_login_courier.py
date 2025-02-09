import allure
from scooter_api import CourierMethods
from conftest import create_and_delete_courier

class TestLoginCourier:
    @allure.title('Проверка успешности логина курьера в систему')
    @allure.description('Создаём аккаунт курьера и логинимся в него, получаем статус 200 и убеждаемся в корректности id')
    def test_successful_courier_login(self, create_and_delete_courier):
        user = CourierMethods.login_courier(create_and_delete_courier)
        assert user.status_code == 200 and user.json()['id'] != 0

    @allure.title('Проверка попытки логина курьера без пароля')
    @allure.description('Пытаемся залогиниться на аккаунт без пароля и получаем ошибку 400 + текст')
    def test_not_password_courier(self):
        user = CourierMethods.login_courier_not_field_password()
        assert user.status_code == 400 and user.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка логина несуществующим курьером')
    @allure.description('Пытаемся залогиниться несуществующим аккаунтом курьера, получаем ошибку 404 + текст')
    def test_no_such_username_and_password(self):
        user = CourierMethods.login_no_such_username_and_password()
        assert user.status_code == 404 and user.json()['message'] == 'Учетная запись не найдена'