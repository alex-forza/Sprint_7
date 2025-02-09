import random
import string
import json
from faker import Faker

class DataGeneration:
    @classmethod
    def register_new_courier_and_return_login_password(cls):
            def generate_random_string(length=10):
                letters = string.ascii_lowercase
                random_string = ''.join(random.choice(letters) for i in range(length))
                return random_string

            login = generate_random_string()
            password = generate_random_string()
            first_name = generate_random_string()

            payload = {
                "login": login,
                "password": password,
                "firstName": first_name
            }

            return payload

class DataGenerationOrder:
    @staticmethod
    def create_data_for_order(color):
        fake = Faker(locale="ru_RU")
        payload = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": random.randrange(10),
            "phone": fake.phone_number(),
            "rentTime": random.randrange(6),
            "deliveryDate": fake.date(),
            "color": color,
            "comment": fake.text(10)
        }

        return json.dumps(payload)