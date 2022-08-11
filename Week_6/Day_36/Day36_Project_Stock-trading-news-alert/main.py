from stocks import Stocks
from news import News

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alert_price_difference = 5

stocks = Stocks(stock_name=STOCK, company_name=COMPANY_NAME, alert_price_difference=alert_price_difference)
data = stocks.get_stock_data()
print(data)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news = News(company_name=COMPANY_NAME)
articles = news.get_news_data()

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
if data[2] > 0:
    price_direction = "🔺"
else:
    price_direction = "🔻"
for i in range(len(articles)):
    print(f"{COMPANY_NAME}: {price_direction}{int(round(data[2], 0))}%\n"
          f"Headline: {articles[i]['Headline']}\n"
          f"Brief: {articles[i]['Brief']}")

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2% 
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have  gone over 821 13F filings that hedge funds 
    and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio 
    positions as of March 31st, near the height of the coronavirus market crash. 
or 
"TSLA: 🔻5% 
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey 
    have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
    filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
    market crash. 
"""
