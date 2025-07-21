import requests
from twilio.rest import Client

news_api_key = "5eb05ff5fe404cecb426c4e7de55975b"

twilio_account_sid = "AC5c73a07e65c32ea6da3b23a0602e12f4"
twilio_auth_token = "31958c381a8ce9c914b94918a94f2bb7"

stock_api_key = "ZD3POJCV4BCE5Y6C"

my_number = "+380969638363"
twilio_number = "+15075744375"

stock_name = "TSLA"
company_name = "Tesla Inc"

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"


stock_data = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey": stock_api_key
}

response = requests.get(stock_endpoint, params=stock_data)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

the_day_before_yesterday_data = data_list[1]
the_day_before_yesterday_closing_price = the_day_before_yesterday_data["4. close"]
print(the_day_before_yesterday_closing_price)


difference = float(yesterday_closing_price) - float(the_day_before_yesterday_closing_price)
up_down = "down"
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 1:

    news_params = {
        "apiKey": news_api_key,
        "qInTitle": company_name,
    }

    news_response = requests.get(news_endpoint, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{stock_name}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(twilio_account_sid, twilio_auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_ = twilio_number,
            to = my_number
        )



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

