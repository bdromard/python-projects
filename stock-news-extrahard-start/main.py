import requests as req
import decouple
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alphavantage_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": decouple.config('AV_KEY').strip()
}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Utiliser un module pour déterminer data actuelle et comparer avec données de date choisie
url = f'https://www.alphavantage.co/query?'
response = req.get(url, params=alphavantage_params)
response.raise_for_status()
data = response.json()
pretty_data = json.dumps(data, sort_keys=True, indent=4)
with open('data.json', 'w') as file:
    file.write(pretty_data)
with open('data.json', 'r') as file:
    data_json = json.load(file)
    print(data_json["Time Series (Daily)"]["2022-12-19"]["4. close"])


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

