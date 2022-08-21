import smtplib
import ssl
import time

import requests
from datetime import datetime

# Challenge:
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

MY_LAT = 52.513550
MY_LONG = 13.387871

smtp_user = input("Please type in the user mail address: ")
smtp_pass = input("Please type in the password: ")


def sent_mail():
    global smtp_user, smtp_pass
    smtp_host = "imap.gmx.net"
    text_body = "Look up, the ISS is over your head!"
    try:
        with smtplib.SMTP(smtp_host) as connection:
            connection.starttls()
            connection.login(user=smtp_user, password=smtp_pass)
            connection.sendmail(
                from_addr=smtp_user,
                to_addrs=smtp_user,
                msg="Subject:ISS!\n\n" + text_body
            )
    except ConnectionRefusedError:
        print(f"\n{text_body}")


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

while True:
    time.sleep(60)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and \
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=ssl.CERT_NONE)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()
        if time_now.hour < sunrise or sunset - 3 < time_now.hour:
            sent_mail()
        else:
            print("ISS overhead but it isn't dark yet!")
    else:
        print("ISS not overhead!")
