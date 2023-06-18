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
    if flights_data == None:
        print('Pas de vol pour cette destination')
        continue
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

# Ask user's information for registration
print("Welcome to Benjamin's Flight Club \n We find the best flight deals and email you")
user_firstname = input('What is your first name?')
user_lastname = input('What is your last name?')
user_email_first = input('What is your email?').lower()
user_email_second = input('Type your email again for validation.').lower()

if user_email_first == user_email_second:
    print("You're in the club!")
    data_mng.post_user_info(user_firstname, user_lastname, user_email_second)
