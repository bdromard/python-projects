import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()
now = datetime.now()

# Constants and variables for API headers and queries
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X")

# API URLs
nutritionix_url_exercise = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_url = os.environ.get('SHEETY_ENDPOINT')

# Asking details on workout exercises to send to API
user_input = input('Tell me which exercises you did:')

# API headers
nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json',
    'x-remote-user-id': "0",
}

sheety_headers = {
    'Authorization': f'Bearer {SHEETY_TOKEN}'
}
# API body
user_query = {
    'query': user_input,
    'gender': 'male',
    'weight_kg': '75',
    'height_cm': '184',
    'age': '33'
}

# Nutritionix API response in JSON
response = requests.post(url=nutritionix_url_exercise, headers=nutritionix_headers, json=user_query)
data = response.json()

# Posting to Sheety API
for exercise in data['exercises']:
    post_to_sheety = {
        'sheet1': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].upper(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }}

    response_sheety = requests.post(url=sheety_url, headers=sheety_headers, json=post_to_sheety)
    response_sheety.raise_for_status()
