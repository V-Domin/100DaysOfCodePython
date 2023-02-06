import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_STOCKS = 'E5IKZ8VRY19GMOZL'
API_KEY_NEWS = 'f5fcbda1136d43188d95d7d1c5b7a2f8'

account_sid = 'ACaa02da6a9a5fabe9cb5bc3be0c5184fd'
auth_token = '7056d75362b87b9aa988b1d59b8cf4eb'

parameters = {
    'function':'TIME_SERIES_DAILY_ADJUSTED',
    'symbol':STOCK,
    'apikey':API_KEY_STOCKS,
}

response_stocks = requests.get(STOCK_ENDPOINT, params=parameters)
response_stocks.raise_for_status()
data_stocks = response_stocks.json()['Time Series (Daily)']

# list = []
# for day, info in data.items():
#     list.append(day)
#     list.append(info)
# recent_days = list[0:4]
# yesterday_data = recent_days[1]['4. close']
# day_before = recent_days[3]['4. close']

data_list = [value for (key, value) in data_stocks.items()]
yesterday_data = data_list[0]['4. close']
day_before = data_list[1]['4. close']


positive_difference = abs(float(yesterday_data) - float(day_before))

actual_percent = positive_difference / float(yesterday_data) * 100

parameters_news = {
    'q':COMPANY_NAME,
    'apiKey':API_KEY_NEWS,
}

response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
response_news.raise_for_status()
data_news = response_news.json()['articles'][:3]

if actual_percent > 3:
    for title in data_news:
        title_news = title['title']
        description = title['description'].replace('<a href="https://www.reuters.com/companies/TSLA.O" target="_blank">(TSLA.O)</a>', '')

        if float(yesterday_data) > float(day_before):
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=f"TSLA: 🔺{int(actual_percent)}%\nHeadline: {title_news}\nBrief: {description}",
                from_='+14422672882',
                to='+380668046628'
            )
            print(message.status)
        elif float(yesterday_data) < float(day_before):
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=f"TSLA: 🔻{int(actual_percent)}%\nHeadline: {title_news}\nBrief: {description}",
                from_='+14422672882',
                to='+380668046628'
            )
            print(message.status)


