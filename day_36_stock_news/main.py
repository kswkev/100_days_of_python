from stock_service import StockService
from news_service import NewsService
from smsService import SmsService
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
def percentage_change(start_value, end_value):
    difference = start_value - end_value
    percentage = (difference / start_value) * 100
    return round(percentage, 2)


stock_service = StockService()
daily_values = stock_service.get_last_x_days_for(2, STOCK)
yesterday = daily_values[0]
yesterday_open_value = float(yesterday["1. open"])
day_before_yesterday = daily_values[1]
day_before_yesterday_open_value = float(day_before_yesterday["1. open"])

percent_difference = percentage_change(day_before_yesterday_open_value, yesterday_open_value)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# https://newsapi.org/v2/everything?q=tesla&from=2024-01-10&sortBy=publishedAt&apiKey=API_KEY

def get_news():
    newsService = NewsService()
    news_json = newsService.get_last_x_days_news_for_company(7, COMPANY_NAME)
    articles = newsService.return_last_x_articles(3, news_json)
    return newsService.format_data(articles)


def format_message(formatted_data, percentage_change):
    message = f"{STOCK}: "
    if percentage_change > 0:
        message += "🔺"
    elif percentage_change < 0:
        message += "🔻"
    message += f"{abs(percentage_change)}%"

    for article in formatted_data:
        message += (f"\nHeadline: {article["title"]}\n"
                    f"Author: {article["author"]}\n"
                    f"Link: {article["url"]}\n"
                    )
    return message


if abs(percent_difference) >= 5:
    news = get_news()
    message = format_message(news, percent_difference)
    print(message)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    smsService = SmsService()
    smsService.send_message(os.getenv("MY_PHONE"), message)

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

