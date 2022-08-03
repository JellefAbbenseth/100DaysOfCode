# #################### Extra Hard Starting Project ######################

# mostly not working because of security reasons of the mail providers
# to get it to work, change the settings of the mail provider

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import smtplib

import pandas

LETTERS_PATH: list[str] = [
    "./letter_templates/letter_1.txt",
    "./letter_templates/letter_2.txt",
    "./letter_templates/letter_3.txt",
]


def get_next_birthday(month, day):
    birthday_data = pandas.read_csv("birthdays.csv", ",")
    for (index, row) in birthday_data.iterrows():
        if row.month == month and row.day == day:
            return [row["name"], row.email]
    return []


def get_text(recipient_name):
    with open(random.choice(list(LETTERS_PATH))) as letter_file:
        letter_text = letter_file.read()
        letter_text = letter_text.replace("[NAME]", recipient_name)
    return letter_text


def sent_mail(recipient_name, to_address):
    smtp_host = "imap.gmx.net"
    smtp_user = input("Please type in the user mail address: ")
    smtp_pass = input("Please type in the password: ")
    text_body = get_text(recipient_name)
    try:
        with smtplib.SMTP(smtp_host) as connection:
            connection.starttls()
            connection.login(user=smtp_user, password=smtp_pass)
            connection.sendmail(
                from_addr=smtp_user,
                to_addrs=to_address,
                msg="Subject:Happy Birthday!\n\n" + text_body
            )
    except ConnectionRefusedError:
        print(f"\n{text_body}")


today = dt.datetime.now()
current_day = today.day
current_month = today.month

data_result = get_next_birthday(current_month, current_day)
if len(data_result) > 0:
    name = data_result[0]
    email = data_result[1]
    sent_mail(name, email)
else:
    print("No birthday today!")
