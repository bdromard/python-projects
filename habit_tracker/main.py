import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

# Accessing token and username through environment variables
user_token = os.environ.get('USER_TOKEN')
username = os.environ.get('USERNAME')

# Getting today's date to post data
today = datetime.now()
yesterday = datetime(year=2023, month=5, day=20)
# Pixela URLs
pixela_users_url = "https://pixe.la/v1/users"
pixela_graph_url = f"https://pixe.la/v1/users/{username}/graphs"
pixela_postdata_url = f"https://pixe.la/v1/users/{username}/graphs/graph1"
pixela_put_url = f"https://pixe.la/v1/users/{username}/graphs/graph1/{today.strftime('%Y%m%d')}"

# Parameters and headers to use in API POST requests
user_params = {"token": user_token,
                        "username": username,
                        "agreeTermsOfService": "yes",
                        "notMinor": "yes"}

graph_params = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "steps",
    "type": "int",
    "color": "ajisai"
}

post_data_params = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "2473"
}

update_data_params = {
    "quantity": "30",
}

headers = {"X-USER-TOKEN": user_token}

# User creation
# response = requests.post(url=pixela_users_url, json=user_params)
# print(response.text)

# Graph creation
# response = requests.post(url=pixela_graph_url, json=graph_params, headers=headers)
# print(response.text)

# Posting data to the graph

# response = requests.post(url=pixela_postdata_url, json=post_data_params, headers=headers)

# Updating data with PUT request
# response = requests.put(url=pixela_put_url, json=update_data_params, headers=headers)

# Deleting data with DELETE request
response = requests.delete(url=pixela_put_url, headers=headers)
print(response.text)