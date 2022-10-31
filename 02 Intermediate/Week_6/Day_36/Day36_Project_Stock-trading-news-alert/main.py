from stocks import Stocks
from news import News
from mail import Mail

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
smtp_user = input("Please type in the user mail address: ")
smtp_pass = input("Please type in the password: ")
smtp_receiver = input("Please type in the mail address of the receiver: ")

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alert_price_difference = 5

stocks = Stocks(stock_name=STOCK, company_name=COMPANY_NAME, alert_price_difference=alert_price_difference)
data = stocks.get_stock_data()

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news = News(company_name=COMPANY_NAME)
articles = news.get_news_data()

# STEP 3: Use https://www.twilio.com or send per mail
# Send a separate message with the percentage change and each article's title and description to your phone number.
if data[3]:
    text_body = ""
    if data[2] > 0:
        price_direction = "🔺"
    else:
        price_direction = "🔻"
    for i in range(len(articles)):
        text_body = f"{COMPANY_NAME}: {price_direction}{int(round(data[2], 0))}%\n" \
                    f"Headline: {articles[i]['Headline']}\nBrief: {articles[i]['Brief']} "
        mail = Mail(smtp_user, smtp_receiver, smtp_pass)
        mail.sent_mail(f"News about {COMPANY_NAME}!", text_body)
else:
    print("No Alert!")

# Optional: Format the SMS/mail message like this:
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
