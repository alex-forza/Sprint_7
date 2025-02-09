import allure
from scooter_api import CourierMethods
from conftest import create_and_delete_courier

class TestRegisterNewCourier:
    @allure.title('Проверка создания аккаунта курьера')
    @allure.description('Создаём аккаунт курьера и проверяем, что код ответа = 201 и тело ответа = {"ok":true}')
    def test_possible_create_courier(self, create_and_delete_courier):
        user = CourierMethods.create_courier(create_and_delete_courier)
        assert user.status_code == 201 and user.text == '{"ok":true}'

    @allure.title('Проверка невозможности создания двух одинаковых аккаунтов')
    @allure.description('Посылаем два запроса с одинаковыми данными регистрации и получаем ошибку')
    def test_duplicate_courier(self, create_and_delete_courier):
        user = CourierMethods.dublicate_create_courier(create_and_delete_courier)
        assert user.status_code == 409 and user.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверка невозможности регистрации курьера без одного обязательного поля')
    @allure.description('Посылаем запрос без поля пароль и пытаемся создать аккаунт; получаем ошибку + текст')
    def test_not_once_required_field(self):
        user = CourierMethods.not_once_required_field()
        assert user.status_code == 400 and user.json()['message'] == 'Недостаточно данных для создания учетной записи'