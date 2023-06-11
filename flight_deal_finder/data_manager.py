import requests
from os import environ
from dotenv import load_dotenv

load_dotenv()

SHEETY_URL = environ.get('SHEETY_ENDPOINT')
SHEETY_API_TOKEN = environ.get('SHEETY_API_TOKEN')

class DataManager:

    def __init__(self):
        self.url = SHEETY_URL
        self.token = SHEETY_API_TOKEN
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }

    def put_to_sheety(self, data):
        for element in data:
            endpoint = f'{self.url}{element["id"]}'
            dict = {
                'price': element
            }
            response = requests.put(url=endpoint, headers=self.headers, json=dict)
            response.raise_for_status()

    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        data = response.json()
        return data

    def get_cities(self):
        response_cities = requests.get(url=self.url, headers=self.headers)
        data = response_cities.json()
        cities_list = []
        for destination in data['prices']:
            cities_list.append(destination['city'])
        return cities_list