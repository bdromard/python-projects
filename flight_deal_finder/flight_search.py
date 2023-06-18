import requests
from os import environ
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData

load_dotenv()

# API endpoints and token
TEQUILA_SEARCH_URL = 'https://api.tequila.kiwi.com/v2/search'
TEQUILA_LOCATIONS_URL = 'https://api.tequila.kiwi.com/locations/query'
TEQUILA_API_TOKEN = environ.get('TEQUILA_API_TOKEN')

# Time variables
tomorrow = datetime.today() + timedelta(days=1)
six_months_later = datetime.today() + timedelta(days=180)
seven_days_return = datetime.today() + timedelta(days=7)
twenty_eight_days_return = datetime.today() + timedelta(days=28)
TOMORROW_AS_STRING = tomorrow.strftime("%d/%m/%Y")
SEVEN_DAYS_AS_STRING = seven_days_return.strftime("%d/%m/%Y")
TWENTY_EIGHT_DAYS_AS_STRING = twenty_eight_days_return.strftime("%d/%m/%Y")
SIX_MONTHS_AS_STRING = six_months_later.strftime("%d/%m/%Y")

# Class to get IATA codes, look for flights
class FlightSearch:

    def __init__(self):
        self.search_url = TEQUILA_SEARCH_URL
        self.locations_url = TEQUILA_LOCATIONS_URL

    def get_destination_code(self, city_data):
        headers = {'apikey': TEQUILA_API_TOKEN }
        city = city_data['city']
        query = {
            'term': city,
            'limit': 1,
            'location_types': 'city'
        }
        response = requests.get(url=self.locations_url, headers=headers, params=query)
        data = response.json()
        code = data['locations'][0]['code']
        return code

    def get_city_flights(self, destination_code):
        search_headers = {
            'apikey': TEQUILA_API_TOKEN
        }
        search_query = {
            'fly_from': 'CDG',
            'fly_to': destination_code,
            'date_from': TOMORROW_AS_STRING,
            'date_to': SIX_MONTHS_AS_STRING,
            'return_from': SEVEN_DAYS_AS_STRING,
            'return_to': TWENTY_EIGHT_DAYS_AS_STRING,
            'one_for_city': 1,
            'adults': 1,
            'max_stopovers': 0
        }
        # Searching for direct flights first.
        response = requests.get(url=TEQUILA_SEARCH_URL, headers=search_headers, params=search_query)
        response.raise_for_status()
        data = response.json()
        print(data)
        # New request for data if there are no results for direct flights.
        if data['_results'] == 0:
            print(f'Pas de vol direct disponible pour {destination_code}')
            search_query['max_stopovers'] = 1
            new_response = requests.get(url=TEQUILA_SEARCH_URL, headers=search_headers, params=search_query)
            new_response.raise_for_status()
            data = new_response.json()
            print(data)
        
        try:
            flight_data = FlightData(
                price=data['data'][0]['price'],
                origin=data['data'][0]['route'][0]['cityFrom'],
                destination=data['data'][0]['route'][0]['cityTo'],
                airport_origin=data['data'][0]['route'][0]['flyFrom'],
                airport_destination=data['data'][0]['route'][0]['flyTo'],
                depart_from=data['data'][0]['route'][0]['local_departure'].split('T')[0],
                return_date=data['data'][0]['route'][1]['local_departure'].split('T')[0],
                stop_overs=1,
                via_city="Dubai"
            )
        except Exception as error:
            print(error)
        else: 
            print(f'{flight_data.destination} : €{flight_data.price}')
   
            data_for_sheety = {
                'city': flight_data.destination,
                'iataCode': flight_data.airport_destination,
                'lowestPrice': flight_data.price
            }

            return data_for_sheety
