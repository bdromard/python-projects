import requests as req

parameters = {
    "amount": 10,
    "type": "boolean",
}
response = req.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
response_data = response.json()

question_data = response_data["results"]