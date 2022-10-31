import datetime as dt
import random
import smtplib

# mostly not working because of security reasons of the mail providers
# to get it to work, change the settings of the mail provider

weekday = 1


def get_quote():
    with open("quotes.txt") as quotes_file:
        quote_list = quotes_file.readlines()
    return random.choice(list(quote_list))


def sent_mail(text_body):
    smtp_host = "imap.gmx.net"
    smtp_user = input("Please type in the user mail address: ")
    smtp_pass = input("Please type in the password: ")
    to_address = input("Please type in the receivers full mail address: ")
    with smtplib.SMTP(smtp_host) as connection:
        connection.starttls()
        connection.login(user=smtp_user, password=smtp_pass)
        connection.sendmail(
            from_addr=smtp_user,
            to_addrs=to_address,
            msg="Subject:Nice quote\n\n" + text_body
        )


current_day = dt.datetime.now().weekday()

if current_day == weekday:
    quote = get_quote()
    print(quote)
    sent_mail(quote)
else:
    print("Sorry, today there's no quote.")
