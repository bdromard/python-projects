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

news_api_params = {
    "apikey": decouple.config('NEWS_KEY').strip(),
    "q": COMPANY_NAME,
    "searchIn": "title",
    "pageSize": 3
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Utiliser un module pour déterminer data actuelle et comparer avec données de date choisie
url_alphav = f'https://www.alphavantage.co/query?'
response = req.get(url_alphav, params=alphavantage_params)
response.raise_for_status()
data = response.json()

#   Prettifying data to make it more readable.
pretty_data = json.dumps(data, sort_keys=True, indent=4)
with open('data.json', 'w') as file:
    file.write(pretty_data)
with open('data.json', 'r') as file:
    data_json = json.load(file)

# Get market closures values from yesterday and two days ago, then calculate increase / decrease and print it.
market_closure_key = "4. close"
time_series_daily = data_json["Time Series (Daily)"]
yesterday = list(time_series_daily.values())[-1]
two_days_ago = list(time_series_daily.values())[-2]
yesterday_closure = float(yesterday[market_closure_key])
two_days_ago_closure = float(two_days_ago[market_closure_key])
result = (yesterday_closure - two_days_ago_closure) / yesterday_closure * 100
rounded_result = round(result, 2)

if rounded_result > 0:
    print(f"TSLA: +{rounded_result}")
else:
    print(f"TSLA: -{rounded_result}")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

url_news = "https://newsapi.org/v2/everything?"
response_news = req.get(url_news, params=news_api_params)
response_news.raise_for_status()
data_news = response_news.json()
pretty_data_news = json.dumps(data_news, sort_keys=True, indent=4)

with open('data_news.json', 'w') as news_file:
    news_file.write(pretty_data_news)
with open('data_news.json', 'r') as news_file:
    news_data = json.load(news_file)

for news in news_data['articles'][:3]:
    print(f'HEADLINE: {news["title"]}\n Description: {news["description"]}')

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

