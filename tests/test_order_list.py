import allure
from scooter_api import DataOrder

class TestOrderList:
    @allure.title('Проверка списка заказов')
    @allure.description('Проверка получения списка заказов')
    def test_order_list(self):
        order_list = DataOrder.get_list_order()
        assert order_list.status_code == 200 and order_list.json()['orders'] != []