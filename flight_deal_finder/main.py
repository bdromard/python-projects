#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

# Objects initialization
data_mng = DataManager()
flight_request = FlightSearch()

# Getting data in Google Sheet
sheet_data = data_mng.get_data()['prices']

# Update price for each city in sheet
for city in sheet_data:
    flights_data = flight_request.get_city_flights(city['iataCode'])
    price = {'lowestPrice': flights_data['lowestPrice']}
    city.update(price)

# Send data to sheet
data_mng.put_to_sheety(sheet_data)

# Code to get IATA codes
# for city in sheet_data:
#     code = {'iataCode': FlightSearch.get_destination_code(FlightSearch(), city_data=city)}
#     city.update(code)
#
# data_mng.put_to_sheety(sheet_data)