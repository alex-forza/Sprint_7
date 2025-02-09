import pytest
from data import Urls
from data import Api
import requests
from helpers import DataGeneration

@pytest.fixture()
def create_and_delete_courier():
    data_payload = DataGeneration.register_new_courier_and_return_login_password()
    yield data_payload
    login = requests.post(Urls.url + Api.api_login_courier, data=data_payload)
    id_courier = login.json()['id']
    requests.delete(Urls.url + Api.api_create_courier + str(id_courier))